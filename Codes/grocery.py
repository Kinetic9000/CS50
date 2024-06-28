def main():
    d=[]
    f=[]
    try:
        while True:
            x=input("").strip().upper()
            if x:
                d.append(x)
            
    except EOFError:
        pass
    for i in d:
        if i not in f:
            f.append(i)
    y=1
    f.sort()
    for j in f:
        print(y,j)
        y+=1
if __name__ == "__main__":
    main()