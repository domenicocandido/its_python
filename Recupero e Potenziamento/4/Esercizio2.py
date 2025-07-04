def printListBackward(l:list) -> None:

    if not l:
        pass
    else:
        print (l[-1])
        printListBackward(l[:-1]) # :-1 torna la lista eccetto l'ulimo elemento


printListBackward([1,2,3,4,5])