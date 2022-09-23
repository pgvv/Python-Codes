# get sentence from user
original = input("Please enter a sentence: ").strip().lower()

# split sentence into words
words =original.split()


# covert words to pig latin
words_new = []

# if word starts with a vowel, add "yay"
for w_o in words:
    if w_o[0] in "aeiou":
        new_word = w_o + "yay"
        words_new.append(new_word)
    else:
        
        # if word starts with a consonant,  move the first consonant cluster to the end & add "ay"
        vowel_position = 0
        for letter in w_o:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else:
                break
        cons = w_o[:vowel_position]
        rest = w_o[vowel_position:]

        # combine words to form a sentence
        new_word = rest + cons + "ay"
        words_new.append(new_word)

# output the final string
new = " ".join(words_new).capitalize()
print(new)
