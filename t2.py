def quicksort(array: list) -> list:
    if len(array) > 1:
        num = array[0]
        great = [x for x in array if x > num]
        same = [x for x in array if x == num]
        low = [x for x in array if x < num]
        result = quicksort(great) + same + quicksort(low)
        return result
    return array


def common_divs(data: list) -> list:
    if len(data) <= 0:
        return None
    else:
        array = quicksort(data)
        great = array[0]
        for i in range(1, len(array)):
            divs = []
            num_f = great
            num_s = array[i]
            while num_f != 1:
                mod = num_f % num_s
                if mod == 0:
                    divs.append(num_s)
                num_f = num_s
                num_s = mod
            print(divs)


test = [42, 12, 18]
print(common_divs(test))
