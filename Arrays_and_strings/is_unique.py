#Is Unique

def is_unique(word):
    characters = set()

    for char in word:
        if char in characters:
            return False
        else:
            characters.add(char)
    
    return True


#print(is_unique('yes'))

def is_unique_2(word):
    word = word.lower()
    if len(word) > 128:
        return False
    
    characters = [False] * 128

    for char in word:
        val = ord(char)
        if characters[val]:
            return False
        else:
            characters[val] = True
    
    return True

print(is_unique_2('ChrIstina'))