# the file is opened with the open function being on the same hierarchy level
password = open('pass.txt')

# Next, the file is read through with the read function
read_code = password.read()
print("Enter your password:")
password_entered = input()

# The conditional statements very the validity of the passcode you entered
if password_entered == read_code:
    print("Access granted")
#Spicing things up a bit when a intruder tries to hack using 12345 as a passcode
elif password_entered == "12345":
    print("That's too cheap a password")
else:
    print("Access Denied. Try again")
