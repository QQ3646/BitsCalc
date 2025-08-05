import bits_list
import notation_selector
from tkinter import *
from typing import Optional

import sign_and_size
from utils import clear_both_values
import formatted_value


_unformatted_value: Optional[StringVar] = None
_unformatted_entry: Optional[Entry] = None

def change_unformatted_value():
    if _unformatted_value.is_programmed_changed_value:
        _unformatted_value.is_programmed_changed_value = False
        return

    if get_unformatted_value() == "":
        formatted_value.mark_as_programmed_edited()
        clear_both_values()
        return

    if get_unformatted_value() == "-":
        if sign_and_size.is_unsigned:
            _unformatted_entry.config(fg="RED")
        return

    if not (sign_and_size.lowerPoint <= get_unformatted_value_as_int() < sign_and_size.upperPoint):
        _unformatted_entry.config(fg="RED")
        return

    _unformatted_entry.config(fg="BLACK")

    notation_selector.change_formatted_value(get_unformatted_value_as_int(), notation_selector.get_current_notation())
    bits_list.update()

def change_format() -> None:
    from utils import convert_from_bin_to_dec
    mark_as_programmed_edited()
    _unformatted_value.set(str(convert_from_bin_to_dec(bits_list.button_list.get_current_bin_number(), sign_and_size.is_unsigned, sign_and_size.get_current_size())))
    notation_selector.change_formatted_value(get_unformatted_value_as_int(), notation_selector.get_current_notation())

def get_unformatted_value() -> str:
    return _unformatted_value.get()

def get_unformatted_value_as_int() -> int:
    return 0 if _unformatted_value.get() == '' else int(_unformatted_value.get())

def mark_as_programmed_edited() -> None:
    _unformatted_value.is_programmed_changed_value = True

def set_unformatted_value_raw(value: int) -> None:
    mark_as_programmed_edited()
    _unformatted_value.set(str(value))

def setup_unformatted_entry() -> None:
    global _unformatted_value, _unformatted_entry
    _unformatted_value = StringVar(value="")

    _unformatted_entry = Entry(textvariable=_unformatted_value)
    _unformatted_entry.grid(row=1, columnspan=4)
    _unformatted_value.is_programmed_changed_value = False
    _unformatted_value.trace_add("write", lambda x1, x2, x3: change_unformatted_value())

def clear() -> None:
    _unformatted_value.set("")
