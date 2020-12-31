interrogatives = ['who', 'whom', 'which', 'whose', 'where', 'when', 'why', 'what', 'how', 'have']

def title_str(str_array):                       #titles all strings on the array
    for i in range(0,len(str_array)):
        str_array[i] = str_array[i].title()
    return str_array


def ver_if_question(string):                    #verifies if the current string is a question or not
    for each in interrogatives:
        if string.startswith(each) == True:
            string = string + '?'
            return string
    return f'{string}.'

str_input = ''
str_array = []

while True:
    if(str_input == '\end'):
        break
    else:
        str_input = input('Say something: ')
        str_array.append(ver_if_question(str_input))
        continue

print(title_str(str_array))