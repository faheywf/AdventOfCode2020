
def problem1():
    with open("day1_part1.txt", "r") as f:
        entries = [int(line.strip()) for line in f.readlines()]

    for i in range(len(entries)):
        n = entries[i]
        for j in range(i+1, len(entries)):
            m = entries[j]
            if n + m == 2020:
                print(n * m)
                return

def problem2():
    with open("day1_part1.txt", "r") as f:
        entries = [int(line.strip()) for line in f.readlines()]

    for i in range(len(entries)):
        n = entries[i]
        for j in range(i+1, len(entries)):
            m = entries[j]
            for k in range(j+1, len(entries)):
                o = entries[k]
                if n + m + o == 2020:
                    print(n * m * o)
                    return

if __name__ == "__main__":
    problem1()
    problem2()