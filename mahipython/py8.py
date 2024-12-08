def search(arr,N,x):

    for i in range(0,N):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr=[10,20,30,40,50]
    x=10
    N=len(arr)
    result=search(arr,N,x)
    if result ==-1:
        print("element is not present")
    else:
        print("element is present at index",result)
