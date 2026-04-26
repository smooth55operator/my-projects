def func (word_list):
    longest_word = word_list[0]
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
words = ['barcelona', 'tony_stark','messi','thomas_shelby'] 
longest = func(words)
print(f'Longest word: {longest}')
