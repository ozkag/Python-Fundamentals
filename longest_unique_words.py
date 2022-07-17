def get_n_longest_unique_words(words, n):
    
    unique_word_list = []
    wanted_unique_word_list = []

    for word in words:
        if words.count(word) == 1:
            unique_word_list.append(word)

    for i in range(len(unique_word_list) - 1):
        if len(unique_word_list[i]) < len(unique_word_list[i + 1]):
            var = unique_word_list[i + 1]
            unique_word_list[i + 1] = unique_word_list[i]
            unique_word_list[i] = var
    
    for i in range(n):
        wanted_unique_word_list.append(unique_word_list[i])
    

    return(wanted_unique_word_list)


        


    
    
    
    
    
    
    
    
    
    
    
    
    