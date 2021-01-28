import itertools
import sys


def wordlistgen(text):
    if '-size' in sys.argv:
        size = int(sys.argv[3])
        result = itertools.permutations(text, size)
    else:
        result = itertools.permutations(text, len(text))
    c = 0
    for i in result:
        c += 1
        print(c)
        print(''.join(i))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].count('.txt') > 0:
        filename = sys.argv[1]
        message = open(filename, 'r').read()
    else:
        message = input('No input file selected, please inform a text manually: \n')
    wordlistgen(message)
