# Convert bank statement to YNAB view

## The story behind this project.

I use YNAB to track my expenses. They recommend reconciling the accounts often to keep the bank and YNAB accounts synchronized.

Once in a while, I forget to do it, and most active accounts lose synchronization.

I thought not a big deal. I can always open the bank and YNAB transactions and follow the running balance to find where I lost or added extra transactions.

However, YNAB reorders the transactions, and there is no way (as of this writing) to keep the order of the transactions as in the bank statement.
It means that each transaction's running balances in YNAB and a bank differ.

YNAB uses two separate columns for inflow and outflow.
By default, YNAB sorts the transactions by Date, outflow amount, and inflow amount in descending order.

The converter translates the transactions from a bank into a table similar to YNAB's.
Then, the converter sorts the transactions in the same way as in YNAB.
After that, the converter calculates the running balance.

## Usage

### Convert
```sh
./convert2ynab.py -b -1.87 bank_transactions.csv > bank.csv
```

### Compare

Open CSV file in Excel and visually compare the result with YNAB.
