def main():
    x=[]
    try:
        while True:
            name=input("Name: ").strip()
            if name:
                x.append(name)
    except EOFError:
        pass
    if len(x)==1:
        print(f"Adieu, adieu, to {x[0]}")
    elif len(x)==2:
        print(f"Adieu, adieu, to {x[0]} and {x[1]}")
    else:
        print(f"Adieu, adieu, to {', '.join(x[:-1])}, and {x[-1]}")
if __name__ == "__main__":
    main()
            
        