import random
import string

chars = ' ' + string.punctuation +string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()


random.shuffle(keys)
print(f'chars : {chars}')
print(f'keys : {keys}')

# Encrypt
normal_text = input('enter a message to encrypt : ')
cipher_text = ''
for letter in normal_text :
     index = chars.index(letter)
     cipher_text += keys[index]
print(f'original message: {normal_text}')
print(f'encrypted message: {cipher_text}')



#  for Decrypt the messsage  [use one operation at a time ]
cipher_text = input('enter a message to Decrypt : ')
normal_text = ''
for letter in cipher_text :
     index = keys.index(letter)
     normal_text += chars[index]

print(f'encrypted message: {cipher_text}')
print(f'original message : {normal_text}')
