__author__ = 'michaellin'

import Quandl
import sys


def main():
    print revenue_test("MSFT")


def revenue_test(symbl):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbl +'_REV_LAST')
    rev_series = rev_data_frame['Revenues']

    years_increasing = get_years_increasing(rev_series)
    if years_increasing > 2:
        return True, years_increasing
    else:
        return False, years_increasing


def eps_test(symbl):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbl + '_EPS_GRO')
    rev_series = rev_data_frame['Growth in Earnings Per Share']

    years_increasing = 0
    for i in reversed(rev_series):
        if i > 0:
            years_increasing += 1
        else:
            break

    if years_increasing > 5:
        return True, years_increasing
    else:
        return False, years_increasing


def roe_test(symbl):
    rev_data_frame = Quandl.get('OFDP/DMDRN_' + symbl + '_ROE')
    rev_series = rev_data_frame['Return on Equity']

    years_increasing = get_years_increasing(rev_series)

    if years_increasing > 5:
        return True, years_increasing
    else:
        return False, years_increasing


def get_years_increasing(arr):
    prev_rev = sys.maxint
    count = 0

    for i in reversed(arr):
        curr_rev = i
        if prev_rev > curr_rev:
            prev_rev = curr_rev
            count += 1
        else:
            break
    return count






if __name__ == "__main__":
    main()

