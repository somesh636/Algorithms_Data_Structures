"""
ECE606, F'20, Assignment 1, Problem 6
Skeleton solution file.
"""

"""
You are not allowed to import anything
"""

def base9_converter(number): 

    """ base9_converter(number): Convert Decimal Number to Base 9

    Parameter:
    -----------
    number: int 
    number to be converted to Base 9 form 

    Return: 
    --------
    base9_merged_int: return a number in Base 9 format 
    """

    quotient = 0 
    r_list = []

    while (number >= 9): 
        quotient = number // 9 
        remainder = number % 9
        r_list.append(remainder)
        number = quotient


    r_list.append(number)
    r_list.reverse()
    base9_str = [str(i) for i in r_list]
    b9_merged_int = int(''.join(base9_str)) 

    return b9_merged_int

def base9_base10(number):
    """ base9_base10(number): Convert Base 9 to Base 10

    Parameter:
    -----------
    number: int
    number to be converted to Base 9 form 

    Return: 
    --------
    base9_merged_int: return a number in Base 9 format 
    """

    int_list = [int(value) for value in str(number)]
    base10_num = 0
    int_list.reverse()

    for val in range(len(int_list)): 
        base10_num += (int_list[val] * (9 ** val)) 

    return base10_num

def gcd(x, y): 
    """ gcd(x, y): Convert Base 9 to Base 10

    Parameter:
    -----------
    x: int
    number for which GCD is required 

    y: int
    number for which GCD is required 

    Return: 
    --------
    gcd: GCD for x and y  
    """

    if (x>y): 
        small_num = y
    else: 
        small_num = x 

    for value in range(1, small_num+1): 
        if ((x % value == 0) and (y % value == 0)):
            gcd = value  

    return gcd 


def sformbnine(r):
    """
    You need to implement this method.
    You are certainly allowed to define any subroutines you want
    above this method in this file.
    """

    # Convert Base 9 to Base 10 
    r_new = []
    base10_num1 = base9_base10(r[0])
    base10_num2 = base9_base10(r[1])

    # Convert Simplest Form to Base 9 
    gcd_num = gcd(base10_num1, base10_num2)

    if (gcd == 1): 
        return r
        
    else: 

        num_1 = base10_num1 / gcd_num 
        num_2 = base10_num2 / gcd_num
        num1_10_9 = base9_converter(int(num_1))
        num2_10_9 = base9_converter(int(num_2))

        r_new.append(num1_10_9)
        r_new.append(num2_10_9)
        return r_new
        
if __name__ == "__main__": 
    
    r1 = [14, 35]
    r2 = [11, 27]

    num1 = sformbnine(r1)
    num2 = sformbnine(r2)
    # print("r1: {0}".format(num1))
    # print("r2: {0}".format(num2))