import notation_selector
from tkinter import *
from tkinter import ttk
from typing import Optional
from utils import clear_both_values
import formatted_value


_unformatted_value: Optional[StringVar] = None

def change_unformatted_value():
    if _unformatted_value.is_programmed_changed_value:
        _unformatted_value.is_programmed_changed_value = False
        return

    if get_unformatted_value() == "":
        formatted_value.mark_as_programmed_edited()
        clear_both_values()
        return

    notation_selector.change_formatted_value(get_unformatted_value_as_int(), notation_selector.get_current_notation())

def get_unformatted_value() -> str:
    return _unformatted_value.get()

def get_unformatted_value_as_int() -> int:
    return int(_unformatted_value.get())

def mark_as_programmed_edited() -> None:
    _unformatted_value.is_programmed_changed_value = True

def set_unformatted_value_raw(value: int) -> None:
    mark_as_programmed_edited()
    _unformatted_value.set(str(value))

def setup_unformatted_entry() -> None:
    global _unformatted_value
    _unformatted_value = StringVar(value="")
    ttk.Entry(textvariable=_unformatted_value).grid(row=1, columnspan=4)
    _unformatted_value.is_programmed_changed_value = False
    _unformatted_value.trace_add("write", lambda x1, x2, x3: change_unformatted_value())

def clear() -> None:
    _unformatted_value.set("")
