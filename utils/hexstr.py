import sys

def hexstr(n):
    return "{:04x}".format(n)

def main():
    hexString = "No Input Number -\nUsege : python3 hexstr.py 9435\nOutput: 24db"
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        try:
            x = int(args[0])
            hexString = hexstr(x)
        except:
            hexString = "Wrong Input - Please insert integer to translate into HEX value\nUsege : python3 hexstr.py 9435\nOutput: 24db"
    print(hexString)
    return 0

if __name__ == "__main__":
    main()
