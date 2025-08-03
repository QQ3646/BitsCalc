from tkinter import StringVar, ttk
from typing import Optional

lowerPoint, upperPoint = 0, 0

_size_and_sign_var: Optional[StringVar] = None


def update_lower_and_upper_point(var, index, mode):
    global lowerPoint, upperPoint

    size = int(_size_and_sign_var.get()[1:])
    is_unsigned = _size_and_sign_var.get()[0] == "u"

    lowerPoint = 0           if is_unsigned else -(2 ** (size - 1))
    upperPoint = (2 ** size) if is_unsigned else   2 ** (size - 1)

def setup_sign_and_size() -> None:
    global _size_and_sign_var
    _size_and_sign_var = StringVar()
    size_and_sign = ["i4", "i8", "u8"]
    combobox = ttk.Combobox(textvariable=_size_and_sign_var, values=size_and_sign)
    _size_and_sign_var.trace_add("write", callback=update_lower_and_upper_point)
    _size_and_sign_var.set(size_and_sign[0])
    combobox.grid(row=0, columnspan=4)