Program will translate integer to 4 chars Hex value
Usege : python3 hexstr.py 9435
Output: 24db
"""
import sys

print("Hello From hexstr")
print("The value of __name__ is:", repr(__name__))

def hexstr(n):
    return "{:04x}".format(n)

def usage():
    print("Wrong Input - Please insert integer to translate into HEX value\nUsege : python3 hexstr.py 9435 255 111\nOutput: 24db")

def main():
    if len(sys.argv) > 1:      # sys.argv = {"hexstr.py","9435","255","111"}
        args = sys.argv[1:]    # args = {"9435"}
        try:
            for x in args:
                print(hexstr(int(x)))
        except:
            usage()            # wrong input --> print usage()
    else:
        usage()                # wrong input --> print usage()
    return 127

if __name__ == "__main__":
    main()
