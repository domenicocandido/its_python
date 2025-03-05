def city_country(city:str, country:str) -> str:
    
    msg = f"{city},{country}"
    return msg

city1 = city_country("Milano", "Italia")
city2 = city_country("Bologna", "Italia")
city3 = city_country("Madrid", "Spagna")

print(f"{city1}\n{city2}\n{city3}")


