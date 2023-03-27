import random
import time

# List of Numbers
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Asking for phrase
phrase = input("Enter The Phrase: ")
number_for_phrase = []

# Choosing random number from list, to the length of the phrase and joining them with no spaces
for i in range(len(phrase)):
    r = random.choice(number_list)
    number_for_phrase.extend(str(r))
    hashed = "".join(number_for_phrase)

print(f"\nYour Hashed Code For '{phrase}' is '{hashed}'")

# Asking if you want to see your msg
see_msg = input("Do you want to see the msg: ")

if see_msg == 'yes':

    decrypt = input("Enter The Hashed Code Given Above: ")

    try:

        if decrypt == hashed:
            print(f"Phrase Matched The Message Is: {phrase}")
        else:
            print("No Match !!!")
    except Exception as e:
        print(f"Error occurred {e}")

    finally:

        time.sleep(1)
        print("\nThanks For Using!")

else:
    print("Your msg has been successfully Encrypted")
