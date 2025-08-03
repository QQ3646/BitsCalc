import formatted_value
import unformatted_value

def convert_from_dec_to_bin(number: int, sign_and_sign: str) -> str:
    def revert(char: str) -> str:
        match char:
            case "0": return "1"
            case "1": return "0"
            case _  : return char
            
    abs_number = abs(number)
    bits_num = int(sign_and_sign[1:])
    binary = f'{{0:{bits_num}b}}'.format(abs_number)

    if number < 0:
        binary = bin(int("".join(map(revert, binary)), 2) + 1)[2:]

    return binary

def clear_both_values() -> None:
    """Clear both values. But fields should manually be marked as `program_edited`."""
    formatted_value.clear()
    unformatted_value.clear()