def find_disappeared_numbers(nums: list[int]) -> list[int]:
    n = len(nums)
    total = [x for x in range(1, n+1)]
    for i in nums:
        if i in total:
            total.remove(i)
        else:
            continue
    return total
        

print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
