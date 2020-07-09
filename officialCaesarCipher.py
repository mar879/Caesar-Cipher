def encryptReverse(lst):
    x = lst[::-1] # reverses list of numbers from encryptShift function
    y = "".join([chr(c) for c in x]) # converts list of numbers to string of characters
    return "Your encrypted message is: " + "\n" + y # returns your encrypted message
    
def encryptShift(string, firstShift, secShift, direction):
    # converts each letter to ascii value(number) and shifts
    a = [] # variable of empty list created in order to append each ord(letter) easily
    if direction == "+": # if direction is +, shifted to the right
        i = 0
        while i < len(string):
            for char in string:
                if i%2 == 0: # if even index, shifted by firstShift 
                    shifted = ord(char) + firstShift # shifted value
                    if shifted > 126: # if shifted greater than 126 (upper limit), subtracted by 95, and appended to a
                        shifted = shifted - 95
                        a.append(shifted)
                        i += 1
                    else: # other values just appended to a
                        a.append(shifted)
                        i += 1
                else: # if odd index, shifted by secShift 
                    otherShift = ord(char) + secShift # shifted value
                    if otherShift > 126: # if otherShift greater than 126 (upper limit), subtracted by 95, and appended to a
                        otherShift = otherShift - 95
                        a.append(otherShift)
                        i += 1
                    else: # other values just appended to a
                        a.append(otherShift)
                        i += 1 
    else: # if direction is -, shifted to the left 
       i = 0
       while i < len(string):
            for char in string:
                if i%2 == 0: # if even index, shifted by firstShift 
                    shifted = ord(char) - firstShift
                    if shifted < 32: # if shifted less than 32 (lower limit), added to 95, and appended to a
                        shifted = shifted + 95
                        a.append(shifted)
                        i += 1
                    else: # other values just appended to a
                        a.append(shifted)
                        i += 1
                else: # if odd index, shifted by secShift 
                    otherShift = ord(char) - secShift
                    if otherShift < 32: # if otherShift less than 32 (lower limit), added to 95, and appended to a
                        otherShift = otherShift + 95
                        a.append(otherShift)
                        i +=1
                    else: # other values just appended to a
                        a.append(otherShift)
                        i += 1
    return encryptReverse(a) # returns list of numbers (a) to encryptReverse function for reversing and conversion to characters

def encrypt(string, integer, direction):
    # validates whether user input of strin, firstShift, secShift, direction is valid
    string = raw_input("Please type your message: ") # asks user for message
    while True: 
        firstShift = integer
        integer = raw_input("Please input a number between 1 and 95 to be used as a first shift >>> ") #asks for firstShift 
        try:        
            a = int(integer) # converts integer string to actual integer, if fails to, returns error message
            if a < 1 or a > 94: # if firstShift not in range, returns error message
                print "Invalid input. Your input is not in the range." 
            else: #ends loop if firstShift is in range
                break 
        except ValueError: #accepts value error and asks user to write a number for firstShift again
            print "Invalid input. Your input is not an integer." + "\n"
    while True: # firstShift is int and in range, thus proceeds to ask for second shift number
        secShift = integer
        integer = raw_input("Please input a number between 1 and 95 to be used as a second shift >>> ") #asks for secShift
        try: 
            b = int(integer) # converts integer to actual integer
            if b < 1 or b > 94: # if secShift not in range, returns error message
                print "Invalid input. Your input is not in the range." 
            else:
                break #ends loop if secShift is in range
        except ValueError: #accepts value error and asks user to write a number for secShift again
            print "Invalid input. Your input is not an integer." + "\n"
    direction = raw_input("Please input encryption direction. Type + or - >> ") # secShift is int and in range, thus proceeds to ask for direction of shift
    while direction != "+" and direction != "-": # if direction input not + or -, returns error message, asks user for input of direction again
        print "Invalid input." 
        direction = raw_input("Please input encryption direction. Type + or - >> ")
    else: # if direction input is + or -, returns to encryptShift function and prints your decrypted message
        return encryptShift(string, a, b, direction) + "\n" + "Your decrypted message is: " + "\n" + str(string) 


