x=input("Input: ").strip()
print("Output: ",end="")
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        continue
    else:
        print(i,end="")