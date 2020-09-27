if __name__ == "__main__": 

    # Insertion Sort Algorithms 

    A = [5, 4, 2, 6, 3, 1]
    print("original Array A: ", A)

    for j in range(0, len(A)): 
        key = A[j]
        i = j-1

        while i >= 0 and A[i] > key: 
            A[i + 1] = A[i]
            i = i-1 
        
        A[i+1] = key


    print("Sorted Array A: ", A)