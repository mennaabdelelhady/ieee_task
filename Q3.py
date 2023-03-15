def find_second_largest(arr):
    # sort the array in descending order
    arr.sort(reverse=True)
    
    # return the second largest element
    return arr[1]
    
# example 
my_arr = [1, 2, 3, 5, 4, 7, 6]
second_largest = find_second_largest(my_arr)
print(second_largest)  # output: 2
