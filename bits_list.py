from tkinter import *

button_list = list()

def apply(byte, bit) -> None:
    print(f"{byte} {bit}")


def setup_bits_buttons():
    for i in range(0, 1):
        for j in range(0, 8):
            enabled_checkbutton = Checkbutton(command=lambda x=j: apply(0, x))
            enabled_checkbutton.grid(row=3 + i, column=j)
            button_list.append(enabled_checkbutton)
