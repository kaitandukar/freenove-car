"""MicroPython driver for Freenove Pico Mecanum wheels (GPIO from original headers)."""
from machine import Pin, PWM, ADC, time_pulse_us
from time import sleep, sleep_us

class Car:
    def __init__(self):
        # M1 front left, M2 rear left, M3 front right, M4 rear right.
        self.motors = []
        for a, b in ((18,19), (21,20), (7,6), (9,8)):
            pair = (PWM(Pin(a)), PWM(Pin(b)))
            for p in pair:
                p.freq(500)
                p.duty_u16(0)
            self.motors.append(pair)
        self.servo = PWM(Pin(13))
        self.servo.freq(50)
        self.trig = Pin(4, Pin.OUT, value=0)
        self.echo = Pin(5, Pin.IN)
        self.battery = ADC(26)
        self.light_left = ADC(28)
        self.light_right = ADC(27)
        self.tracking = (Pin(12, Pin.IN), Pin(11, Pin.IN), Pin(10, Pin.IN))
        self.buzzer = PWM(Pin(2))
        self.buzzer.duty_u16(0)

    def move(self, m1, m2, m3, m4):
        for speed, (forward, backward) in zip((m1,m2,m3,m4), self.motors):
            speed = max(-100, min(100, speed))
            # Disable both directions before switching to avoid overlap.
            forward.duty_u16(0)
            backward.duty_u16(0)
            (forward if speed >= 0 else backward).duty_u16(round(abs(speed)*65535/100))

    def stop(self):
        self.move(0,0,0,0)

    def servo_angle(self, angle):
        angle = max(30, min(150, angle))
        # Original: 2.5%-12.5% duty at 0-180 degrees, 50 Hz.
        pulse_us = 500 + angle * (2000/180)
        self.servo.duty_u16(round(pulse_us/20000*65535))

    def distance_cm(self):
        self.trig.value(0)
        sleep_us(2)
        self.trig.value(1)
        sleep_us(10)
        self.trig.value(0)
        try:
            duration = time_pulse_us(self.echo, 1, 30000)
            return duration / 58.0 if duration >= 0 else None
        except OSError:
            return None

    def drive(self, left, right):
        self.move(left, left, right, right)

    def servo_sweep(self, start, end, delay_ms=10):
        step = 1 if end >= start else -1
        for angle in range(start, end + step, step):
            self.servo_angle(angle)
            sleep(delay_ms / 1000)

    def beep(self, frequency=2000, duration_ms=150):
        self.buzzer.freq(frequency)
        self.buzzer.duty_u16(32768)
        try:
            sleep(duration_ms / 1000)
        finally:
            self.buzzer.duty_u16(0)

    def battery_adc(self):
        return self.battery.read_u16() * 1023 // 65535

    def battery_voltage(self, coefficient=3.0):
        # Default coefficient is an estimate; calibrate against a multimeter.
        return self.battery.read_u16() * 3.3 / 65535 * coefficient

    def light_values(self):
        return (self.light_left.read_u16() * 1023 // 65535,
                self.light_right.read_u16() * 1023 // 65535)

    def track_values(self):
        return tuple(pin.value() for pin in self.tracking)

    def close(self):
        self.stop()
        for pair in self.motors:
            for p in pair:
                p.deinit()
        self.servo.deinit()
        self.buzzer.deinit()
