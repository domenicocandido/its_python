import time

def cronometro(fun):

    def wrapped(*args):

        start = time.time()
        fun(*args)
        print(time.time() - start)
    
    return wrapped

@cronometro

def prova():
    print("Ciao, come stai?")

prova()