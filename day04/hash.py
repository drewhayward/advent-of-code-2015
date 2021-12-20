from hashlib import md5
from tqdm import trange

def mine(prefix, difficulty=5):
    target = '0' * difficulty
    for i in trange(1, 10000000):
        hash = md5(f"{prefix}{i}".encode('utf-8')).hexdigest()
        if hash.startswith(target):
            print(hash)
            break

    return i

if __name__ == '__main__':
    print('--- Part 1 ---')
    print(mine('yzbqklnj', 5))
    print('--- Part 2 ---')
    print(mine('yzbqklnj', 6))

