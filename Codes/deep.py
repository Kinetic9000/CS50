x=input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()
match x:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")
