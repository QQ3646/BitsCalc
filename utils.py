import bits_list
import formatted_value
import unformatted_value

def convert_from_dec_to_bin(number: int, bits_num: int) -> str:
    def revert(char: str) -> str:
        match char:
            case "0": return "1"
            case "1": return "0"
            case _  : return char
            
    abs_number = abs(number)
    binary = f'{{0:0{bits_num}b}}'.format(abs_number)

    if number < 0:
        binary = bin(int("".join(map(revert, binary)), 2) + 1)[2:]

    return binary

def convert_from_bin_to_dec(number: int, is_unsigned: bool, bits_num: int) -> int:
    if is_unsigned:
        return number
    else:
        if (number >> (bits_num - 1)) == 0:  # positive number
            return number
        else:
            return -((~number & (2 ** bits_num - 1)) + 1)


def clear_both_values() -> None:
    """Clear both values. But fields should manually be marked as `program_edited`."""
    formatted_value.clear()
    unformatted_value.clear()
    bits_list.update()