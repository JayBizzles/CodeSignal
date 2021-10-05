#get the length of the letters inside list and add 2 to the size and add asterisk
#return that list
def addBorder(picture):
    result = []
    stars = ""
    last = []
    stars='*'*(len(picture[0])+2)
    print(stars)
    last.append(stars)
    for let in picture:
        res = let.rjust(len(let)+1,'*')
        dum = res.ljust(len(res)+1,'*')
        last.append(dum)
    last.append(stars)
    print(last)
addBorder(["abc","ded"])