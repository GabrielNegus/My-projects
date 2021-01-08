# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:51:42 2021

@author: gabri
"""
print( """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 PP    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP******  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                          88                                 
           88             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(plain_text, shift_amount, direction_input):
    if direction == 'encode':
        result_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift_amount) % 26
                result_text += alphabet[new_position]
            else:
                result_text += char
        print(f"The encoded text is {result_text}\n")
    elif direction == 'decode':
        result_text = ""
        for char in plain_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position - shift_amount +26) % 26
                result_text += alphabet[new_position]
            else:
                result_text += char
        print(f"The decoded text is {result_text}\n")   
            
caesar(plain_text = text, shift_amount=shift, direction_input = direction)

again = True
while again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(plain_text = text, shift_amount=shift, direction_input = direction)
    
    user_choice = input('Would you like to restart the Cipher? yes / no \n').lower()
   
    if user_choice == 'no':
        again = False
        print('Goodbye!')
    
    
       
    

