def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    sq = 0
    if (x%2) == 0:
        while x > 1:
            x /= 2
            if x > 1:
                sq += 1
        return sq
    else:
        while x > 1:
            x /= 2
            if x > 1:
                sq += 1
        return sq
    
def main():
    print(mySqrt(4))

if __name__ == "__main__":
    main()