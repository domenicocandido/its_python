def make_shirt(size:str,text:str):
    msg = f"La maglia è una {size} e contiene {text}." 
    return msg

maglia1 = make_shirt("L", "Naples")
maglia2 = make_shirt(size = "M", text = "Rome")

print(maglia1)
print(maglia2)