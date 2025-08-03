import formatted_value
import sign_and_size
import unformatted_value
from tkinter import *
from tkinter import ttk
from typing import Optional
import enum

__all__ = ['select_notation', 'setup_notation_dropdown_list']

class Notation(enum.Enum):
    binary = 2
    octal = 8
    hexadecimal = 16

    @classmethod
    def as_list(cls) -> list:
        return [cls.binary, cls.octal, cls.hexadecimal]

    @classmethod
    def from_base(cls, base: int):
        match base:
            case 2:  return cls.binary
            case 8:  return cls.octal
            case 16: return cls.hexadecimal
            case _:  raise AssertionError(f"There is no notation with base '{base}'.")

    @classmethod
    def from_name(cls, name: str):
        match name:
            case "bin": return cls.binary
            case "oct": return cls.octal
            case "hex": return cls.hexadecimal
            case _:  raise AssertionError(f"There is no notation with name '{name}'.")

    def get_prefix(self) -> str:
        match self:
            case Notation.binary:      return "0b"
            case Notation.octal:       return "0o"
            case Notation.hexadecimal: return "0x"

    def get_name(self) -> str:
        match self:
            case Notation.binary:      return "bin"
            case Notation.octal:       return "oct"
            case Notation.hexadecimal: return "hex"

    def format_number(self, number: int) -> str:
        match self:
            case Notation.binary:      return bin(number).upper()[2:]
            case Notation.octal:       return oct(number).upper()[2:]
            case Notation.hexadecimal: return hex(number).upper()[2:]



_notations = list(map(lambda x: x.get_name(), Notation.as_list()))
_notations_variable: Optional[StringVar] = None

def select_notation() -> None:
    """
    Invokes when notation selected from dropdown list. Gets current number from
    unformatted field and change formatted value.
    """
    change_formatted_value(unformatted_value.get_unformatted_value_as_int(), get_current_notation())

def change_formatted_value(decimal_number: int, notation: Notation) -> None:
    from utils import convert_from_dec_to_bin

    b_number = convert_from_dec_to_bin(decimal_number, sign_and_size.get_current_size())
    formatted_value.set_formatted_value_raw(
        notation.get_prefix() +
        notation.format_number(int(b_number, 2))
    )

def change_notation_by_input(new_notation: Notation) -> None:
    _notations_variable.set(new_notation.get_name())
    select_notation()

def setup_notation_dropdown_list() -> None:
    global _notations_variable
    _notations_variable = StringVar(value=_notations[0])

    # TODO: change combobox with custom thing and merge `notation selector` with formatted value
    notation_list = ttk.Combobox(textvariable=_notations_variable, values=_notations, width=6)
    notation_list.bind("<<ComboboxSelected>>", lambda _: select_notation())
    notation_list.grid(row=2, columnspan=2, column=0)

def get_current_notation_as_str() -> str:
    return _notations_variable.get()

def get_current_notation() -> Notation:
    return Notation.from_name(_notations_variable.get())