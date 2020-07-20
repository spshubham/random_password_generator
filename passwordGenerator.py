from passwordCreator import PasswordC
import argparse

args = argparse.ArgumentParser("Usage: python passwordGenerator.py -c CHARSET -l LENGTH")
#args = argparse.ArgumentParser()
args.add_argument('charset')
args.add_argument('-l','--length',default=8)
options  = args.parse_args()
print(options.charset)
print(options.length)

password = PasswordC(options.charset,int(options.length))
password.set_the_charset()
password.generate_password()
print("Random password is :",password.get_password())