# Convert bank statement to YNAB view

By default, transactions are sorted by Date, then largest outflow to largest inflow.

YNAB uses two column separate columns for inflow and outflow.
A bank uses single column for both kind of transactions.

## Examples

Input schema:
"DATE","TRANSACTION TYPE","DESCRIPTION","AMOUNT","ID","MEMO","CURRENT BALANCE"

Output schema:
"DATE","DESCRIPTION","OUTFLOW","INFLOW","BALANCE"

## Notes

The BALANCE field is calculated starting from some initial value.
If there is no initial value then balance starts from zero.
