def check_permutation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    
    sorted_1 = sorted(string_1)
    sorted_2 = sorted(string_2) 


    for i in range(len(sorted_1)):
        if sorted_1[i] != sorted_2[i]:
            return False
        
    return True

def check_permutation2(string1, string2):
    if len(string1) != len(string2):
        return False
    
    characters = [0] * 128

    for c in string1:
        characters[ord(c)] += 1
        
    for c in string2:
        characters[ord(c)] -= 1

    for i in characters:
        if i > 0:
            return False
        
    return True


def check_permutation3(s, t):
    if len(s) != len(t):
        return False
      
    dictS, dictT = {}, {}

    for i in range(len(s)):
        dictS[s[i]] = 1 + dictS.get(s[i], 0)
        dictT[t[i]] = 1 + dictT.get(t[i], 0)

    return dictS == dictT



print(check_permutation3('abb', 'bba'))

    

# print(check_permutation('abb', 'bba'))
# print(check_permutation('chch', 'hhhh'))
# print(check_permutation('aaaaa', 'aaaaa'))
# print(check_permutation('racecar', 'carrace'))


