def nameGenerate(fName, lName):

    if (isinstance(fName, str) == 0  or isinstance(lName, str) == 0):
        raise ValueError('Name should be a string.')
    else:
        if (len(fName) == 1):
            fullName = lName + ", " + fName + "."
        else:
            fullName = fName + " " + lName

    return fullName