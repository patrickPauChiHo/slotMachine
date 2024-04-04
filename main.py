import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 3,
    "B" : 4,
    "C" : 6,
    "D" : 7
}

symbol_value = {
    "A" : 10,
    "B" : 7,
    "C" : 5,
    "D" : 3
}

def checking_winnings(columns, lines,bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        #get the first symbol in the row
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines        

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end="")
                
        print()


# keep asking for input until the user enter a valid number
def deposit():
    while True:
        amount = input("What wouold you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("lines must be between 1 and " + str(MAX_LINES))
        else:
            print("Please enter a number")
            
    return lines

def get_Bet():
    while True:
        amount = input("What wouold you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET < amount < MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")
            
    return amount

def spin(balance):
    while True:
        lines = get_number_of_lines()
        bet = get_Bet()
        total_bet = lines * bet
        
        if total_bet > balance:
            print(f"Your current balace is ${balance}. You don't have enough money bro.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is ${total_bet}. Good luck!")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = checking_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Your current balance is ${balance}")
        answer = input("Press Enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")
    
main()