def rimbalzo() -> None:
    
    tempo: int = 0
    altezza: float = 0.0
    velocita: float = 100.0
    rimbalzi: int = 0
    

    while rimbalzi <= 5:
        
        altezza += velocita
        velocita -= 96

        if altezza < 0:
            altezza *=  -0.5
            velocita *= -0.5
            rimbalzi += 1
            
            print (f"Tempo: {tempo} Rimbalzo!")
        
        else:
            
            print (f"Tempo: {tempo} Altezza: {altezza}")
        
        tempo += 1

rimbalzo()