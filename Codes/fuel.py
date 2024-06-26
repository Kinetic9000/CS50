def fuel(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y or y == 0:
            raise ValueError
        percentage = (x / y) * 100
        return round(percentage)
    except (ValueError, ZeroDivisionError):
        return None

def main():
    while True:
        fraction = input("Fraction: ")
        percentage = fuel(fraction)
        if percentage is not None:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        else:
           continue

if __name__ == "__main__":
    main()

        