def main():
    x = input("Greeting: ").strip().lower()

    if x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")
if __name__ == "__main__":
    main()