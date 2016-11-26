import random
# Lotto Max
Number = 7 
Min = 1
Max = 49
pick = []
for i in range(1,Number+1):
    draw=random.randint(Min,Max)
    while draw in pick:
        draw=random.randint(Min,Max)  
    pick.append(draw)
pick.sort()
print(pick)
