age = 25
print(age)

age1 = 1
age_2 = 2
age_of_user = 7


result = 20 / 3
print(result)

print("Here is a floor version (crop decimal):", 20 // 3)

result = 5 ** 3
print(result)

print(round(20 / 3, 0))

print(int(20 / 3))

print(result / age)

print(20 / 3 + 1)

print((20 / 3) + 1)

print(20 / (3 + 1))

print(5 ** 5)

print(78 % 11)

age = 30
age += 1
print(age)

age = 300
age /= 9
print(age)

me = "Jared"
print("/n")

me = "J\ta\tr\te\td"
print(me)

you = 'John'
me = "Jared"
print(me, you)

single_quotes = 'She said "Hi"'
print(single_quotes)

double_quotes = "She said \"Hi\""
print(double_quotes)

single_quotes = 'I\'m learning!'
print(single_quotes)

double_quotes = "I'm learning!"
print(double_quotes)

print(r"as raw as I\'ve ever seen. \/\/ () \/\/. \t")

msg = me + " + " + you
print(msg)

print(me, "+", you)

print("my " "name " "is " "Jared")

msg = f"{me} + {you}"
print(msg)

print("""Name: Jared
      Age: 30""")

print("""\
      Name: Jared. \
      Age: 30""")

msg = "This is a very important message."
print(msg[5])

print(msg[0] + "acos")

msg[-1]

msg = "This is a very important message."
print(msg[-0])
print(-0)
print(0 == -0)

msg = "This is a very important message."
print(msg[1:3])

print(msg[:5])
print(msg[1:])
print(msg[:])

print(msg[-8:])



msg = "Java is my favorite!"
# msg[0] = 'K'
new = 'K' + msg[1:]
print(new)

msg = 'K' + msg[1:]
print(msg)

language = "Java"
language += " is actually coffee"
print(language)

name = "Jared"
print(len(name))
print("Index 4:", name[4])
print("Last index:", name[len(name) -1])

length = len(name)
msg = "length is " + str(length)
print(msg)

ages = [20, 25, 20]

names = ["Jared", "Emily", "Sabrina"]
my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]
print(ages)
print(names)
print(my_favorite_things)

print(ages[2])
print(ages[1:])
print(my_favorite_things[2])
print(my_favorite_things[2][1])

ages[0] = 5
ages[1] = 10
ages[2] = 15
print(ages)

names = ["Jared", "Emily", "Sabrina"]
names2 = names[:]
names2[0] = "Gared"
print(names)

my_favorite_things = ["Working out", 7, ["netlix", "Amazon Prime"]]
my_favorite_things2 = my_favorite_things.copy();
my_favorite_things[2][0] = "Audible"
print(my_favorite_things2)

import copy
my_favorite_things3 = copy.deepcopy(my_favorite_things)
my_favorite_things[2][0] = "Hulu"
print(my_favorite_things)
print(my_favorite_things3)

good = ["kale", "brocolli", "spinach"]
bad = ["pizza", "fries", "wings"]
just_right = good + bad
print(just_right)

good += bad
print(good)

good.extend(bad)
print(good)

good.append("green beans")
print(good)

good = ["kale", "brocolli", "spinach"]
removed = good.pop()
print(removed)

# print("What is your name? ")
# name = input()

# name = input("What is your name? ")
# print("hello " + name)


# num1 = input("What is your favorite number? ")
# num2 = input("what is your second favorite number? ")
# print(num1, "+", num2, "=", num1 + num2)


# num1 = input("What is your favorite number? ")
# num2 = input("what is your second favorite number? ")
# print(type(num1), type(num2))

# num1 = float(num1)
# num2 = float(num2)
# print(type(num1), type(num2))

# print(num1, "+", num2, "=", num1 + num2)

# num1, num2 = input("What are your favorite 2 numbers (separated by spaces): ").split()
# print(num1, num2)
# num1, num2 = map(float, input("What are your favorite 2 numbers (seperated by spaces):").split())

happy = True
print(happy)

print(5 > 3)
print(5 < 3)

me = "Jared"
nerd = "Caleb"
print("me == you?", me == nerd)

my_grades = [100, 100, 100]
your_grades = [100, 100, 100]
print("Same grade?", my_grades == your_grades)

print("are grades the same object?", my_grades is your_grades)

my_grades = your_grades
print("are grades the same object", my_grades is your_grades)


print("A before B", "A" != "B")
print(not "A" == "B")

# name = input("What's your name?")
# print("what's your age")
# if name == "Jared":
#     print("Hey, Jared")

# age = 25
# # if age > 100:
# #     print("Wow?")
# # print("You are so old")

# if age > 100:
#     print("WOW!")
#     print("You are so old")

# if age > 100:
#     print("WOW!")
#     print("You are so old")
# else:
#     print("You're so young")

#     if age > 100:
#         print("youre old")
#     elif age > 120:
#         print("How are you alive?")
#     else:
#         print("You may have some years left in you")

jared_is_cool = False
if jared_is_cool:
    print("Let's be friends")
else:
    print("EWW")

thunder = False
lighting = True

if lighting or thunder:
    print("Dont go swimming!")

car_nice = True
on_sale = False

if car_nice and on_sale:
    print("Buy the car!")