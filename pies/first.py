    
lists = [
[1,2,3,4,5],
[1,2,3,4,5],

[2,1,2,5,6,3],
[2,1,2,5,6,2],

[3,1,2,5,6,5],
[3,1,2,5,6,5,3],

[4,1,2,5,6,5,16],
[4,1,2,5,6,5],

[5,'celery','carrots','bread','milk'],
[5,'celery','carrots','bread','cream'],

[6,1,2,3,4,5],
[6,1,2,3,4,5],

]

def forloops ():

    for i in range(0, len(lists), 2):
        if (i + 1 ) >= len(lists):
            print("end of the lists")
            return 
        
        elif len(lists[i]) != len(lists[i + 1]):
            print("not same length", lists[i + 1], " as ", lists[i])
            i = i + 1

        else:
            print("comparing lists ", lists[i], " and ", lists[i+1])

            for j in range(0, len(lists[i])):

                if lists[i][j] != lists[i+1][j]:
                    print("lists are not the same.")
                    i = i + 1
                    break
                
            else:
                print("They are the same!")



        # if (len(lists[i])) != (len(lists[i+1])):
        #     print("lists are not the same length", lists[i], ' and ', lists[i+1])
        #     # i += 1
        # else:
        #     print('working on lists', lists[i], 'and ', lists[i+1])

        # for j in range(0, len(lists[i]), 1):
        #     # print(lists[i + 1][j])
        #     # print(lists[i][j])
        #     # print(lists[i+1][j])
        #     if lists[i][j] != lists[i + 1][j]:
        #         # i += 1
        #         print('Char ' , lists[i][j] , ' does not match ' , lists[i+1][j])
        #         break
            

forloops()