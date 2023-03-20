##Q1:
def my_func(x1,x2,x3):
    if type(x1) == str or type(x2) == str or type(x3) == str:
        return None
    else:
        if x1+x2+x3 == 0:
            return "Not a number – denominator equals zero"
        else:
            if type(x1) == float or type(x2) == float or type(x3) == float:
                return float((x2+x3)*x3)
            else:
                return"Error: parameters should be float"
    
    
##Q2:
#switching to lower case:
def revword (word):
    New = word[::-1].lower()
    return New

#finding amount of times
def countword():
    file1 = open('text.txt')
    Lst = []
    for line in file1:
        Lst = Lst + line.rstrip().split()
    word = Lst[0]
    
    LowerLst = []
    notone = 0
    for Lword in Lst:
        if notone != 0:
            LowerLst.append(revword(Lword))
        else:
            LowerLst.append(Lword)
        notone = notone + 1
    Amount = 0
    for each in LowerLst:
        if each == word:
            Amount = Amount + 1
    return Amount

countword()


    
