#!/usr/bin/python3
def magic_calculation(a, b):
    nb_print = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Exceeded')
            else:
                nb_print += (a ** b) / i
        except:
            nb_print = b + a
            break
    return nb_print
