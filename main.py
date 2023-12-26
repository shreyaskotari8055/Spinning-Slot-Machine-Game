import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET =1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 2,
    "B" : 5,
    "C" : 3,
    "D" : 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for colomn in columns:
            symbol_to_check = colomn[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    
    columns = []
    for _ in range(cols):
        colomn = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            colomn.append(value)
        columns.append(colomn)
    
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()        


def deposite():
    while True:
         amount = input("What would you like to deposite? : ")
         if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than zero")
         else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet (1-"+ str(MAX_LINES) +") :")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet_amount():
    while True:
        amount = input("What would you like to bet :")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET  <= amount <= MAX_BET:
                break
            else:
                print(f"Betting amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
    return amount


def spin():
    lines = get_number_of_lines()
    while True:
        bet = get_bet_amount()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have sufficient balance to bet, youur current balance is : {balance}")
        else:
            break
    print(f"Your betting {bet} on {lines} lines. Total bet is : {total_bet}")


    slot = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_values)
    print(f"You won {winnings}.")
    print(f"You won on lines:", *winning_lines)

   
def main():
    balance = deposite()
   

main()