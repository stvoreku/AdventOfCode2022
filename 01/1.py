with open("input_1") as f:
    lines = f.readlines()

ELVES_LIST = []
elve_pointer = 0
for l in lines:
    l = l.strip()
    if l != '':
        try:
            ELVES_LIST[elve_pointer] += int(l)
        except IndexError:
            ELVES_LIST.append(int(l))
    else:
        elve_pointer +=1

#and 1
print(sorted(ELVES_LIST)[-1])
#ans 2
print(sorted(ELVES_LIST)[-1] + sorted(ELVES_LIST)[-2] + sorted(ELVES_LIST)[-3])