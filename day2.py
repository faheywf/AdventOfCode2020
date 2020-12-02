def problem1():
    with open("day2.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    acc = 0
    for password in passwords:
        count, letter, passwd = password.split()
        # clean up inputs
        min_count, max_count = map(int, count.split("-"))
        letter = letter.replace(":", "")
        acceptable = min_count <= passwd.count(letter) <= max_count
        if acceptable:
            acc += 1

    print(acc)

def problem2():
    with open("day2.txt", "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    acc = 0
    for password in passwords:
        count, letter, passwd = password.split()
        # clean up inputs
        idx1, idx2 = map(int, count.split("-"))
        letter = letter.replace(":", "")
        acceptable = (passwd[idx1 - 1] == letter) != (passwd[idx2 - 1] == letter)
        if acceptable:
            acc += 1

    print(acc)

if __name__ == "__main__":
    problem1()
    problem2()