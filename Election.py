import random
import pandas as pd

wb=pd.read_excel('parties.xlsx')
a=[]
while True:
    x = random.choice(wb['정당'])
    a.append(x)
    print(a)
    for party in a:
        if a.count(party)>5:
            print(party)
    break

