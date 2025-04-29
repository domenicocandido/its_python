def seconds_since_noon(hours:int, minutes:int, seconds:int) -> int:

    hours_seconds = (hours % 12) * 3600
    minutes_seconds = minutes * 60
    total_hours= hours_seconds + minutes_seconds + seconds

    if hours == 12:
        total_hours += 12 * 3600

    return total_hours
        
    
    

print(seconds_since_noon(3, 15, 30))
print(seconds_since_noon(1, 0, 0))


def time_difference(hours1:int, minutes1:int, seconds1:int, hours2:int, minutes2:int, seconds2:int) -> int:

    time1 = seconds_since_noon(hours1, minutes1, seconds1)
    time2 = seconds_since_noon(hours2, minutes2, seconds2)

    if time2 >= time1:
        return time2 - time1
    
    else:
        return time1 - time2

print(time_difference(1, 0, 0, 3, 15, 30))
print(time_difference(0, 0, 0, 12, 0, 0))

