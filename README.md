# Fetch-Exercise
This code has been implemented for the Fetch Backend Software Engineer Internship opportunity. 

# Description 
This program completes user requests to redeem points. These points are provided by payers, and payers provide their points through transactions. The goal of this program is to satisfy user requests by prioritizing points from the oldest transactions while maintaining non-negative payer balances. 

# Installing
This program requires that Transaction.py, TransactionList.py, main.py, and transactions.csv are located in the same directory. It is assumed that Python3 is the version of Python that is used to run this program. 

# Usage
* The provided transactions.csv file can be used, or you can provide your own .csv file. The first row of the .csv file should contain header information, for example:<br> 
&emsp;&emsp;"payer","points","timestamp"

* The rest of the rows of the .csv file should be formatted like so:  
&emsp;&emsp;"payer",amount,"YYYY-MM-DDTHH:MM:SSZ"  

* To execute the program from a terminal window: py main.py ./path/to/csv/file

# Author
Rei-Yi Tan
tanreiyi@gmail.com
