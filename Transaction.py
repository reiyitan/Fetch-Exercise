from datetime import datetime

class Transaction: 
    #Class that allows for encapsulation of individual transactions. 

    #note: the datetime module considers earlier dates to be less than more recent dates. 
    #The Transaction class considers earlier dates to be greater than more recent dates.
    #This is for the purpose of having earlier transactions be sorted at higher indices of a list. 

    def __init__(self, payer, amount, timestamp):
        #Initializes a Transaction object. 
        #payer: the name of the payer as a string.
        #amount: the amount of the payer's transaction as an int.
        #timestamp: the date and time of the transaction formatted as "yyyy-mm-ddThh:mm:ssZ".
        self.payer = payer
        self.amount = amount 
        self.timestamp = self.cleanTimestamp(timestamp) 

    def cleanTimestamp(self, timestamp): 
        #Parses a timestamp and formats it to work with the datetime module. 
        #Returns the formatted timestamp.
        timestamp = timestamp.replace("T", " ") 
        timestamp = timestamp.replace("Z", "") 
        return timestamp

    def __lt__(self, other): 
        #Enables comparison between two Transaction objects. 

        #Returns true if the transaction referenced by self occured after 
        #the transaction referenced by other. Returns false otherwise. 
        return self.timestamp > other.timestamp
    
    def __le__(self, other): 
        #Enables comparison between two Transaction objects. 

        #Returns true if the transaction referenced by self occurred either after or 
        #at the same time as the transaction referenced by other. 
        return self.timestamp >= other.timestamp 
