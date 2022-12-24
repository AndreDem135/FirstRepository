## вывод форматированный в строку
n=int(input('Во сколько вы сегодня встали?'))
print(f' Хорошее сегодня утро в {n} утра ',end=', axaxaxaxaxa')
print(', нужно жить')
# вечный цикл с выходом по break
while True:
    print('БАНАН',end=' ')
    if n > 12:
        break
    else:
        n+=1
# двойной пребор из диапазона 2 значений (0,1) в дмумерном массиве или подбор двух параметров
for x in range(0,2):
    for y in range(0,2):
        print(x,y)
        if x>=y and (y!=0 or not(x)<=0):
            print(x,y,' - 6,67*10^(-11)')
# логическая переменная c произвольным названием True/False
fg=True 
if n<8:
    fg=False
print(fg)

a=int(input('ВВеди произвольное число! '))
print(a//n,a%n,a^a)
print(f'{(bin(a)[2:])}-ваше число в 2-ичной системе счисления')
b=input('введите дату вашего рождения (#22.12.2006)')
m=list(input('введите число случайное'))
m=list(map(int, m))
b=list(b)
c=b
b.append('ЧАйник')
b=''.join(b)
c.sort(reverse=True)
print(b.count('0'), b.index('Ч'),c,max(c),min(c),sum(m))
print('abab'+'bgb')
print(int('77',8))
print(m[0])
def fi(b):
    if b==0:
        return 0
    return b + fi(b-1)
print(fi(55))
spisok=[x for x in m if x-4<=7]
print(spisok)
div=set(m)
div.add(55)
p='87985241247126478734'
p.replace('5','33')
h='gg,aa,ss,ff,ddss,tt,e,,jojo'
result=h.split()
print(result)
with open('text1.txt') as f:
    Te1=f.readline()
    print(Te1)
with open('text1.txt') as f:
    Tex1=f.readlines()
    print(Tex1)
with open('text1.txt') as f:
    Texts=[x for x in f]
    print(Texts)
with open('text2.txt') as f:
    Te2=f.readline()
    print(Te2)
with open('text2.txt') as f:
    Tex2=f.readlines()
    print(Tex2)
with open('text2.txt') as f:
    Texts2=[x for x in f]
    print(Texts2)
