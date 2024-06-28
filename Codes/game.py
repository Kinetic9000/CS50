import random
def positive(x):
    while True:
        try:
            value=int(input(x))
            if value > 0:
                return value
            else:
                continue
        except ValueError:
            pass
def main():
    level=int(positive("Level: "))
    number=random.randint(1,level)
    guess=int(positive("Guess: "))
    while guess!=number:
        if guess>number:
            print("Too large!")
        else:
            print("Too small!")
        guess=int(positive("Guess: "))
    print("Just right!")
if __name__=="__main__":
    main()
    
            