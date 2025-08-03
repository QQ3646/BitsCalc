from tkinter import *

import bits_list
import formatted_value
import notation_selector
import sign_and_size
import unformatted_value

if __name__ == '__main__':
    root = Tk()
    root.title("BitsCalc")
    root.geometry("250x300")

    sign_and_size.setup_sign_and_size()
    unformatted_value.setup_unformatted_entry()
    notation_selector.setup_notation_dropdown_list()
    formatted_value.setup_formatted_value()
    bits_list.setup_bits_buttons()

    # root.wm_attributes("-topmost", True)
    # root.bind("<FocusOut>", lambda e: root.quit())
    root.mainloop()
