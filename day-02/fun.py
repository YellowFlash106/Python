def greet_alice():
    print('hello , alice')

def greet(name, lname):
    print(f'hello, {name} {lname}')

# greet("dave","ok")
# greet(name="alice",lname="ok")
def greet(name, lname="ok"):
    print(f'hello, {name} {lname}')

greet("dave")
greet(name="alice",lname="ok")