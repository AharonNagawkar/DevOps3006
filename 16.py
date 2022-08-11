def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age cannot be negative")


try:
    get_age()
except ValueError as e:
    if len(e.args) > 0:
        if e.args[0] == "age cannot be negative":
            print("blabla")
        else:
            print(f"Here is the reason: {e.args[0]}")
    else:
        print(e.args)
