def blackjack_hand_total(cards: list[int]) -> int:
    somma_carte = 0
    asso = 0
    
    for i in cards:
        
        somma_carte += i
        
        if i == 1 and somma_carte < 11:
            asso == 11
        elif i == 11 and somma_carte > 21:
            somma_carte -= 10

        elif cards[1] == 11:
            somma_carte -= 5
            
    return somma_carte

print(blackjack_hand_total([2, 3, 5]))
print(blackjack_hand_total([11, 5, 5]))
