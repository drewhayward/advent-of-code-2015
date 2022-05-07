from pprint import pprint
from itertools import product
import re

def read_input(filename):
    pat = r'([\w ]+) (\d+),(\d+)[\w ]+?(\d+),(\d+)'
    commands = []
    points = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            res = re.match(pat, line)
            commands.append(res.groups()[0])
            points += [list(map(int, res.groups()[1:]))]
    return commands, points

def run_program(commands, points):
    board = {(x,y): False for x, y in product(range(1000), range(1000))}

    for command, (x1, y1, x2, y2) in zip(commands, points):
        for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if command == 'turn on':
                board[(x,y)] = True 
            elif command == 'turn off':
                board[(x,y)] = False
            else:
                board[(x,y)] = not board[(x,y)]

    return sum(1 for b in board.values() if b)

def run_program2(commands, points):
    board = {(x,y): 0 for x, y in product(range(1000), range(1000))}

    for command, (x1, y1, x2, y2) in zip(commands, points):
        for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1)):
            if command == 'turn on':
                board[(x,y)] += 1 
            elif command == 'turn off':
                board[(x,y)] = max(0, board[(x,y)] - 1)
            else:
                board[(x,y)] += 2

    return sum(board.values())

if __name__ == "__main__":

    print('--- Part 1 ---')
    commands, points = read_input('input.txt')
    print(run_program(commands, points))
    
    print('--- Part 2 ---')
    print(run_program2(commands, points))