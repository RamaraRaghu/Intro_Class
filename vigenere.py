#Rakshith Raghu(rr5de)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def letter_to_index(letter):
    letter = letter.lower()
    for i in range(25):
        if(letter == alphabet[i]):
            index_value = i
            break
        else:
            index_value = -1
    return index_value

def index_to_letter(index_value):
    if(index_value >= 0 and index_value <= 25):
        letter = alphabet[index_value]
    else:
        letter = '?'
    return letter

def vigenere_encrypt(plain_letter, key_letter):
    plain_letter = str(plain_letter)
    key_letter = str(key_letter)
    if(plain_letter in alphabet and key_letter in alphabet):
        index = letter_to_index(plain_letter)
        index1 = letter_to_index(key_letter)
        if(index+index1 > 25):
            index2 = index + index1 - 26
        else:
            index2 = index + index1
        final_letter = index_to_letter(index2)
        return final_letter
    else:
        final_letter = plain_letter
        return final_letter

def vigenere_decrypt(cipher, key):
    if(cipher in alphabet and key in alphabet):
        index = letter_to_index(cipher)
        index1 = letter_to_index(key)
        if(index - index1 < 0):
            index= index - index1 + 26
        else:
            index = index - index1
        final_letter = index_to_letter(index)
        return final_letter
    else:
        final_letter = cipher
        return final_letter

def encrypt(plain, key):
    encrypted = ''
    plain = plain.lower()
    key = key.lower()

    while(len(plain)> len(key)):
        key = key + key
    for i in range(len(plain)):
        value = vigenere_encrypt(plain[i],key[i])
        encrypted = encrypted + value
    return encrypted

def decrypt(cipher, key):
    plainer = ''
    cipher = cipher.lower()
    key = key.lower()

    while(len(cipher)> len(key)):
        key = key + key
    for i in range(len(cipher)):
        value = vigenere_decrypt(cipher[i], key[i])
        plainer = plainer + value
    return plainer