import sys
from api import PasswordGenerator

def main():
    try:
        length = int(sys.argv[1])
    except (ValueError, IndexError):
        print("usage: generator.py length\n    Generate a random password\n\nGoing with default length (13)")
        length = 13
    Gen = PasswordGenerator(length=length)
    for comp in Gen.generate_one2():
        print(comp, end="")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        raise SystemExit(1)