def urlify(string, length):
    string = list(string)

    index = len(string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            string[index - 3:index] = '%20'
            index -= 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return string

print(urlify("Mr John Smith    ", 13))

