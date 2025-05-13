import random

class LotteryMachine:

    def __init__(self) -> None:

        self.list_element = [1,2,3,4,5,6,7,8,9,22,"a", "b", "c", "d", "e"]
        self.winning_ticket:list[str] = []

    def draw_winning_ticket(self) -> None:

        self.winning_ticket = random.sample(self.list_element, 4)

    
    def announce_winner(self) -> None:
        
        print(f"Il biglietto vincente è: {self.winning_ticket}")
        print(f"Se il tuo ticket ha gli stessi elementi ma in ordine diverso vinci lo stesso un premio")
    
lottery = LotteryMachine()
lottery.draw_winning_ticket() 
lottery.announce_winner()  