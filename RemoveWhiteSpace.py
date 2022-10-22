##Remove white space in string
import re

ip = input("ENTER THE STRING:")

print("ORIGINAL TEXT IS :", ip)
print("NEW TEXT IS :",re.sub(r'\s+','',ip))

