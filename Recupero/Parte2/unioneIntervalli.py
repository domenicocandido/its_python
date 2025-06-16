def merge_intervals(intervals:list[list]) -> list[list[int]]:

    result:list[list[int]] = []

    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])

    for interval in intervals:
            
        start = interval[0]
        end = interval[1]

        if not result:
           
           result.append([start, end])
        
        else:    
            
            old_start, old_end = result[-1]


            if start <= old_end:
                result[-1][1] = max(old_end, end)
            else:
                result.append([start, end])

    return result

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]] 
print(merge_intervals(intervals))

intervals = [[1, 4], [4, 5]] 
print(merge_intervals(intervals))