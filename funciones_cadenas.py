string = "Example large string"
# Show simple character of the string
print (string[5])
#Show a slice of the string
print (string[5:15])
#Show words of the string separated by spaces
words = string.split()
print(words)
#Show words of the string separated by "l"
words = string.split("l")
print(words)
#Join words of a list into a string with spaces
cadena = " ".join(["String", "with", "spaces"])
print(cadena)
#Length of the string
string = "Hello"
print(len(string))