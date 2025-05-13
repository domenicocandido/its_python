PATH: str = "Lezione_15/example.txt"
mode: str = "w"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)

output: str = file.write("Ciaooo")
print(output)
file.close()


