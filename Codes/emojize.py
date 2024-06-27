import emoji
def main():
    x=input("Input: ").strip()
    if ":" in x:
        a,b=x.split(":",1)
        print("Output: ",f"{a}",emoji.emojize(f":{b}",language="alias"),sep="")
    else:
        a=x
        b=""
        print("Output: ",f"{a} {b}",sep="")
        
    
    
if __name__ == "__main__":
    main()