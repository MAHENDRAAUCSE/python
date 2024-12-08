ls2 = [18,21,38,20,39,31,22,23]
ls3 = [18,21,38,20,39,39,31,22,23]
def median(dataset):
    data = sorted(dataset)
    index = len(data)//2
    if len (dataset)%2!=0
        return data[index]
    return(data[index-1]+data[index])/2
print(median(ls2))
print(median(ls3))
