import random

MAX_BET=1000
MIN_BET=1
MAX_LINE = 3

ROWS=3
COLS=3

symbols_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbols_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_win(columns, lines, bet, values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol!= symbol_to_check:
                break
        else:
            winnings += values[symbol] + bet
            winning_line.append(lines+1)
    
    return winnings, winning_line
    

def get_slot_machine_spin(row, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for _ in range(row):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1 :
                print(column[row], end="|")
            else:
                print(column[row], end=" ")
    
        print()


def deposit():
    while True:
        amount=input("What would you like to deposit?: Rs.")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be grater than 0")
        else:
            print("please enter a valid no.")
    return amount

def get_number_line():
    while True:
        line=input("enter the no. of line to bet on (1 - "+str(MAX_LINE)+")?")
        if line.isdigit():
            line=int(line)
            if 1<=line<=MAX_LINE:
                break
            else:
                print("Enter a valid input")
        else:
            print("please enter a valid no.")
    return line


def get_bet():
    while True:
        amount=input("What would you like to bet?: Rs.")
        if amount.isdigit():
            amount=int(amount)
            if MAX_BET>=amount>=MIN_BET:
                break
            else:
                print(f"Amount must be between Rs.{MIN_BET} - Rs.{MAX_BET}.")
        else:
            print("please enter a valid no.")
    return amount

def game(balance):
    lines= get_number_line()
    while True:
        bet=get_bet()
        total_bet= bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet that amount, your current balance is: Rs.{balance}")
        else:
            break
    print(f"You are betting Rs.{bet} on {lines} lines. Total= Rs.{total_bet}")
    
    slot= get_slot_machine_spin(ROWS, COLS, symbols_count)
    
    print_slot_machine(slot)
    
    winning, winning_line=check_win(slot, lines, bet, symbols_values)
    print(f"You won Rs.{winning}.")
    print(f"You won on ", *winning_line)
    return winning - total_bet
    

def main():
    balance=deposit()
    while True:
        print(f"Current balance is Rs{balance}")
        spin = input("press enter to play (q to quit).")
        if spin == "q":
            break
        balance += game(balance)
    print(f"you are left with Rs{balance}")

main()