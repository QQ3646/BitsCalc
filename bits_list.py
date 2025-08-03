from tkinter import *

import sign_and_size

button_list: list[Checkbutton] = list()

def apply(byte, bit) -> None:
    print(f"{byte} {bit}")

def update() -> None:
    from utils import convert_from_dec_to_bin
    import unformatted_value

    b_number = convert_from_dec_to_bin(unformatted_value.get_unformatted_value_as_int(), sign_and_size.get_current_size())

    for i, b in enumerate(reversed(b_number)):
        if b == "1":
            button_list[i].select()
        else:
            button_list[i].deselect()

def update_bits_count():
    for i in button_list[:sign_and_size.get_current_size()]:
        i.grid(i.grid_info_saved)
    for i in button_list[sign_and_size.get_current_size():]:
        i.grid_forget()

def setup_bits_buttons():
    global button_list
    for i in range(0, 1):
        for j in range(7, -1, -1):
            enabled_checkbutton = Checkbutton(command=lambda x=j: apply(0, x))
            enabled_checkbutton.grid(row=3 + i, column=j)
            enabled_checkbutton.grid_info_saved = enabled_checkbutton.grid_info()
            button_list.append(enabled_checkbutton)
