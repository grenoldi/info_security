import random
import string

size = 16

chars = string.ascii_letters + string.digits + 'çÇ!@#$%&*()-=+[]{},.;:/?'

rnd = random.SystemRandom()


if __name__ == '__main__':
    print(''.join(rnd.choice(chars) for i in range(size)))
