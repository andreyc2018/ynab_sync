"""
Compare bank and YNAB transactions.
The transaction files are prepared by convert2ynab.py
"""

import argparse
import pandas as pd


def compare(bank_filename, ynab_filename):
    bank_cmp_df = pd.read_csv(bank_filename, sep=',', header=0, usecols=['Date', 'Outflow', 'Inflow', 'Balance'])
    print(bank_cmp_df.info())
    # print(bank_cmp_df)
    ynab_cmp_df = pd.read_csv(ynab_filename, sep=',', header=0, usecols=['Date', 'Outflow', 'Inflow', 'Balance'])
    print(ynab_cmp_df.info())
    # print(ynab_cmp_df)
    # bank_cmp_df = pd.DataFrame(bank_full_df, columns=['Date', 'Outflow', 'Inflow', 'Balance'])
    # ynab_cmp_df = pd.DataFrame(ynab_full_df, columns=['Date', 'Outflow', 'Inflow', 'Balance'])
    # bank_cmp_df.sort_index(axis=1, inplace=True)
    # ynab_cmp_df.sort_index(axis=1, inplace=True)
    # print(bank_cmp_df.info())
    # print(ynab_cmp_df.info())
    # print(bank_cmp_df.equals(ynab_cmp_df))
    # bank_cmp_df.reset_index(drop=True, inplace=True)
    # ynab_cmp_df.reset_index(drop=True, inplace=True)
    result = bank_cmp_df.compare(ynab_cmp_df, keep_shape=True)
    print(result.info())
    print(result.to_string())
    # merged = pd.merge(bank_cmp_df, ynab_cmp_df, on=['Outflow', 'Inflow', 'Balance'], how='inner')
    # print(merged.info())
    # print(merged.to_string())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog = 'compare',
                    description = 'Compare bank and YNAB transactions. The transaction files are prepared by convert2ynab.py')
    parser.add_argument('bank', help='bank transactions filename')
    parser.add_argument('ynab', help='ynab transactions filename')

    args = parser.parse_args()
    compare(args.bank, args.ynab)
