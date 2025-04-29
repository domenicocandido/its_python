import math

def memorizza_file(files: list[int]) -> None:
    spazio_totale_blocchi = 1000  # numero di blocchi disponibili inizialmente
    dimensione_blocco = 512  # dimensione di un singolo blocco in byte

    for file_size in files:
        # Calcolare la dimensione compressa (80% della dimensione originale)
        file_size_compressed = file_size * 0.8
        
        # Calcolare il numero di blocchi necessari per memorizzare il file compresso
        num_blocchi = math.ceil(file_size_compressed / dimensione_blocco)
        
        # Verificare se ci sono abbastanza blocchi disponibili
        if num_blocchi <= spazio_totale_blocchi:
            # Memorizzare il file, aggiornare lo spazio disponibile
            spazio_totale_blocchi -= num_blocchi
            print(f"File di {file_size} byte compresso in {file_size_compressed} byte e memorizzato. "
                  f"Blocchi usati: {num_blocchi}. Blocchi rimanenti: {spazio_totale_blocchi}.")
        else:
            # Non è possibile memorizzare il file
            print(f"Non è possibile memorizzare il file di {file_size} byte. Spazio insufficiente.")
            break  # Interrompere il ciclo, non è possibile memorizzare altri file

memorizza_file([1100, 20000, 1048576, 512, 5000])
