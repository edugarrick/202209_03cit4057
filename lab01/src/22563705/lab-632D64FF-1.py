

array_test = [1000, 22, 34, 58, 25, 1, 3, 19, 80]

def sort(arr):
    # START: Correct the mistake  
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    # END: Correct the mistake
 
def main(): 
    print("Original array is:")
    for i in range(len(array_test)):
        print("%d" % array_test[i], end=" ")
    print("\n") 
    sort(array_test)
    print("Sorted array is:")
    for i in range(len(array_test)):
        print("%d" % array_test[i], end=" ")

if __name__ == "__main__":
    main()