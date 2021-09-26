#new python feature 3.6 onwards
#f-string----------------------------------------------------------
name = "Bob"
greeting = "Hello, Bob"

print(greeting)

name = "Rolf"

print(greeting)

# above statement does not calculate name dynamically, changing name does not change greetings
# to achieve that we need to use f-string, it allows uas to embed the variables inside of strings

greeting = f"Hello, {name}" 

print(greeting)

name = "Bob" 

#again same problem here, it will not change the value dynamically it will print the Hello, Rolf
#one good thing about f-string is instead variable we can directly use the data

print(f"Hello, {name}")

#TEMPLATE STRING----------------------------------------------------------
name = "Chakrapani U"
greeting = "Hello, {}"

#Here we are using the format function, whats that doing it is giving the name to this 
#template and what template will do is it willreplace the curly braces by "name" variable
with_name = greeting.format(name)
print(with_name)

#benifit of this is we can reuse template to send any values or variable 
# another benifit of template string is for longer phrase

longer_phrase = "Hello, {}. Welcome to {} Learning."

with_name_longer_phrase = longer_phrase.format("Chakrapani U","Python")

print(with_name_longer_phrase)
