# Part 1 - Encryption
#1 - Create a function called encrypt() that takes original_text and shift amount as 2 inputs.

#2 - Inside the encrypt(), shift each letter of the original_text forwards in the alphabet
# by the shift_amount and print the encrypted text.
    # - loop through each letter using for loop
    # - Using the index() find the index position of each letter

# 3 - Call the encrypt() function and pass user inputs. You should be able to test the code and encrypt a message.
# 4 - What happens if you try to shift z forwards by 9? Can you fix the code?

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
# text = input("Type your Message: \n").lower()
# shift = int(input("Type the shift number: \n"))


def encrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        # shifting the letters if the shift_amount is more than the 25(z)
        shifted_position = shifted_position % len(alphabet) # 0- 25
        cipher_text += alphabet[shifted_position]
        # print(cipher_text)
    print(f"Here is the encoded result : {cipher_text}")
# encrypt(text,shift)

# Part 2 - Decryption
# 1. Create a function called 'decrypt()' that takes original_text and 'shift_text'
# 2. Inside decrypt(), shift each letter of the original_text backwards in the alphabet
# by the shift_amount and print the encrypted text.
# 3. Combine the encrypt() and decrypt() functions into a function called 'caesar' use the value of the user chosen 
# direction variable to determine which function 

def decrypt(original_text,shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        # shifting the letters if the shift_amount is more than the 25(z)
        shifted_position = shifted_position % len(alphabet) # 0- 25
        output_text += alphabet[shifted_position]
        # print(output_text)
    print(f"Here is the encoded result : {output_text}")
# decrypt(original_text=text,shift_amount=shift)


def caesar(original_text,shift_amount, encode_or_decode):
    output_text = ""

    # this decodes the text 
    if encode_or_decode == 'decode':
            shift_amount *= -1
    
    for letter in original_text:
        # this encode the text
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)
        output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result :{output_text}" )

# caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

# Part 3 - Reorganisiong Code
should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt :\n").lower()
    text = input("Type your Message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no' \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
   