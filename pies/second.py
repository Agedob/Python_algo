
word_list = ['hello','world','my','name','is','Anna']
the_key = "o"
word_list_2 = ['Excepteur', 'ut', 'aliqua', 'tempor', 'officia', 'nisi', 'officia', 'dolore', 'ex pariatur']
def Second(array_str, array_key):
    re = ""
    for i in range(0, len(array_str)):

        for j in range(0, len(array_str[i])):

            if array_key == array_str[i][j]:
                re += array_str[i] + " "
                break
        
        
    
    return re


print(Second(word_list_2,"a"))

