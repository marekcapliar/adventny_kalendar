fr = open('text/rps.txt', 'r')

game = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9, ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}
counter = 0
for row in fr:
    chars = row.strip().split()
    counter += game[(chars[0], chars[1])]   # game- pozerame do dict, chars[0] je prve pismenko, chars[1] je druhe pismenko
print(counter)
