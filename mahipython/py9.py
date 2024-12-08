def binary_search(V,To_Find):
    lo=0
    hi=len(V)-1
    while hi-lo>1:
        mid=(hi+lo)//2
        if V[mid]<To_Find:
            lo=mid+1
        else:
            hi=mid
    if V[lo]==To_Find:
        print("Found at the index",lo)
    elif V[hi]==To_Find:
        print("Found at index",hi)
    else:
        print("not found")


if __name__=='__main__':
    V=[10,30,40,50,60]
    To_Find=1
    binary_search(V,To_Find)
    To_Find=6
    binary_search(V,To_Find)
    To_Find=10
    binary_search(V,To_Find)
