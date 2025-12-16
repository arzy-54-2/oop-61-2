my_list = [1,2,3,4,5,6,7,8,9,10]
target = 11
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return  print(mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return print('нету того что мы искали!!')
binary_search(my_list, target)

my_list_2 = [1,2,22,3,4,3215,3124,6,7,8,9,10]

print(my_list_2)
print(sorted(my_list_2))

# from django
# from colorama
