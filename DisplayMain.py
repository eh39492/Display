from machine import Pin
from random import randint
from time import sleep_ms
button = Pin(3, Pin.IN, Pin.PULL_UP)
previous_state = button.value()
segment_a = Pin(2, Pin.OUT, value=0)
segment_b = Pin(6, Pin.OUT, value=0)
segment_c = Pin(7, Pin.OUT, value=0)
segment_d = Pin(21, Pin.OUT, value=0)
segment_e = Pin(10, Pin.OUT, value=0)
segment_f = Pin(8, Pin.OUT, value=0)
segment_g = Pin(20, Pin.OUT, value=0)
digits = (
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1),  # 9
)
segments = (segment_a, segment_b, segment_c, segment_d, segment_e, segment_f, segment_g)
while True:
    current_state = button.value()
    if previous_state == 1 and current_state == 0:
        number = randint(0, 9)
        for segment, state in zip(segments, digits[number]):
            segment.value(state)
        print(number)
    previous_state = current_state
    sleep_ms(100)
    
