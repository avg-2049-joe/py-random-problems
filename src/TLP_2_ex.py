"""
Problems intended to explore problem solving techniques
"""


def print_v_shape():
    """
    Using a v shape using the '#' character

    ########
     ######
      ####
       ##
    """

    char_to_use = '#'
    num_spaces = 0
    length_required = 8
    chars_to_print = length_required - 2 * (num_spaces)

    while(chars_to_print > 0):

        # print the first spaces
        for _ in range(0, num_spaces):
            print(" ", end="")

        # print the character
        for _ in range(0, chars_to_print):
            print(char_to_use, end="")

        # print the last spaces
        for _ in range(0, num_spaces):
            print(" ", end="")

        print("")

        num_spaces += 1
        chars_to_print = length_required - 2 * (num_spaces)


def print_eye_shape():
    """
    Print the following shape
        ##    
       ####   
      ######
     ########
      ######
       ####
        ##
    """

    char_to_use = '#'

    for num_lines in range(7, 0, -1):

        num_spaces = abs(4 - num_lines)

        # first print spaces
        for _ in range(0, num_spaces):
            print(" ", end="")

        # print the character
        num_chars = 8 - 2*(num_spaces)
        for _ in range(0, num_chars):
            print(char_to_use, end="")

        # print the spaces
        for _ in range(0, num_spaces):
            print(" ", end="")

        # print a new line char at the end of each loop
        print("")


def print_weird_shape():
    """
    #            #
     ##        ##
      ###    ###  
       ########   
       ########
      ###    ###
     ##        ##
    #            #
    """

    for num_lines in [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]:

        num_middle_spaces = abs(14 - 2 * (2 * num_lines - 1))

        # print begin spaces
        for _ in range(0, num_lines - 1):
            print(" ", end="")

        # print char
        for _ in range(0, num_lines):
            print("#", end="")

        # print middle spaces
        for _ in range(0, num_middle_spaces):
            print(" ", end="")

        # print char
        for _ in range(0, num_lines):
            print("#", end="")

        # print end spaces
        for _ in range(0, num_lines - 1):
            print(" ", end="")

        print("")


if __name__ == "__main__":
    print_weird_shape()
