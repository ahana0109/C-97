intro=input("Write a sentence - ")
print(intro)
cCount=0
wCount=1

for c in intro:
    cCount+=1
    if(c==" "):
        wCount+=1

print(cCount)
print(wCount)