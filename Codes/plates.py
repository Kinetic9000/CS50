
            
           
def main():
    plate = input("Enter a vanity plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
 if 2 <= len(s) <= 6 and  s.isalnum() and s[0:2].isalpha():
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            return s[i:].isdigit()
    return True

if __name__ == "__main__":
    main()
