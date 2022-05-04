    
lists = [
[1,2,5,6,2],
[1,2,5,6,2],

[1,2,5,6,3],
[1,2,5,6,2],

[1,2,5,6,5],
[1,2,5,6,5,3],

[1,2,5,6,5,16],
[1,2,5,6,5],

['celery','carrots','bread','milk'],
['celery','carrots','bread','cream']
]

def forloops ():
    
    for i in range(0, len(lists), 1):
        print('working on lists', lists[i], 'and ', lists[i+1])
        if len(lists[i]) != len(lists[i+1]):
            print("lists are not the same length")
            i += 1
            break
        for j in range(0, len(lists[i]), 1):
            # print(lists[i][j])
            if lists[i][j] != lists[i + 1][j]: 
                print('Char ' , lists[i][j] , ' does not match ' , lists[i+1][j])
                break
            elif lists[i][j] != lists[i + 1][j]:
                print(lists[i][j], lists[i + 1][j], 'Does not match')
                break
           


forloops()