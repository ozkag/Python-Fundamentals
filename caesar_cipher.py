

def caesar_cipher(string, offset):
    chars_list = list(string)
    ordinals_list = []
    new_word_chars_list = []
    new_word = ""

    for char in chars_list:
        ordinals_list.append(ord(char))

    for i in range(len(ordinals_list)):
        if ordinals_list[i] - offset >= 97:

            ordinals_list[i] = ordinals_list[i] - offset
            new_word_chars_list.append(chr(ordinals_list[i]))

        else:
            ordinals_list[i] = 25 - offset + ordinals_list[i] + 1
            new_word_chars_list.append(chr(ordinals_list[i]))

    for char in new_word_chars_list:
        new_word += char

    return new_word






    

    



    













