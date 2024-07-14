import re
def validate(email):
    if re.match(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email):
        return True
    else:
        return False
def main():
     x=input("Email: ").strip()
     if validate(x):
         print("Valid")
     else:
         print("Invalid")
if __name__ == "__main__":
    main()
    