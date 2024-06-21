# def print_instructions():
#     print("Password Manager helps you store, generate, import/export and find your saved passwords.\n"
#           "\n-r, --register           -> register as a new user"
#           "\n-l, --login              -> login to an existing user"
#           "\n-pg, --passwordgenerator -> generate password"
#           "\n-ps, --passwordsave      -> save password"
#           "\n-pi, --passwordimport    -> import password"
#           "\n-pe, --passwordexport    -> export password"
#           "\n-pf, --passwordfind      -> find password"
#           "\n-pu, --passwordupdate    -> update a current password"
#           "\n-pd, --passworddelete    -> delete a stored password"
#           "\n-ud, --userdelete        -> delete a user with all his data")

def print_big_letters():
    letters = {
        'T': [
            " --------- ",
            "|         |",
            " ---   --- ",
            "   |   |   ",
            "   |   |   ",
            "   |___|   ",
        ],
        'H': [
            " _     _   ",
            "| |   | |  ",
            "| |___| |  ",
            "|  ___  |  ",
            "| |   | |  ",
            "|_|   |_|  ",
        ],
        'E': [
            " _______   ",
            "|  _____|  ",
            "| |_____   ",
            "|  _____|  ",
            "| |_____   ",
            "|_______|  ",
        ],
        'O': [
            "  _____    ",
            " //    \   ",
            "||      |  ",
            "||      |  ",
            "||      |  ",
            " \_____/   ",
        ],
        'N': [
            " _     _   ",
            "| \   | |  ",
            "|  \__| |  ",
            "|  _    |  ",
            "| | \   |  ",
            "|_|  \__|  ",
        ],
    }

    max_height = max(len(letters[letter]) for letter in letters)

    for i in range(max_height):
        for letter in 'THEONEO':
            if letter in letters and i < len(letters[letter]):
                print(letters[letter][i], end="  ")
            else:
                print(" " * 13,
                      end="  ")  # If the character is not in the dictionary or the line is out of range, print spaces
        print()
