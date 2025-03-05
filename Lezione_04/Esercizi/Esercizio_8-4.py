def make_shirt(size:str =  "L", text:str = "I Love Python."):
    msg = f"La maglia è una {size} e contiene {text}." 
    return msg

maglia1 = make_shirt()
maglia2 = make_shirt(size = "M")
maglia3 = make_shirt("S", "Milano")
print(maglia1)
print(maglia2)
print(maglia3)