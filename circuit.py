import operator

def parse_line(line):
    lhs, rhs = line.split(" -> ")
    lhs = lhs.split(' ')

    def num_convert(inp):
        try:
            return int(inp)
        except:
            return inp

    variable = rhs
    if len(lhs) == 1:
        num = lhs[0]
        expression = ["ID", num_convert(num)]
    elif len(lhs) == 2:
        op, num = lhs
        expression = [op, num_convert(num)]
    elif len(lhs) == 3:
        num1, op, num2 = lhs
        expression = [op, num_convert(num1), num_convert(num2)]
    
    return variable, expression

def as_unsigned(num):
    bits = bin(num)[3:]
    return int(bits, base=2)

def read_input(filename):
    program = {}
    with open(filename) as f:
        lines = f.readlines()
        # remove newlines
        lines = [line.strip() for line in lines]

        for line in lines:
            variable, expr = parse_line(line)
            program[variable] = expr

    return program

def int_invert(num):
    binary = bin(num)[2:].zfill(16)
    inverted = ''.join('1' if b == '0' else '0' for b in binary)
    return int(inverted, base=2)

def get_value(program, variable, memo):
    if variable in memo:
        return memo[variable]

    if isinstance(program[variable], int):
        return program[variable]

    op, *args = program[variable]

    for i, arg in enumerate(args):
        if isinstance(arg, str):
            args[i] = get_value(program, arg, memo)

    OPS = {
        "ID": lambda x: x,
        "AND": operator.and_,
        "NOT": int_invert,
        "OR": operator.or_,
        "LSHIFT": operator.lshift,
        "RSHIFT": operator.rshift
    }

    memo[variable] = OPS[op](*args)
    return memo[variable]


if __name__ == "__main__":
    
    test_program = read_input('test.txt')

    print('--- Part 1 ---')
    program = read_input('input.txt')
    res = get_value(program, 'a', {})
    print(res)

    print('--- Part 2 ---')
    program['b'][1] = res
    print(get_value(program, 'a', {}))