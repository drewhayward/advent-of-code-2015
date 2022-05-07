
import enum


def has_double(s):
    prev = None
    for c in s:
        if prev and c == prev:
            return True
        prev = c
    return False

def num_vowels(s):
    vowels = 'aeiou'
    return sum(1 for c in s if c in vowels)

def banned(s):
    for pair in ['ab', 'cd', 'pq', 'xy']:
        if pair in s:
            return True
    return False

def two_pair(s):
    pairs = set()
    prev = None
    for i, c in enumerate(s):
        if i - 1 < 0: continue

        pair = s[i-1:i+1]
        if pair in pairs:
            return True

        pairs.add(prev)
        prev = pair
    return False

def mirrored(s):
    for i, c in enumerate(s):
        if i - 2 < 0: continue

        if c == s[i - 2]:
            return True
    return False        


def is_nice(s):
    return has_double(s) and num_vowels(s) >= 3 and not banned(s)

def is_nice2(s):
    return two_pair(s) and mirrored(s)

if __name__ == "__main__":
    test = "ugknbfddgicrmopn"
    print(test, is_nice(test))

    print('--- Part 1 ---')
    with open('strings.txt','r') as f:
        strings = f.read().split('\n')
    
    print(sum(1 for s in strings if is_nice(s)))

    print('--- Part 2 ---')
    print(sum(1 for s in strings if is_nice2(s)))
    