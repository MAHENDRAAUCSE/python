def partition(array,low,high):
    pivot=array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high])=(array[high],array[i+1])
    return i+1
def quick_sort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
if __name__=='__main__':
    array=[10,17,18,90,11,50]
    quick_sort(array,0,len(array)-1)
    print(f'sorted array:{array}')
