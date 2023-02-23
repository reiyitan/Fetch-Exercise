import csv
from collections import defaultdict
from Transaction import Transaction 

class TransactionManager: 
    #Class for managing transactions. Reads in a .csv of payer transaction 
    #information and processes user requests. 

    def __init__(self, filepath): 
        self.payerBalances = self.initBalances(filepath)
        self.transactions = []
        self.initTransactions(filepath) 
    
    def initBalances(self, filepath): 
        #Creates a dictionary where keys are payer names and values are the 
        #total balances of payers. 

        #filepath: the file to the .csv containing transaction information. 
        #Returns a dictionary of payer-balance pairs. 
        payerBalances = defaultdict(lambda : 0) 
        with open(filepath, "r") as file: 
            reader = csv.reader(file) 
            next(reader) #skip .csv header
            for row in reader: 
                payer = row[0]
                amount = int(row[1])
                payerBalances[payer] += amount
        return dict(payerBalances)

    def insertTransaction(self, transaction): 
        #Helper method for initTransactions. 
        #Uses binary insert to insert a transaction into self.transactions,
        #sorted by timestamp.
        if len(self.transactions) == 0: 
            self.transactions.append(transaction) 
            return 
        
        lower = 0
        upper = len(self.transactions) - 1
        while lower <= upper: 
            middle = int(lower + ((upper - lower) / 2))
            if lower == upper: 
                if transaction <= self.transactions[lower]: 
                    self.transactions.insert(lower, transaction)
                    return
                elif transaction > self.transactions[lower]: 
                    self.transactions.insert(lower + 1, transaction) 
                    return 
            elif transaction == self.transactions[middle]: 
                self.transactions.insert(middle, transaction) 
                return 
            elif transaction < self.transactions[middle]: 
                upper = middle - 1
            elif transaction > self.transactions[middle]: 
                lower = middle + 1

    def initTransactions(self, filepath):     
        #Creates a list of transactions such that more recent transactions
        #are located at lower indices of the list, and older transactions
        #are located at higher indices of the list. Ignores transactions with 
        #negative amounts. 
    
        #filepath: the path to the .csv file containing transaction information. 
        with open(filepath, "r") as file: 
            reader = csv.reader(file) 
            next(reader) #skip .csv header 
            for row in reader: 
                payer = row[0]
                amount = int(row[1]) 
                timestamp = row[2] 
                self.insertTransaction(Transaction(payer, amount, timestamp))

    def processUserRequest(self, requested): 
        #Processes a user request according to the following rules: 
        #Points with the oldest timestamp are used first. 
        #Payer balances must not be negative after processing the user request. 

        #This function modifies self.payerBalances as well as self.transactions. 

        #requested: The amount of points a user requested. 
        usedTransactions = [] 

        while requested > 0: 
            currTransaction = self.transactions.pop() 
            payer = currTransaction.payer
            transactionAmount = currTransaction.amount
            payerBalance = self.payerBalances[payer] 
            if transactionAmount > 0: 
                usedTransactions.append(currTransaction) 

            if transactionAmount < 0: 
                requested -= transactionAmount 
                self.payerBalances[payer] -= transactionAmount
                continue
            elif payerBalance == 0: 
                continue 
            
            #transaction has enough to satisfy the request 
            if requested - transactionAmount <= 0: 
                #request cannot be satisfied without payer going negative
                if payerBalance - requested < 0: 
                    requested -= payerBalance 
                    currTransaction.amount -= payerBalance
                    self.payerBalances[payer] = 0
                #request can be satisfied without payer going negative 
                elif payerBalance - requested >= 0: 
                    currTransaction.amount -= requested 
                    self.payerBalances[payer] -= requested
                    requested = 0
            #transaction does not have enough to satisfy the request
            elif requested - transactionAmount > 0: 
                maxAmount = min(payerBalance, transactionAmount) 
                requested -= maxAmount
                currTransaction.amount -= maxAmount
                self.payerBalances[payer] -= maxAmount

            for transaction in usedTransactions: 
                if transaction.amount == 0: 
                    continue
                self.insertTransaction(transaction) 
