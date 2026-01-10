def binary_search(arr, target, left = 0, right = None) -> tuple[int | None, int]:
    steps = 0

    if arr is None or len(arr) == 0: return None, steps
    
    if right is None:
        right = len(arr) -1
    
    if target < arr[left] or target > arr[right]: return None, steps

    while left < right:
        mid = int((left + right) // 2)
        if target == arr[mid]:
            return mid, steps
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid

        steps += 1

    return None, steps

def exponential_search(arr, target, inverted = False) -> tuple[int | None, int]:
    steps = 0

    if arr is None or len(arr) == 0: return None, steps
    if target < arr[0] or target > arr[-1]: return None, steps

    if not inverted:
        if arr[0] == target:
            return 0, steps

        lenght = len(arr)
        i = 1
        prev_i = i

        while i < lenght and arr[i] < target:
            prev_i = i
            i *= 2
            steps += 1

        i = min(i, lenght-1)
        if arr[i] == target:
            return i, steps

        result = binary_search(arr, target, prev_i, i)
        steps += result[1]
        return result[0], steps

    elif inverted:
        arr_end = len(arr) - 1
        i = arr_end
        prev_i = i
        factor = 1

        if arr[i] == target:
            return i, steps

        while i > 0 and arr[i] > target:
            prev_i = i
            factor *= 2
            i = arr_end - factor
            steps += 1

        i = max(i, 0)

        if arr[i] == target:
            return i, steps
        else:
            l = i
            r = prev_i

            result = binary_search(arr, target, l, r)
            steps += result[1]
            return result[0], steps




nums = [4, 8, 20, 22, 31, 58, 63, 66, 73, 74, 78, 97, 99, 106, 119, 124, 134, 170, 184, 191, 200, 203, 217, 223, 225, 226, 246, 288, 294, 299, 300, 303, 309, 312, 324, 335, 336, 360, 366, 373, 385, 390, 391, 424, 426, 428, 433, 437, 443, 461, 541, 576, 579, 583, 601, 603, 604, 607, 608, 609, 630, 636, 637, 640, 668, 669, 675, 685, 687, 692, 701, 718, 720, 721, 761, 765, 767, 826, 829, 832, 842, 843, 849, 856, 860, 861, 863, 879, 891, 899, 904, 910, 941, 953, 957, 961, 963, 970, 974, 993]
#nums = [1,2,3,4,5]
target = 994

exponential_result = exponential_search(nums, target, True)
binary_result = binary_search(nums, target)

steps = exponential_result[1]
exp_idx = exponential_result[0]
if exp_idx != None:
    print("EXPONENTIAL_S| steps:",steps, "index:",exp_idx, "number:",nums[exp_idx])
else:
    print("EXPONENTIAL_S| Not found target number in nums. Steps: ",steps)

steps = binary_result[1]
binary_idx = binary_result[0]
if binary_idx != None:
    print("BINARY_S| steps:",steps, "index:",binary_idx, "number:", nums[binary_idx])
else:
    print("BINARY_S| Not found target number in nums. Steps: ",steps)