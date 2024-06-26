def main():
    x=input("camelCase: ").strip()
    print("snake_case: ",end="")
    for i in x:
        if i.isupper():
            print("_"+i.lower(),end="")
        else:
            print(i,end="")
if __name__ == "__main__":
    main()