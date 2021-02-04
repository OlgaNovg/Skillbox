import random

HIDDEN_NUMBER = None


def guess_number():
    global HIDDEN_NUMBER
    digits = list(range(9))
    res = [0, 0, 0, 0]
    for i in range(4):
        if i == 0:
            d = random.randint(1, 9)
        else:
            d = random.randint(0, len(digits) - 1)

        res[i] = digits[d]
        del digits[d]

    HIDDEN_NUMBER = int("".join(str(x) for x in digits))


def check_number(user_number):

    if not isinstance(user_number, int) or user_number // 1000 == 0:
        return False

    hidden_num_str, user_num_str = str(HIDDEN_NUMBER), str(user_number)
    bulls, cows = 0, 0
    for i in range(4):
        if hidden_num_str[i] == user_num_str[i]:
            bulls += 1
        elif user_num_str[i] in list(hidden_num_str):
            cows += 1

    return {"bulls": bulls, "cows": cows}


if __name__ == "__main__":
    print(HIDDEN_NUMBER)
    guess_number()
    print(HIDDEN_NUMBER)

    check_number(2563)