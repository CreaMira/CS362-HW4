
def avg(num_list):

    if (len(num_list) == 0):
        raise ValueError('The list is Empty!')
    else:
        avg = sum(num_list) / len(num_list)

    return round(avg,2)