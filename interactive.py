"""
Password generator. 
Generates password using arguments passed to,
or you can use the PasswordGenerator class to access the API directly
"""
import sys

from api import PasswordGenerator, version

def main():
    try:
        from colorama import init
    except ImportError:
        init = lambda wrap: None
    finally:
        init(wrap=True)
    print("\x1b[34mPassword Generator\x1b[39m v\x1b[31m{}\x1b[39m, Written by 000Zer000".format(version))
    print("See the original repo (https://github.com/000Zer000/Password-Generator) for updates and more info")
    try:
        length = int(sys.argv[1])
    except (ValueError, IndexError):
        print("\n\n\x1b[34m[+] Going with default length (13)\x1b[39m\n")
        length = 13
    Gen = PasswordGenerator(length=length)
    while True:
        print("\x1b[33m[*] Press <enter> for a random password (q for quit, l for changing the length)\x1b[39m: ", end="")
        try:
            z = input().strip()
        except EOFError:
            print("Don't do that again")
            continue
        if z == "q":
            break
        elif z == "l":
            while True:
                try:
                    print("\x1b[33m[*] Please enter newer length (old {})\x1b[39m: ".format(length), end="")
                    try:
                        length = int(input().strip())
                    except EOFError:
                        print("Not here")
                        continue
                    Gen = PasswordGenerator(length=length)
                    break
                except ValueError:
                    print("\x1b[31m[-]Ewww, A valid integer please\x1b[39m")
        elif z == "":
            print("\x1b[34m[+] Generated\x1b[39m '", end="")
            for comp in Gen.generate_one2():
                print(comp, end="")
            print("'")
        else:
            print("What do you mean by '{}' ??".format(z))
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
       print("\n\x1b[31m[-] User requested exit, exiting...\x1b[39m")
  