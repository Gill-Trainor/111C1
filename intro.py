print('Hello World')

name = 'Gill'
last_name = 'Trainor'
age = 30
found = False
average = 42.23

print(name)
print(last_name)
print(age)
print(found)
print(average)

print(21+21)
print(age - 1)
print(78 * 121)
print(123 / 43)
print(10 % 3) # % = modulus operator(returns the residue of the division)

def test():
    print("inside the fn")
    print("this too")

def separator():
    print('---------------------------')

test()

separator()
print(name + last_name)
print(10 * name)

separator()
print(name + str(23))  #str converts the number into string

separator()

if(age < 90):
    print('You are a young person')
elif(age == 90):
    print('you are on the border line')
else:
    print('sorry bud you are old')