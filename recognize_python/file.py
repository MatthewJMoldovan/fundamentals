num1 = 42 #variable declaration, number, primitive data type
num2 = 2.3 #variable declaration, float 
boolean = True #variable declaration, boolean, primitive data type
string = 'Hello World' #varialbe declaration, string, primitive data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declation, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, object/dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declation, Tuple
print(type(fruit)) #log statmenet, type check, prints class type, 
print(pizza_toppings[1]) #log statment, prints sausage
pizza_toppings.append('Mushrooms') #adds value to pizza_toppings
print(person['name']) #acesses person, logs 'name': 'John'
person['name'] = 'George' #changes value of 'name' to 'George'
person['eye_color'] = 'blue' #adds value of 'eye_color' : 'blue' to dictionary 'person'
print(fruit[2]) #logs banana

if num1 > 45: #conditional, if loop
    print("It's greater") #logs "It's greater"
else: #conditional, else
    print("It's lower") #logs "It's lower"

if len(string) < 5: #conditional, length check, if loop
    print("It's a short word!") #logs "It's a short word!"
elif len(string) > 15: #conditional, length check, elif loop
    print("It's a long word!") #logs "It's a long word!"
else: #conditional, else
    print("Just right!") #logs "Just right!"

for x in range(5): #for loop, variable declaration, conditional
    print(x) #logs x while x < 5
for x in range(2,5): #for loop, variable declartion, conditional
    print(x) #logs x while x is between 2-5
for x in range(2,10,3): #for loop, varialbe declartion, conditional
    print(x) #logs x
x = 0 #varible declaration
while(x < 5): #conditional, while loop
    print(x) #logs x
    x += 1 #changes value of x

pizza_toppings.pop() #deletes value from list pizza_toppings
pizza_toppings.pop(1) #deletes value at index 1 from list pizza_toppings

print(person) #logs the dictionary person
person.pop('eye_color') #deletes the key and value 'eye_color' from dictionary person
print(person) #logs the dictionary person

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional, if loop
        continue #continues forward throughout the loop
    print('After 1st if statement') #logs "After 1st if statement"
    if topping == 'Olives': #conditional, if loop
        break #ends loop

def print_hello_ten_times(): #variable declaration
    for num in range(10): #for loop, conditional, variable declaration
        print('Hello') #log 'Hello'

print_hello_ten_times() #calls function print_hello_ten_times

def print_hello_x_times(x): #variable declaration
    for num in range(x): #for loop, conditional, variable declaration
        print('Hello') #logs 'Hello'

print_hello_x_times(4) #calls function print_hello_x_times, adjust variable

def print_hello_x_or_ten_times(x = 10): #variable declatrion
    for num in range(x): #for loop, conditional, variable declaration
        print('Hello') #logs 'Hello'

print_hello_x_or_ten_times() #calls print_hello_x_or_ten_times, x = 10
print_hello_x_or_ten_times(4) #calls print_hello_x_or_ten_times, x = 4


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)