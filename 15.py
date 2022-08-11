import requests

print("moshe")

try:
    response = requests.get("httd://github.com")
except Exception as e:
    print("something is wrong")
    print(e.args)
print("haim")


try:
    f = int(input("enter number: "))
    r = 5/0
except ZeroDivisionError:
    print("could not divide by zero")
except ValueError:
    print("enter a legal number")
except BaseException as e:
    print("something went wrong, here's why:")
    print(e.args)
