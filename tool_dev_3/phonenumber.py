import phonenumbers
import sys
from phonenumbers import geocoder, carrier


def print_number_info(phone_number):
    pn = phonenumbers.parse(phone_number)
    ro_number = phonenumbers.parse(phone_number, "RO")
    print('' + carrier.name_for_number(ro_number, 'pt') + ': ' + geocoder.description_for_number(pn, 'pt'))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].count('.txt') > 0:
        filename = sys.argv[1]
        phones = open(filename, 'r').read().split('\n')
        for phone in phones:
            if len(phone) > 0:
                print_number_info(phone)
    else:
        phone = input('No input file selected, please inform a phone number manually: \n')
        ro_number = phonenumbers.parse(phone, "RO")
        print(carrier.name_for_number(ro_number, 'pt'))
        print_number_info(phone)
