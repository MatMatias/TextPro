interrogatives = ['who', 'whom', 'which', 'whose', 'where', 'when', 'why', 'what', 'how', 'have']

def capitalize_str(str_array):                       #capitalizes all strings on the array
    for i in range(0, len(str_array)):
        str_array[i] = str_array[i].capitalize()
    return str_array


def ver_if_question(string):                    #verifies if the current string is a question or not
    for each in interrogatives:
        if string.startswith(each) == True:
            string = string + '?'
            return string

    return f'{string}.'

def format_str_array(str_array):
    return "\n".join(str_array)

str_input = ''
str_array = []

while True:
    str_input = input('Say something: ')
    if(str_input == '\end'):
        break
    else:
        str_array.append(ver_if_question(str_input))
        continue

print(format_str_array(capitalize_str(str_array)))