def decryptShift(string, firstShift, secShift, direction):
    # converts each letter to ascii value(number) and shifts
    a = [] # variable of empty list created in order to append each letter easily
    if direction == "+": # if direction is +, shifted to the left
        i = 0
        while i < len(string):
            for char in string:
                if i%2 == 0: # if even index, shifted by firstShift 
                    shifted = ord(char) - firstShift # shifted value
                    if shifted < 32: # if shifted less than 32 (lower limit), added to 95, converted to character and appended to a
                        shifted = shifted + 95
                        a.append(chr(shifted))
                        i += 1
                    else: # other values just converted to character and appended to a
                        a.append(chr(shifted))
                        i += 1
                else: # if odd index, shifted by secShift 
                    otherShift = ord(char) - secShift # shifted value
                    if otherShift < 32: # if otherShift less than 32 (lower limit), added to 95, converted to character and appended to a
                        otherShift = otherShift + 95
                        a.append(chr(otherShift))
                        i +=1
                    else: # other values just converted to character and appended to a
                        a.append(chr(otherShift))
                        i += 1
    else: # if direction is -, shifted to the right
       i = 0
       while i < len(string):
            for char in string:
                if i%2 == 0: # if even, shifted by firstShift 
                    shifted = ord(char) + firstShift # shifted value
                    if shifted > 126: # if shifted greater than 126 (upper limit), subtracted by 95, converted to character and appended to a
                        shifted = shifted - 95
                        a.append(chr(shifted))
                        i += 1
                    else: # other values just converted to character and appended to a
                        a.append(chr(shifted))
                        i += 1
                else: # if odd, shifted by secShift 
                    otherShift = ord(char) + secShift
                    if otherShift > 126: # if otherShift greater than 126 (upper limit), subtracted by 95, converted to character and appended to a
                        otherShift = otherShift - 95
                        a.append(chr(otherShift))
                        i += 1
                    else: # other values just converted to character and appended to a
                        a.append(chr(otherShift))
                        i += 1 
    finalString = ''.join(a) # converts list of characters to string (in order to remove brackets, commas, and spaces)
    return "Your decrypted message is: \n" + finalString # returns user's decrypted message

def decryptReverse(s): # reverses string from decrypt function
    i = len(s) - 1 # last index
    sNew = "" # new empty string variable to add characters of s reversed
    while i >= 0: # while index greater than or equal to 0, last index character added to empty variable, sNew
        sNew = sNew + str(s[i])
        i -= 1 # subtracts 1 from i in order to go backwords through s
    return sNew # returns reversed string to decryptShift

def decrypt(string, integer, direction):
    # validates whether user input of strin, firstShift, secShift, direction is valid
    string = raw_input("Please type your message: ") # asks user for message
    while True: 
        firstShift = integer
        integer = raw_input("Please input a number between 1 and 95 to be used as a first shift >>> ") #asks for firstShift 
        try:        
            a = int(integer) # converts integer string to actual integer, if fails to, returns error message
            if a < 1 or a > 94: # if firstShift not in range, returns error message
                print "Invalid input. Your input is not in the range."
            else: #ends loop if firstShift is in range
                break 
        except ValueError: #accepts value error and asks user to write a number for firstShift again
            print "Invalid input. Your input is not an integer."
    while True: # firstShift is int and in range, thus proceeds to ask for second shift number
        secShift = integer
        integer = raw_input("Please input a number between 1 and 95 to be used as a second shift >>> ") #asks for secShift
        try: 
            b = int(integer) # converts integer to actual integer
            if b < 1 or b > 94: # if secShift not in range, returns error message
                print "Invalid input. Your input is not in the range."
            else:
                break #ends loop if secShift is in range
        except ValueError: #accepts value error and asks user to write a number for secShift again
            print "Invalid input. Your input is not an integer."
    direction = raw_input("Please input encryption direction. Type + or - >> ") # secShift is int and in range, thus proceeds to ask for direction of shift
    while direction != "+" and direction != "-": # if direction input not + or -, returns error message, asks user for input of direction again
        print "Invalid input.",
        direction = raw_input("Please input encryption direction. Type + or - >> ")
    else: # if direction input is + or -, returns to reverse function
        # returns to decryptShift function (replaces its parameter "string" for the reverse of the user input --> string) and then prints the encrypted message
        return decryptShift(str(decryptReverse(string)), a, b, direction) + "\n" + "Your encrypted message is: " + "\n" + str(string) 

def CaesarCipher(x):
    # validates the user input from main
    # a, b, c are actually the parameters string, integer, and direction
    a = ""
    b = ""
    c = ""
    while x != "E" and x != "e" and x != "D" and x != "d":
        # if user input is other than the letters e or d (caps or lowercase)
        # returns error message and user asked question again
        print "Invalid input.",
        x = raw_input("Would you like to encrypt or decrypt your message? Type E or D >> ")
    if x == "E" or x == "e": # if user input is e, returns to encrypt function
        return encrypt(a, b, c)
    else: # if user input is d, returns to decrypt function 
        return decrypt(a, b, c)

def main():
    # asks user for input of e or d and then goes to inputAndValidation function
    x = raw_input("Would you like to encrypt or decrypt your message? Type E or D >>> ")
    print CaesarCipher(x)
main()
