# strings
string = " Hello my my name is ema "
print(string.upper())
print(string.capitalize()) # first character only
print(string.title()) # first letter of each word
print(string.replace(" ", "\n"))
print(string.strip())
print(string.count("my"))

# extract all email addresses from a string
import re
string = "Contact us at help@example.com or support@xyz.co"
print(re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", string))

# Find all numbers (integers and decimals) in text
string = "Price: 25, Tax: 1.5"
print(re.findall(r'[0-9]\.?[0-9]*',string))
