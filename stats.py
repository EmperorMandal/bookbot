
def get_num_words(text):
    words = text.split()
    word_count = len(words)
    return word_count

def count_carecters(text):
    text_lowercase = text.lower()

    dictionary = {
            'a' : 0,
            'b' : 0,
            'c' : 0,
            'd' : 0,
            'e' : 0,
            'f' : 0,
            'g' : 0,
            'h' : 0,
            'i' : 0,
            'j' : 0,
            'k' : 0,
            'l' : 0,
            'm' : 0,
            'n' : 0,
            'o' : 0,
            'p' : 0,
            'q' : 0,
            'r' : 0,
            's' : 0,
            't' : 0,
            'u' : 0,
            'v' : 0,
            'w' : 0,
            'x' : 0,
            'y' : 0,
            'z' : 0,
        }

    for x in text_lowercase:
        if x in dictionary:
            dictionary[x] = dictionary[x] + 1
    return dictionary

def sorting(dictio):
    sorted_dic = []

    for i, x in dictio.items():
        dic = {"char": i, "num": x}
        sorted_dic.append(dic)

    def sort_on(item):
        return item["num"]

    sorted_dic.sort(reverse=True, key=sort_on)

    return sorted_dic
