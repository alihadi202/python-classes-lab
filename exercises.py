
class Game():
    def __init__(self):
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    def print_board(self):
        b = self.board
        print(f"""
                A   B   C
            1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
                ----------
            2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
                ----------
            3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def play_game(self, spot , turn):
        if not self.board[spot]:
            self.board[spot] = turn

            return True
        else:
            return False
        
    def check_win(self , turn):
        cols = ["a" , "b" , "c"]
        i = 0
        for col in cols:
            if self.board[f'{col}{1}'] == turn  and self.board[f'{col}{2}'] == turn  and self.board[f'{col}{3}'] ==turn:
                return True

        for i in range(3):
            if self.board[f'{cols[0]}{i+1}'] ==turn and self.board[f'{cols[1]}{i+1}'] == turn and self.board[f'{cols[2]}{i+1}'] ==turn:
                return True
            
        if self.board[f'{cols[0]}{1}'] ==turn and self.board[f'{cols[1]}{2}'] == turn and self.board[f'{cols[2]}{3}'] ==turn:
            return True
        if self.board[f'{cols[2]}{1}'] ==turn and self.board[f'{cols[1]}{2}'] == turn and self.board[f'{cols[0]}{3}'] ==turn:
            return True
        
        

game_instance = Game()
game_instance.print_board()
turn ="X"
turns = 0
while True:
    
    spot = input("choose spot ")
    valid = game_instance.play_game(spot, turn)
    game_instance.print_board()
    done= game_instance.check_win(turn)
    if done :
        print(turn+" won")
        break
    
    if valid :
        turn ="O" if turn=="X" else "X"
        turns=(turns+1)%10
    else:
        print("chosen already choose again ")
    
    if turns == 9:
        print("it's a tie")
        break

    
    
    




def print_message(self):
  pass
## If there is a tie: print("Tie game!")
## If there is a winner: print(f"{self.winner} wins the game!")
## Otherwise: print(f"It's player {self.turn}'s turn!")

def render(self):
  pass
# Call upon print_board
## Call upon print_message

