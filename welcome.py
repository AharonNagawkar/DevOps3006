is_true = False

a = 2
b = 2.5

strOne = "One"
strThree = "Three"

if a < b:
    print("a is smaller than b")
elif a == b:
    print("a equals b")
else:
    print("something")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == f)
print(k is f)
print(t == e)
print(t is e)
print(type(k) is int)
print(type(k) == int)