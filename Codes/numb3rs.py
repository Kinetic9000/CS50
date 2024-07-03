import re
import sys
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    x=re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)
    try:
        if 0<=int(x.group(1))<=255 and 0<=int(x.group(2))<=255 and 0<=int(x.group(3))<=255 and 0<=int(x.group(4))<=255:
            return True
        else:
            return False
    except:
        sys.exit("False")
if __name__ == "__main__":  
    main()