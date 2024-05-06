from typing import Optional


def simple_num(ls: int, gt: int) -> list[Optional[int]]:
    if ls > gt:
        ls, gt = gt, ls
    simple_list = []
    for num in range(ls, gt + 1):
        i = 1
        half = num / 2
        counter = 0
        if num == 1:
            simple_list.append(num)
        else:
            while i <= half and counter < 2:
                if num % i == 0:
                    counter += 1
                i += 1
            if counter == 1:
                simple_list.append(num)
    return simple_list


test_1 = (12, 27)
print(f"test_1 - {simple_num(*test_1)}")
test_2 = (0, 0)
print(f"test_2 - {simple_num(*test_2)}")
test_3 = (-3, 3)
print(f"test_3 - {simple_num(*test_3)}")
test_4 = (1, 2)
print(f"test_4 - {simple_num(*test_4)}")
test_5 = (27, 12)
print(f"test_5 - {simple_num(*test_5)}")
