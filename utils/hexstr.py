"""
Program will translate integer to 4 chars Hex value
Usege : python3 hexstr.py 9435
Output: 24db
"""
import sys

def hexstr(n):
    return "{:04x}".format(n)

def usage():
    print("Wrong Input - Please insert integer to translate into HEX value\nUsege : python3 hexstr.py 9435\nOutput: 24db")

def main():
    if len(sys.argv) > 1:      # sys.argv[0] = python3
        args = sys.argv[1:]    # get args list
        try:
            x = int(args[0])   # x = sys.argv[1]
            print(hexstr(x))
        except:
            usage()            # wrong input fail to int() --> print usage()
    else:
        usage()                # No input parameter --> print usage()
    return 0

if __name__ == "__main__":
    main()

