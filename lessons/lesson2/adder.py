__version__ = "1.0.0"

def add(alist) :
    if alist is None or len(alist)==0:
        return 0

    print("adding", alist)

    sum = 0
    for i in range(len(alist)) :
        if type(alist[i]) == str :
            try :
                x = float(alist[i])
            except Exception as e:
                print("cannot convert", alist[i], e)
                continue 

        elif type(alist[i]) == float or type(alist[i]) == int :
            x = alist[i]
        else :
            print("cannot convert ", type(alist[i]))
            continue
        sum = sum + x

    return sum
