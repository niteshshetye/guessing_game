def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not an leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not an leap year")


def sqrt_num(num):
    num_sqrt = int(num ** 0.5)
    return num_sqrt


def cube_num(num3):
    num_cube = int(num3 ** (1/3))
    return num_cube


def swap_first_last_number_list(new_list):
    size = len(new_list)
    temp = new_list[0]
    new_list[0] = new_list[size - 1]
    new_list[size - 1] = temp
    return new_list


def update_clue(guess_word, secrete_word, clue):
    index = 0
    while index < len(secrete_word):
        if guess_word == secrete_word[index]:
            clue[index] = guess_word
        index += 1

