from tkinter import *
from tkinter import ttk
from typing import Optional
import notation_selector
import unformatted_value
from notation_selector import Notation, get_current_notation

_formatted_value: Optional[StringVar] = None

def change_formatted_value():
    current_notation = notation_selector.get_current_notation()

    def change_format_manually(new_notation: Notation):
        unformatted_value.set_unformatted_value_raw(unformatted_value.get_unformatted_value_as_int() // current_notation.value)

        notation_selector.change_notation_by_input(new_notation)
        _formatted_value.is_programmed_changed_value = False

    if _formatted_value.is_programmed_changed_value:
        _formatted_value.is_programmed_changed_value = False
        return


    if len(_formatted_value.get()) >= 4:
        may_be_new_format = _formatted_value.get()[-2:]
        match may_be_new_format:
            case "0b":
                change_format_manually(Notation.binary); return
            case "0o":
                change_format_manually(Notation.octal); return
            case "0x":
                change_format_manually(Notation.hexadecimal); return

    unformatted_value.mark_as_programmed_edited()

    if len(_formatted_value.get()) == 2:
        from utils import clear_both_values
        clear_both_values()
        return

    new_value = int(_formatted_value.get(), get_current_notation().value)
    unformatted_value.set_unformatted_value_raw(new_value)

def mark_as_programmed_edited() -> None:
    _formatted_value.is_programmed_changed_value = True

def set_formatted_value_raw(value: str) -> None:
    mark_as_programmed_edited()
    _formatted_value.set(value)

def clear() -> None:
    _formatted_value.set(notation_selector.get_current_notation().get_prefix())

def setup_formatted_value() -> None:
    global _formatted_value
    _formatted_value = StringVar(value="")
    _formatted_value.set(notation_selector.get_current_notation().get_prefix())
    ttk.Entry(textvariable=_formatted_value).grid(row=2, column=2, columnspan=4)
    _formatted_value.is_programmed_changed_value = False
    _formatted_value.trace_add("write", lambda x1, x2, x3: change_formatted_value())
