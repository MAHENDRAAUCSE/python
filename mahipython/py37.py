ls2 = [30,20,15,45,31,6,6,11]
ls3 = ['mahe','vignesh','mahe','pranay','pranay','venki','lakshmi','vignesh']
def mode(dataset):
    frequency = {}
    for value in dataset:
        frequency[value] = frequency.get(value,0)+1
    most_frequent = max(frequency.values())
    modes = [key for key,value in frequency.items() if value == most_frequent]
    return modes
print(mode(ls2))
print(mode(ls3))
