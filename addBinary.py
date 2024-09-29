def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    int_a, int_b = int(a), int(b)
    num_a, num_b = 0, 0
    
    addpow = 0

    while int_a != 0 or int_b !=0:
        p = 2**addpow        
        # if int_a%10 == 1:
        num_a += p*(int_a%10)
        # if int_b%10 == 1:
        num_b += p*(int_b%10)
        int_a//=10
        int_b//=10
        addpow+=1

    dec = num_a+num_b
    if dec == 0:
        return "0"
    to_bin = ""

    while dec >= 0:
        if dec%2 == 0:
            to_bin = '0' + to_bin
        else:
            to_bin = '1' + to_bin
        dec //= 2
    return to_bin



a = "0"
b = "0"
print(addBinary(a,b))

