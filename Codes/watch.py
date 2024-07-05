import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    p= r'src="(https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+))"'
    match = re.search(p,s)
    if match:
       id= match.group(2)
       return f"https://youtu.be/{id}"
    else:
       return None





if __name__ == "__main__":
    main()