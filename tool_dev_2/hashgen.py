import hashlib
import sys

###########################################################
#  To use this file, you can insert manually the text to be
#   hashed or you can provide a file.
#
#  To select the hash types, use the appropriate flags on
#  command line: -md5, -sha1, -sha256, -sha512
#
###########################################################


def hashgen_test(msg):
    if '-md5' in sys.argv:
        result = hashlib.md5(msg.encode('utf-8'))
        print('MD5 Hash: ' + result.hexdigest())
    if '-sha1' in sys.argv:
        result = hashlib.sha1(msg.encode('utf-8'))
        print('SHA1 Hash: ' + result.hexdigest())
    if '-sha256' in sys.argv:
        result = hashlib.sha256(msg.encode('utf-8'))
        print('SHA256 Hash: ' + result.hexdigest())
    if '-sha512' in sys.argv:
        result = hashlib.sha512(msg.encode('utf-8'))
        print('SHA512 Hash: ' + result.hexdigest())


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].count('.txt') > 0:
        filename = sys.argv[1]
        message = open(filename, 'r').read()
    else:
        message = input('No input file selected, please inform a text manually: \n')
    hashgen_test(message)
