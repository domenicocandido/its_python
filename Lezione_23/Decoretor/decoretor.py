import time

def cronometro(fun):

    def wrapper(args):

        start = time.time()
        fun(args)
        print(time.time() - start)
    
    return wrapper

# scrivendo qui @cronometro successivamente non dovrò scrivere prova = cronometro(prova)
def prova():
    print("Ciao")

def prova2():
    print("Hello")

prova = cronometro(prova)  # questo può essere sostituito con @cronometero su def prova() 
prova2 = cronometro(prova2)

prova()
prova2()