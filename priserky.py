# genetic code priserky 0 az 9 a je to 5 cisel napr. 2,5,8,9,1
# best priserka je 1,1,1,1,1
# mutacie

import random
monsters=[]
dlzka=5
cage=[]
sort=[]

def monster_creation():
    temp=[]
    for i in range (5):
        temp.append(random.randint(0,10))
    return temp

def iq_test(monster:list)-> int:
    return monster.count (1)

def sexik (monster1,monster2):
    new_monster=[]
    percent=random.randrange(1,101)
    for i in range(dlzka):
        if percent>7:
            new_monster.append(random.randrange(0,101))
        else:
            percent1=random.randrange(1,101)
            if percent1>50:
                new_monster.append(monster1[i])
            else:
                new_monster.append(monster2[i])
    return new_monster

def sort(cage):
    for x in range(len(cage),0,-1):
        for j in range(x-1):
            if iq_test(cage[j]) > iq_test(cage[j+1]):
                cage[j], cage[j+1]=cage[j+1], cage[j]
    return cage

for i in range(10):
    cage.append(monster_creation())
print(sort(cage))

for g in range (10):
    sort(cage)
    cage=cage[len(cage)//2::]
    for z in range (len(cage)):
        cage.append(sexik(cage[random.randrange(0,5)], cage[random.randrange(0,5)]))
    print(cage[::-1])
    input()

