def count_floors(s):
    floor = 0
    for c in s:
        if c == '(':
            floor += 1
        else:
            floor -= 1

    return floor

def first_basement(s):
    floor = 0
    for i, c in enumerate(s):
        if c == '(':
            floor += 1
        else:
            floor -= 1

        if floor < 0:
            break

    return i + 1
if __name__ == "__main__":
    with open('day01/input.txt') as f:
        s = f.read()

    print('--- Part 1 ---')
    print(count_floors(s))
    print('--- Part 2 ---')
    print(first_basement(s))