"""
payment = int(input("payment:"))
hours = int(input("hours:"))
if hours <= 40:
    salary = payment * hours
    print("salary:",salary)

elif hours > 40:
    overtime = hours -40
    salary = payment*hours+(3/2)*payment*overtime
    print("salary:",salary)
"""


"""
puan = float(input("give me a note the between of 0 and 1 "))
if puan <0 or puan > 1:
    print("error")

elif 0.9 <= puan <= 1:
    print("AA")

elif 0.8 <= puan < 0.9:
    print("B")

elif 0.7 <= puan < 0.8:
    print("C")

elif 0.6 <= puan < 0.7:
    print("D")

else:
    print("F")

"""
"""
count = 0
for i in [3,41,55,88,90]:
    count = count+i  # burada 1 yazarsak kaç tane eleman olduğunu i yazarsak elemanları toplar.
print(count)

count1 = 0
for j in range(1,101):
    count1 = count1+j # 1 den 100e sayıların toplamı # ancak hem sayma hemde toplama için pythonın özel aparatları vardır bunlar len() ve sum() aparatlarıdır.
print(count1)
"""
"""
count = [3,41,55,88,90]
print(len(count))
print(sum(count))


total = 0
count =0

while True:
    number = input("number:")
    if number == "done":
        print("done")
        break
    flag = True
    for i in number:
            if not i.isdigit() and i != '-' and i != '-':
                flag = False
                break

            if flag:
                number = int(number)
                count +=1
                print(count)
                total += number
                print(total)

if count >0:
    average = total / count
    print(average)

largest = None
print('before:',largest)
for i in [1,2,3,4,88,99,1452,55,44747,9845641]:      # en büyük en küçük sayı
    if largest is None or i < largest:
        largest = i
    print("loop:",i,largest)
print(largest)

startnumber = int(input("sn:"))
endnumber = int(input("es:"))
count = 0
for i in range(startnumber,endnumber+1):        # tek sayıların sayısı 
    if i % 2 == 1:
        count += 1
        print(i)
print("odd numbers:",count)

total = 0
number = int(input("number:"))
for i in range(0,number+1):     
    if i % 2 ==0:             # çift sayıların toplamı
        print(i)
        total += i
print(total)


target = random.randint(0, 100)
print(target)

while True:
    n = int(input("n:"))
    if n == (-1):
        break
    elif n < target:
        print("smaller than target")           # sayı bulmaca
    elif n > target:
        print("bigger than target")
    else:
        n == target
        print("cong yoy find the target number",target)
        

total =0
for i in range(1,11):
    n = int(input("n"))     # kullanıcıdan alınan 10 sayının toplamı
    total += n
print(total)

count =0
total =0
for i in range(1,11):
    n = int(input("n"))
    total += n                  # kullanıcıdan alınan 10 sayının averajı
    count += 1

if count > 0:
    average = total /count
print(average)


largest = None
print('before:',largest)
for i in range(10):
    n = int(input("n:"))
    if largest is None or n > largest: # kullanıcıdan alınan 10 sayını  en büyüğü
        largest = n

print(largest)



fact = 1
n = int(input("n:"))
for i in range(1,n+1): # faktoriyel
    fact = fact*i
print(fact)


for i in range(1,101):
    if i % 7 ==0:   # 7 nin katları
        print(i)


# fonksiyonlarla faktoriyel bulma
def faktoriyel(sayi):
    faktoriyel =1
    if sayi == 0 or sayi ==1:
        print("fakt",faktoriyel)
    else:
        while sayi > 1:
            faktoriyel = faktoriyel*sayi
            sayi -=1
        print("fakt",faktoriyel)

faktoriyel(5)

def toplama(a,b,c):
    return a+b+c
def ikiylecarp(a):
    return a*2
toplam = toplama(3,4,5)
print(ikiylecarp(toplam))
"""

numbers = dict()
for i in range(31):
    numbers[i] = i**2

print(numbers, "\n")







































