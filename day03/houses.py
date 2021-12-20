def find_visited(moves):
    x, y = (0,0)
    visited = set()
    visited.add((x,y))
    for move in moves:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '<':
            x -= 1
        elif move == '>':
            x += 1
        visited.add((x,y))
    return visited

def count_houses(moves):
    return len(find_visited(moves))

def cound_double_houses(moves):
    return len(find_visited(moves[::2]).union(find_visited(moves[1::2])))

if __name__ == "__main__":
    with open('day03/input.txt', 'r') as f:
        moves = f.read()

    print('--- Part 1 ---')
    print(count_houses(moves))
    print('--- Part 2 ---')
    print(cound_double_houses(moves))