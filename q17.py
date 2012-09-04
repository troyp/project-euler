# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
# 20 letters. The use of "and" when writing out numbers is in compliance
# with British usage.
# ---------------------------------------------------------------------------

def n_to_words(n):
    small = n&99    # tens & units
    large = n>>2    # hundreds
    if large and small:
        return hundreds(large) + "And" + tensunits(small)
    elif large:
        return hundreds(large)
    else:
        return tensunits(small)

def tensunits(n):
    if n >= 20:
        tens, units = divmod(n,10)
        return d[tens*10]+d[units]
    return d[n]

def hundreds(n):
    return d[n] + "Hundred"

d = {  1 : 'One',
       2 : 'Two',
       3 : 'Three',
       4 : 'Four',
       5 : 'Five',
       6 : 'Six',
       7 : 'Seven',
       8 : 'Eight',
       9 : 'Nine',
       10 : 'Ten',
       11 : 'Eleven',
       12 : 'Twelve',
       13 : 'Thirteen',
       14 : 'Fourteen',
       15 : 'Fifteen',
       16 : 'Sixteen',
       17 : 'Seventeen',
       18 : 'Eighteen',
       19 : 'Nineteen',
       20 : 'Twenty',
       30 : 'Thirty',
       40 : 'Fourty',
       50 : 'Fifty',
       60 : 'Sixty',
       70 : 'Seventy',
       80 : 'Eighty',
       90 : 'Ninety'
    }
