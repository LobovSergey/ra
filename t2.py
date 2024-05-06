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
        divs = []
        array = quicksort(data)
        less = array[-1]
        if less < 0:
            less -= less * 2
        for i in range(1, less + 1):
            c = 0
            for el in array:
                if el % i != 0:
                    break
                c += 1
            if c == len(array):
                divs.append(i)
        if len(divs) == 0:
            return None
        return divs


test_1 = [42, 12, 18]
print(f"test_1 - {common_divs(test_1)}")
test_2 = [0, 0, 0]
print(f"test_2 - {common_divs(test_2)}")
test_3 = [42, 12, 18, -2]
print(f"test_3 - {common_divs(test_3)}")
test_4 = [42, 12, 18, 13, 13]
print(f"test_4 - {common_divs(test_4)}")
test_5 = []
print(f"test_5 - {common_divs(test_5)}")
test_6 = [42]
print(f"test_6 - {common_divs(test_6)}")
test_7 = [42, 12, 18, 0]
print(f"test_7 - {common_divs(test_7)}")
