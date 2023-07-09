"""
THIS IS A SLOT MACHINE.
THIS SLOT MACHINE IS SIMPLE.
IT HAS A 3x3 DISPLAY
YOU WIN IF THE CENTER ROW IS A MATCH.
OTHER COMBINATIONS ARE NOT ACCOUNTED FOR.
"""

import random


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolMultiplier = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningRows = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningRows.append(line + 1)
    
    return winnings, winningRows

def getSlotMachineSpin(rows, cols, symbols) -> list:
    allSymbols = [] #List with all symbols taken from the dictionary
    for symbol, countSymbol in symbols.items():
        for _ in range(countSymbol):
            allSymbols.append(symbol)

    #print(allSymbols)

    columns = [] #Will be a nested list
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:] #Same as allSymbols.copy()
        for _ in range(rows):
            value = random.choice(allSymbols)
            currentSymbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def displaySlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i < len(columns) - 1: print(column[row], end = " | " )
            else: print(column[row])


def getDeposit():
    while 1:
        amount = input("How much would you like to deposit? €")
        if amount.isdecimal():
            amount = int(amount)
            if amount > 0: break
            else: print("Amount must be greater than 0.")
        else: print("Please enter a valid number.")

    return amount

def getNumberOfLines():
    while 1:
        lines = input("Enter the number of lines to bet on. (1 - " + str(MAX_LINES) + ") : ")
        if lines.isdecimal():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES: break
            else: print("Amount must be between 1 and {}".format(str(MAX_LINES)))
        else: print("Please enter a valid number.")
    
    return lines

def getBet():
    while 1:
        bet = input("How much would you like to bet on each line? €")
        if bet.isdecimal():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET: break
            else: print(f"Bet amount must be between €{MIN_BET}€ and €{MAX_BET}")
        else: print("Please enter a valid number.")
    
    return bet

def runSlots(balance):
    lines = getNumberOfLines()
    while 1:
        bet = getBet()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You are betting on {lines} line(s) with €{bet} each, for a total amount of €{totalBet}")
            print(f"You do not have enough to bet that amount. Your curent balance is €{balance}")
        else: break

    print(f"You are betting €{bet} on {lines} line(s). Total bet amount is €{totalBet}")

    slotDisplay = getSlotMachineSpin(ROWS, COLS, symbol)
    displaySlotMachine(slotDisplay)
    winnings, winningRows = checkWinnings(slotDisplay, lines, bet, symbolMultiplier)
    print(f"You won €{winnings}")
    if winningRows: print(f"Winning rows: ", *winningRows)

    return winnings - totalBet


def main():
    balance = getDeposit()

    while balance > 0:
        print(f"Current balance is €{balance}")
        spin = input("Enter any key to play (q to quit). ")
        if spin == "q": break
        balance += runSlots(balance)

    print(f"You left with €{balance}.")

main()