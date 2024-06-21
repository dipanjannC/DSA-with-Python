"""_summary_

Binary Search implementation with recursive and iterative methods. 

"""
def binarySearchIterative(arr,low,high,val):
    
    while low <= high :
        mid = low + (high - low)//2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val :
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binarySearchRecursive(arr,low,high,val):

    if low <= high:

        mid =  low + (high-low)//2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return binarySearchRecursive(arr,low=mid+1,high=high,val=val)
        
        else:
            return binarySearchRecursive(arr,low=low,high=mid-1,val=val)
        


def main():
    arr = [13,15,20,25,31,33,39,40,46,124,142,235,260]
    low = 0
    high = len(arr) - 1 
    val = 235
    result_iterative = binarySearchIterative(arr,low,high,val)
    print(result_iterative)
    result_recursive = binarySearchRecursive(arr,low,high,val)
    print(result_recursive)


main()