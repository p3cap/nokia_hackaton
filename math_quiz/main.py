"""
√ - sqrt()
"""

print('1.: 5')
"""
Távolság képlettel:

(R-1)^2+(R-2)^2=R^2
=>R^2R+5 = 0
R1 = 5
R2 = 1 (nem realisztikus az ábrához)
"""
print('2.: 1.513')
"""
(4^x + 6^x = 9^x)

4 = 2^2
6 = 2x3
9 = 3^2

(2^2)^x + (2x3)^x = (3^2)^x
2^(2x) + 2^x * 3^x = 3^(2x)

a = 2^x
b = 3^x

=> a^2 + ab = b^2 => a^2 + ab - b^2 = 0

Másodfokú egyenlet:
a = (-b +- √(b^2 + 4b^2)) / 2
a/b = (-1 +- √5) / 2
(2^x / 3^x) = (-1 +- √5) / 2

x * log(2/3) = log((-1 + √5) / 2)
x = log((-1 + √5) / 2) / log(2/3)
x ~= 1.513
"""
print('3.: 9')
"""
teleszkopikus összeg

'átlagos eset': 1 / (√n + √(n+1))

1 / (√n + √(n+1)) * (√(n+1) - √n) / (√(n+1) - √n)
= (√(n+1) - √n) / ((√n + √(n+1))(√(n+1) - √n))
= (√(n+1) - √n) / ((n+1) - n)
= √(n+1) - √n

1 / (√n + √(n+1)) = √(n+1) - √n

=> (√2 - √1) + (√3 - √2) + (√4 - √3) + ... + (√100 - √99)

láncolt kivonás -> minden középső tag kiesik:

= √100 - √1 = 10 - 1 = 9

"""
print('4.: 1')
"""
x1 = 1
x2 = -1
Manuálisan kibróbáltam alap számokkal... illetve brute force programmal biztosra mentem (with sympy)
"""
print('5.: 150')
"""
x:= cica; y:= asztal; z:= teknős
x + y - z = 130cm
z + y - x = 170cm

(x+y-z)+(y+z-x)=300 => x-x + z-z + y+y => 2y = 300
y = 150
"""
print('6.: 27')
"""
x:= egér; y:= kutya; z:= cica
x+z=10
y+x=20
y+z=24
x+y+z=?

> egyik szám kiszámolásával az összeset meg lehet határozni

x kiszámítása:
(x+z)+(y+x) = 10 + 20 = 2x+y+z = 30
(2x+y+z) - (y+z) = 30 - 24 = 6 = 2x
x = 6/2 = 3kg

y = 20-x = 17kg
z = 10-x = 7kg

x+y+z = 3 + 17 + 7 = 27kg
"""
print('7.: 0.54')
"""
Anna nyer, ha először dob 6-ost, ami 1/6 esély. 
Ha egyikük sem dob 6ost az első két dobásban, újra kezdődik a játék ugyanonnan, 
tehát az esély megismétlődik. 
P := esély
P = 1/6 + (5/6 * 5/6) * P.

P ~= 0.54.
"""