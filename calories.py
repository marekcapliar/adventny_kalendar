fr = open('text/calories.txt', 'r')

maxim = 0
counter = 0
zoz = []
for row in fr:
    temp = row.strip()
    if temp.isdigit():
        counter += int(temp)
    else:
        if counter > maxim:
            maxim = counter
        zoz.append(counter)
        counter = 0

utzoz = sorted(zoz, reverse=True)
print(sum(utzoz[0:3:1]))

print(maxim)

