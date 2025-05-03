def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters_count = {}
    
    for i in text:
        lowercase_text = text.lower()
        if i not in letters_count:
            letters_count[i] = 1
        if i in letters_count:
            letters_count[i] =+ 1
    return letters_count

