#This program illustrates the algorithm behind binary search
#This algorithm takes advantage of a sorted array by narrowing down the search on upper or lower limits in just one comparison


def binarysearch(arr, low, high, x):

        if high >= low:
            #get median value by using floor division //
            mid = (low + high) // 2
            #print(f"Low is {low} , High is {high} Mid values is {mid}")
            #check if x is equal to median value
            if arr[mid] == x:
                return mid
            #check median value is greater than x this means tha value is in the left side of the array
            elif arr[mid] > x:
                return binarysearch(arr, low, mid-1, x)
            #else if the the median value is less than x the values is in the right side of the array
            else:
                return binarysearch(arr, mid+1, high, x)
        else:
            return -1


arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
#print(len(arr))
x = int(input("Please input a value:" ))
result = binarysearch(arr, 0, len(arr)-1, x)

if result == -1:
    print(f"The values {x} is not in the array!")
else:
    print(f"The number is in the index {str(result)}")