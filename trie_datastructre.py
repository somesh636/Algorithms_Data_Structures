"""
ECE606, F'20, Assignment 2, Problem 3
Skeleton solution file
"""

"""
You are not allowed to import anything
"""

def SearchInTrie(T, s):
    if len(s) == 0:
        # weird, should not happen
        return False

    if len(s) > 0 and len(T) == 0:
        return False

    if len(s) == 1:
        return T[ord(s[0]) - ord('a')][1]

    return SearchInTrie(T[ord(s[0]) - ord('a')][0], s[1:])


def InsertIntoTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    if len(s) == 0:
        return

    if len(T) == 0: 
        # Initialize the Tree
        T.extend([[[], False] for _ in range(26)])

    position = ord(s[0]) - ord('a')

    if len(s) == 1:
        T[position][1] = True
    else:
        InsertIntoTrie(T[position][0], s[1:])

def istriempty(T): 

    if len(T)== 0:
        return True
    
    for value in T: 
        if value[1] == True: 
            return False   
        
        elif value[1] == False and len(value[0]) != 0: 
            return False 

    for index in T: 
        if index[1] == False and len(index[0]) == 0: 
            return True 


def DeleteFromTrie(T, s):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """
    if len(s) >0: 
        position = ord(s[0]) - ord('a')

    if len(s) > 1: 
        DeleteFromTrie(T[position][0], s[1:])


    elif len(s) == 1:
        T[position][1] = False

    if istriempty(T):
        T.clear()

    return
    

if __name__ == "__main__": 

    T = []
    s1 = "ca"
    s2 = "cat"


    InsertIntoTrie(T, s1)
    # InsertIntoTrie(T, s2)

    print("Before T: ", T)
    # value1 = SearchInTrie(T, s1)
    # value2 = SearchInTrie(T, s2)

    # print(" Value1(True): ", value1)
    # print(" Value2(True): ", value2)


    DeleteFromTrie(T, s1)
    # value3 = SearchInTrie(T, s1)
    # print(" Value3(False): ", value3)

    # value4 = SearchInTrie(T, s2)
    # print(" Value4(True): ", value4)

    # DeleteFromTrie(T, s2)
    # value5 = SearchInTrie(T, s2)
    # print(" Value5(False): ", value5)    

    print("\n\n T: ", T)