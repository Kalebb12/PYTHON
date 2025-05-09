programing_dictionary = {
    "bug": "An error in a program that prevents the program from running as expected.",
    "function": "A piece of code that you can easily call over and over again.",
}

# print(programing_dictionary["bug"])
print(programing_dictionary["function"])

programing_dictionary["loop"] = "A programming construct that repeats a group of statements."
programing_dictionary["bug"] = "A mistake in a program that causes it to behave unexpectedly."
print(programing_dictionary["loop"])


for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])