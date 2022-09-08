h = int(input())
m = int(input())

hw = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
mw = ["o' clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]

if m == 0 :
    print(f'{hw[h]} {mw[0]}')
elif m <= 30 :
    if m == 15 or m == 30 :
        print(f'{mw[m]} past {hw[h]}')
    elif m == 1 :
        print(f'{mw[m]} minute past {hw[h]}')
    else :
        print(f'{mw[m]} minutes past {hw[h]}')
elif m > 30 :
    m = 60 - m
    h += 1
    if h > 12 :
        h = h - 12
    if m == 15 :
        print(f'{mw[m]} to {hw[h]}')
    elif m == 1 :
        print(f'{mw[m]} minute to {hw[h]}')
    else :
        print(f'{mw[m]} minutes to {hw[h]}')
