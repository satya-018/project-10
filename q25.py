# Write a Python program that accepts a username, converts it to uppercase,
# and replaces every "A" with "@".
# Display the modified username, its length, first and last character, count of "@", and 
# validate whether the username length is at most 10 characters.

username = input("enter username here: ")
uppercase_username = username.upper()
replace_username = uppercase_username.replace("A","@")
frist_character = replace_username[0]
last_character = replace_username[-1]
print(uppercase_username.replace(" ","_"))
print("modified username:",replace_username)
print("length of sentence:",len(replace_username))
print("frist character:",frist_character)
print("last character:",last_character)
print(replace_username.count("@"))
if len(replace_username) <= 10:
    print("Valid username")
else:
    print("Username is too long")
