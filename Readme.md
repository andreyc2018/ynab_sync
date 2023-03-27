# Convert bank statement to YNAB view

YNAB reorders the transactions on import, which makes it hard to find
incorrect transactions in YNAB by comparing the transactions in YNAB and a bank.

The running balance in YNAB is always different from the bank.
By default, YNAB sorts the transactions by Date, descending outflow, and descending inflow.

YNAB uses two separate columns for inflow and outflow.
A bank uses a single column for both kinds of transactions.

The converter translates the transactions from a bank into a table similar to YNAB's.
The converter sorts the transactions in the same way as in YNAB.
After that, the converter calculates the running balance.

## Examples

A bank uses the following schema:

"DATE","TRANSACTION TYPE","DESCRIPTION","AMOUNT","ID","MEMO","CURRENT BALANCE"

YNAB uses the following schema:

"DATE","DESCRIPTION","OUTFLOW","INFLOW","BALANCE"

The result schema:

"Index","Date","Outflow","Inflow","Balance"

## Usage

### Convert
```sh
./convert2ynab.py -b -1.87 bank_transactions.csv > bank.csv
```

### Compare
Open CSV or xlsx file in Excel and visually compare the result with YNAB.
