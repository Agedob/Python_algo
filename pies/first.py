    
lists = [
[1,2,5,6,2],
[1,2,5,6,2],

[1,2,5,6,5],
[1,2,5,6,5,3],

[1,2,5,6,5,16],
[1,2,5,6,5],

['celery','carrots','bread','milk'],
['celery','carrots','bread','cream']
]

def compare (l1, l2):
    print(l1,l2)

# compare(lists[0],lists[1])


def forloops ():
    for i in range(0, len(lists), 1):
        # print(lists[x])
        
        for j in range(0, len(lists[i]), 1):
            print(lists[i][j])

forloops()