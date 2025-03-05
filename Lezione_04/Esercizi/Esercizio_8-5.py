def describe_city(city:str, country:str = "Italia"):
    
    msg = f"{city} è in {country}"
    return msg

city1 = describe_city("Roma")
city2 = describe_city("Napoli")
city3 = describe_city("Parigi", "Francia")

print(f"{city1}\n{city2}\n{city3}")