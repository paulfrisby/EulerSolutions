# ------------------------------------------------------------------------------
# Project Euler - Problem 017 - Number letter counts
# ------------------------------------------------------------------------------
# Problem Link: https://projecteuler.net/problem=017
# ------------------------------------------------------------------------------
# Author: Paul Frisby
# Email: mail@paulfrisby.com
# Github: https://github.com/paulfrisby/
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Problem Definition
# ------------------------------------------------------------------------------
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# String representation generator
# ------------------------------------------------------------------------------
"""
Since the structure  / logic of the code is very similar, I have adapted my
solution of this problem in to a new function which returns a string containing
a representation in English of the number input. It takes any number in the
range -10^36 < n < 10^36
"""
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Main Code
# ------------------------------------------------------------------------------

# returns number of letters in the British English spelling of n, where 0<n<1000
def subThousandNumLetterCount(n):

    # not correct by itself, but useful when being called as part of larger number
    # since we do not say five thousand and zero
    if n == 0:
        return 0

    # prints error when passed number function isn't built to handle
    elif n < 1 or n > 999 or n%1 != 0:
        print (f'{n} is outside scope of function, n must be a non-negative integer below 1,000')
        return 0

    # '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    # '', [teens dealt with seperately], 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    # 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    # hundreds = units + 10 ('hundred and'), except for zero hundreds
    hundreds = [0, 13, 13, 15, 14, 14, 13, 15, 15, 14]

    # dealing with 'teen' special case
    if 9 < n%100 < 20:
        return hundreds[int(n/100)] + teens[n%10]

    # dealing with special case wherer number is an exact multiple of 100
    # as for 500 we say 'five hundred' not 'five hundred and'
    if n%100 == 0:
        return hundreds[int(n/100)] - 3

    return hundreds[int(n/100)] + tens[(int(n/10))%10] +  units[n%10]
        


# returns number of letters in the British English spelling of n, where 0 <= n < (10^36 - 1)
# uses powers of 1,000 up to 10^33 are defined in the Oxford English Dictionary
# does not deal with 'negative' / 'minus' numbers, although it is trivial to alter result to fit 
def numLetterCount(n):

    if n < 0 or n >= 10**36 or n%1 != 0:
        print (f'{n} is outside scope of function, n must be a non-negative integer below 10^36')
        return 0

    # 'zero'
    if n == 0:
        return 4

    letters = 0

    # to account for additional usage of 'and'
    # present only when final 3 digits is under 100, for example:
    # 42 = 'forty-two' but 1,025,042 = 'one million, twenty-five thousand, and forty-two'
    # but no additional and is present when final 3 digits are 100 or more, for example: 
    # 442 = 'four hundred and forty-two' and 1,025,442 = 'one million, twenty-five thousand, four hundred and forty-two'
    if n > 999 and n%1000 < 100 and n%1000 != 0:
        letters += 3

    # <1000 ,thousand, million, billion, trillion, quadrillion, quintillion, sextillion, septillion, octillion, nonillion, decillion
    thousandPower = [0, 8, 7, 7, 8, 11, 11, 10, 10, 9, 9, 9]
    
    # each 3 digit chunk follows the same rules, apart from with a suffix added for all but the last 3 digits
    # number of 3-digit chunks, 4 digits counts as 2 3-digit chunks
    thousands = int((len(str(n))+2)/3)

    # for each chunk add suffix +  absolute numbner to total
    for i in range(thousands):
        letters = letters + subThousandNumLetterCount(n%1000) + thousandPower[i]
        n = int(n / 1000)

    return letters


# returns an English representation of n as a string, where 0 < n < 1000
def subThousandNumberToText(n):

    # not correct by itself, but useful when being called as part of larger number
    # since we do not say five thousand and zero
    if n == 0:
        return ''

    # prints error when passed number function isn't built to handle
    elif n < 0 or n > 999 or n%1 != 0:
        print (f'{n} is outside scope of function, n must be a non-negative integer below 1,000')
        return False

    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens =  ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    hundreds = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

    # units
    textNum = units[n%10]

    # dealing with 'teen' special case
    if 9 < n%100 < 20:
        textNum = teens[n%10]

    # tens
    else:
        # e.g. 40 -> 'forty'
        if n%10 == 0:
            textNum = tens[(int(n/10))%10]
        # e.g. 00 -> ''
        elif (int(n/10))%10 == 0:
            pass
        # e.g. 42 -> 'forty-two'
        else:
            textNum = tens[(int(n/10))%10] + '-' + textNum

    # hundreds

    # e.g. 500 -> 'five hundred'
    if n%100 == 0:
        textNum = hundreds[int(n/100)]
    elif n < 100:
        pass
    else:
        textNum = hundreds[int(n/100)] + ' and ' + textNum

    return textNum
        


# returns an English representation of n as a string, where -10^36 < n < 10^36
# uses powers of 1,000 up to 10^33 are defined in the Oxford English Dictionary
def numberToText(n):

    # printing error for numbers function is not built to deal with
    if n >= 10**36 or n%1 != 0:
        return f'{n} is outside scope of function, n must be a integer smaller than 10^36 in magnitude'
    
    if n < 0:
        return 'negative ' + numberToText(-n)

    if n == 0:
        return 'zero'

    if n < 1000:
        return subThousandNumberToText(n)

    thousandPowerSuffix = ['' , 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']
    
    # casting to string to avoid problems with verfy large numbers
    n = str(n)

    textNum = ''

    # to account for additional usage of 'and'
    # present only when final 3 digits is under 100, for example:
    # 42 = 'forty-two' but 1,025,042 = 'one million, twenty-five thousand, and forty-two'
    # but no additional and is present when final 3 digits are 100 or more, for example: 
    # 442 = 'four hundred and forty-two' and 1,025,442 = 'one million, twenty-five thousand, four hundred and forty-two'
    if int(n[-3:]) < 100 and int(n[-3:]) != 0:

        last3Digits = n[-3:]
        textNum = 'and ' + subThousandNumberToText(int(last3Digits))
        n = n[:-3]
        
        # each 3 digit chunk follows the same rules, apart from with a suffix added for all but the last 3 digits
        # number of 3-digit chunks, 4 digits counts as 2 3-digit chunks
        thousands = int((len(n)+2)/3)

        # for each chunk add absolute number and suffix to string
        for i in range(thousands):
            if int(n[-3:]) == 0:
                pass
            else:
                textNum = subThousandNumberToText(int(n[-3:])) + ' ' + thousandPowerSuffix[i+1] + ' ' + textNum
            n = n[:-3]

    else:
        # no additional 'and' needed
        # each 3 digit chunk follows the same rules, apart from with a suffix added for all but the last 3 digits
        # number of 3-digit chunks, 4 digits counts as 2 3-digit chunks
        thousands = int((len(n)+2)/3)

        # for each chunk add absolute number and suffix to string
        for i in range(thousands):
            if int(n[-3:]) == 0:
                pass
            elif textNum == '':
                textNum = subThousandNumberToText(int(n[-3:])) + ' ' + thousandPowerSuffix[i]
            else:
                textNum = subThousandNumberToText(int(n[-3:])) + ' ' + thousandPowerSuffix[i] + ' ' + textNum
            n = n[:-3]

    return textNum


total = 0
for n in range(1, 1001):
    total += numLetterCount(n)
print (f'If all the numbers from 1 to 1000 inclusive were written out in words, {total} letters would be used.')

print (numberToText(-123456789000000000222333444555240099))
