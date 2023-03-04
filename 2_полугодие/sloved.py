#5
for i in range(1,100):
    chislo=''
    num=(bin(i)[2:])
    if num.count('1')%2==0:
        chislo='10'+num[2:]+'0'

    if num.count('1')%2!=0:
        chislo='11'+num[2:]+'1'
    if int(chislo,2)>40:
        print (i, int(chislo,2))
        break
#or
for N in range(516):
    b = f'{N:b}'
    if N % 2 == 0:
        b += '10'
    else:
        b = '1' + b + '01'
    if int(b, 2) > 516:
        print(N)
        break

#16
sys.setrecurtionlimit()
def f(n):
    if n==1:
        return(1)
    else:
        return(n*f(n-1)):
    print(f(2023)/f(2020))
    
it1 = it2 = 1
for x1 in range(1, 2024):
    it1 = it1*x1
for x2 in range(1, 2021):
    it2 = it2*x2
print(it1/it2)

#17
count = 0
maxsum = 0
a = [int(i) for i in f] # f - импортированный файл
x = [i for i in a if i%17 == 0]
maxX = max(x)
minX = min(x)
for i in range(len(a)-1):
    if a[i]%17 == 0 or a[i + 1]%17 == 0:
        count += 1
        sum = a[i] + a[i + 1]
        if sum > maxsum:
            maxsum = sum
print(count, maxsum)

#23
def f(x,y):
    if x>y or x==17:
        return 0
    elif x==y:
        return 1
    return f(x+1,y) +f(x*2,y)
print(f(1,10)*f(10,35))

#24
with open('24.txt') as f:
   let=f.readline()
   count,maximum=0,0
   #text=''
   delta=0
   for i in range(len(let)-1):
      if (let[i]=='C' or let[i]=='D' or let[i]=='F') and (let[i+1]=='A' or let[i+1]=='O'):
         delta=0
         #text=text+let[i]+let[i+1]
         count+=1
         maximum=max(count,maximum)
      else: delta+=1
      if delta==2:
         count=0
         #text=''
print(maximum)

with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)

#25
from operator import itemgetter
def f25(chislo):
    if int(chislo)%2023==0:
        ost=int(chislo)//2023
        itog.append(chislo)
        itogost.append(ost)

itog=[]
itogost=[]
for i in range(10):
  for y in range(1000000):
      chislo='1'+str(i)+'21394'
      f25(chislo)

      chislo='1'+str(i)+'2139'+str(y)+'4'
      if int(chislo)>10**10: break
      f25(chislo)

itogo=list(zip(itog,itogost))
print(*itogo)
print(sorted(itogo, key=itemgetter(1)))
for i in range(2023,10**10,2023):
    num=str(i)
    if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
        print(i,i//2023)
        
#26
with open('26.txt') as f:
    data=[int(x) for x inf]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]

    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
print(k,mini)

#27-А

1)Из-за того, что мало пунктов, мы можем использовать перебор.
2)Сначала мы загржаем данные из файла в список.
3)Избавляемся от первого элемента.
4)Затем мы создаем переменную с некоторыми параметрами нашего списка, напрмиер длина.
5)Сдваиваем список.
6)Используя срезы мы меняем список для работы. меняем список с помощью них.
7)Меняем таким образом, чтобы киллометр, для которого мы считаем стоимость доставки, стоял на первом месте.
8)Важный момент, когда мы создаем новый список с использыванием среза мы обнуляем стоимость. Чтобы она не накапливалась.
9)П0рименяем саму формулу, считаем стоимость доставки.
10)создаем переменную для пересчета индекса элементов после середины списка. от длины списка отнимаем индекс элемента.
11)Считаем стоимость накоплением
12)Найденную стоимость на каждом киллометре мы добавляем в новый список.
13)Выводим индекс минимального элемента списка со стоимостью + 1.

#27-Б
1)Используем метод итераций вместо перебора (приближения). С каждым шагом мы приближаемся к точному определенному решению.
2)Вся программа находится в бесконечном цикле, выход из которого это точное решение.
3)Точное решение, это два раза повторяющийся ответ при шаге 1.
4)Если в 27-А проверя большой список фиксированно, большой цикл перебора организован с использованием трех переменных , старта финиша и шага.
5)Шаг настраивается таким образом, чтобы было двадцать равнораспределенных замеров по всей дороге.
6)после каждого прохода цикла переменные старта, конца и шага пересчитываются.
7)Определяем минимальную стоимость среди двадцати значений и киллометр, которому она принадлежит,





