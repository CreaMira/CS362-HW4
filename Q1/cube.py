
def cube(l,w,h):

    if (isinstance(l, str) or isinstance(w, str) or isinstance(h, str)):
        raise ValueError('Side length can not be string.')
    else:
        if (l < 0 or w < 0 or h < 0):
            raise ValueError('Side length can not be negative.')
        else:
            v = l * w * h

    return v