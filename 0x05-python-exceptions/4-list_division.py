#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nb_print = []
    for i in range(0, list_length):
        try:
            nb_print.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            nb_print.append(0)
        except TypeError:
            print("wrong type")
            nb_print.append(0)
        except ZeroDivisionError:
            print("division by 0")
            nb_print.append(0)
        finally:
            pass
    return nb_print
