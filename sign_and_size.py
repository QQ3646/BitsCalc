from tkinter import StringVar, ttk
from typing import Optional


lowerPoint, upperPoint, is_unsigned = 0, 0, False

_size_and_sign_var: Optional[StringVar] = None


def update_lower_and_upper_point():
    global lowerPoint, upperPoint, is_unsigned

    size = int(_size_and_sign_var.get()[1:])
    is_unsigned = _size_and_sign_var.get()[0] == "u"

    lowerPoint = 0           if is_unsigned else -(2 ** (size - 1))
    upperPoint = (2 ** size) if is_unsigned else   2 ** (size - 1)

    from unformatted_value import change_format
    change_format()

    from bits_list import update_bits_count
    update_bits_count()

def get_current_format() -> str:
    return _size_and_sign_var.get()

def get_current_size() -> int:
    return int(get_current_format()[1:])

def setup_sign_and_size() -> None:
    global _size_and_sign_var
    _size_and_sign_var = StringVar()
    size_and_sign = ["i4", "i8", "u8"]
    combobox = ttk.Combobox(textvariable=_size_and_sign_var, values=size_and_sign)
    _size_and_sign_var.trace_add("write", callback=lambda x1, x2, x3: update_lower_and_upper_point())
    _size_and_sign_var.set(size_and_sign[0])
    combobox.grid(row=0, columnspan=4)