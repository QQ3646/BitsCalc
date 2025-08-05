from tkinter import *

import sign_and_size

class BitsButtonList:
    button_list: list[Checkbutton] = list()
    state_list: list[bool] = list()
    size: int = 0

    def resize(self) -> None:
        for b in self.button_list[:sign_and_size.get_current_size()]:
            b.grid(b.grid_info_saved)
        for b, s_idx in list(zip(self.button_list, range(0, len(self.state_list))))[sign_and_size.get_current_size():]:
            b.grid_forget()
            self.state_list[s_idx] = False

    def get_current_bin_number(self) -> int:
        number = 0
        for button_state in reversed(self.state_list):
            number <<= 1
            number += 1 if button_state else 0
        return number


button_list = BitsButtonList()

def apply(byte, bit) -> None:
    print(f"{byte} {bit}")

    button_list.state_list[bit] = not button_list.state_list[bit]
    number = button_list.get_current_bin_number()

    from unformatted_value import _unformatted_value
    from utils import convert_from_bin_to_dec
    _unformatted_value.set(str(convert_from_bin_to_dec(number, sign_and_size.is_unsigned, sign_and_size.get_current_size())))

def update() -> None:
    from utils import convert_from_dec_to_bin
    import unformatted_value

    b_number = reversed(convert_from_dec_to_bin(unformatted_value.get_unformatted_value_as_int(), sign_and_size.get_current_size()))

    for i, b in enumerate(b_number):
        if b == "1":
            button_list.button_list[i].select()
        else:
            button_list.button_list[i].deselect()

def update_bits_count():
    button_list.resize()

def setup_bits_buttons():
    global button_list
    for i in range(0, 1):
        for j in range(8):
            enabled_checkbutton = Checkbutton(command=lambda x=j: apply(0, x))
            enabled_checkbutton.grid(row=3 + i, column=7 - j)
            enabled_checkbutton.grid_info_saved = enabled_checkbutton.grid_info()
            button_list.button_list.append(enabled_checkbutton)
            button_list.state_list.append(False)
