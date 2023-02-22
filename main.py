import sys 
from TransactionList import TransactionManager

"""
Contains main driver code to create a user request. 
"""
def main(): 
    if len(sys.argv) != 3:
        print("usage: main.py <amount to spend> <.csv path>") 
        return
    requested = int(sys.argv[1])
    filepath = sys.argv[2]
    transactionMngr = TransactionManager(filepath)
    transactionMngr.processUserRequest(requested) 
    print(transactionMngr.payerBalances) 
    return transactionMngr.payerBalances

if __name__ == "__main__":
    main()