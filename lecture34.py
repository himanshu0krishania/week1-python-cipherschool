name,char = input("enter coma separated name and charecter: ").split(",")
print(f"length of your name is {len(name)}")
print(f"charecter count:{name.lower().count(char.lower())}")