
def paper(dims):
    l, w, h = dims
    return 2*l*w + 2*w*h + 2*l*h + min(l*w, w*h, l*h)

def ribbon(dims):
    l, w, h = dims
    return l*w*h + min(2*(l+w), 2*(w+h), 2*(l+h))

if __name__ == "__main__":
    with open('day02/input.txt') as f:
        all_dims = list(tuple(map(int, line.split('x'))) for line in f.read().splitlines())

    print('--- Part 1 ---')
    print(sum(paper(dims) for dims in all_dims))
    print('--- Part 2 ---')
    print(sum(ribbon(dims) for dims in all_dims))
