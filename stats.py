def get_num_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letters_count= {}
    lowercase_text = text.lower()
    for i in lowercase_text:
        if i.isalpha():
            if i in letters_count:
                letters_count[i] += 1
            else:
                letters_count[i] = 1
    return letters_count

def sort_alpha(let_dict):
    char_list = []
    for char, num in let_dict.items():
        char_info = {"char": char, "num": num}
        char_list.append(char_info)
    char_list.sort(reverse=True,key=lambda char_list: char_list["num"])
    return char_list

