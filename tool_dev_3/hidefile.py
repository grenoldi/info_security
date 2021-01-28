import ctypes

attribute = 0x02

hidden = ctypes.windll.kernel32.SetFileAttributesW('phonenumbers.txt', attribute)


if __name__ == '__main__':
    if hidden:
        print('file successfuly hidden.')
    else:
        print('could not hide the file.')