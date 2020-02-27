# Exercise 6. Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y + "\n")

print(f"I said: {x}")
print(f"I said {y}" + "\n")

hillarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hillarious))

w = "one"
e = " two"

print(w + e)