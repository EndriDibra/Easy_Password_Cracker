# Author: Endri Dibra

# Taking input
password = input("Please enter your password :")

# data is : a set of all possible characters
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'," ", 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','#', '$', '!', '&', '%', '(', ')', '*', '@', '^']

# counter will increase by one, every time that the characters of data are equal to the characters of password
counter = 0

print("You have entered these letters below :")

# The while loop will continue to work until the value(int) of counter is equal to the number of characters of password
while counter != len(password):

    # Checking - searching every character of password in data
    for i in password:
        for k in data:
            if i == k:
                counter += 1
                print(i)

    # In case that their lengths are the same, means that the password is cracked - found
    if counter == len(password):
        print("The password is cracked")

    # Else password is being requested, which means that the characters of password didn't match with the lista's
    else:
        password = input("ERROR! ReENTER YOUR PASSWORD :")