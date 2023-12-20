#!/usr/bin/python3
def magic_calculation(a, b):
    j = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            j += a ** b / i
        except Exception:
            j = b + a
            break
    return j
