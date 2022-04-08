import sys

def hexstr(n):
    return "{:04x}".format(n)

def main():
    hexString = "No Input Number -\nUsege : python3 hexstr.py 4435"
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        try:
            x = int(args[0])
            hexString = hexstr(x)
        except:
            hexString = "Wrong Input - Please insert integer to translate into HEX value\nUsege : python3 hexstr.py 4435"
    print(hexString)
    return 0

if __name__ == "__main__":
    main()
