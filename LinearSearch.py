
#Linear Search Algorithm
def linearSearch(list,query):
    for i in range(0,len(list)):
        if list[i] == query:
            return i
    return -1

#driver code
if __name__ == '__main__':
    list = [2,3,5,6,7,8,9]
    query = 81
    print(linearSearch(list,query))