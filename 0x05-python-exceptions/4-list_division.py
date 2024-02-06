#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div = 0
    new_list = []
    try:
        for i in range(len(my_list_1)):
            for j in range(len(my_list_2)):
                while i == j:
                    div = my_list_1[i] / my_list_2[j]
                    j += 1
            i += 1
    except TypeError:
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    finally:
        new_list.append(div)
        return new_list
