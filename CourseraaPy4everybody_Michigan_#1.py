# ----------------------
# February 2023
# ----------------------


# ----------------------
# PRIMEIRO USO
# instalar vscode
# instalar python
# usar dracula tema
# run linting py (ctrl+P)
# ----------------------


# GETTING STARTED

x = 2
print(x)
x = x + 2
print(x)

n = 3
while n > 0:  # repeatead
    print(n)
    n = n-1
print('Blastoff!')

print(type(n))  # vendo o tipo armazenado de dado

print("123"+"abc")

x = 1 + 2 * 3 - 8 / 4
print(x)

x = int(98.6)
print(x)

# convert elevator floors
# variveis menmonicas facilitam a leitura dos humanos
inp = input('Europe floor? ')
usf = int(inp)+1
print('Us floor', usf)

# ----------------------
# condicionais
# ----------------------

x = 5
if x < 10:  # condicional
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')

x = 4
if x > 2:
    print("Bigger")
else:
    print("Smaller")
print("all done")


# ----------------------
# multi-way
# ----------------------
x = 4
if x < 2:
    print("Smaller")
elif x < 10:
    print("Medium")
else:
    print("Large")
print('All done')


# ----------------------
# usando o comando TRY
# ----------------------
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)


# ----------------------
# usando o comando TRY
# ----------------------
astr = 'abc'
try:
    istr = int(astr)  # se der erro nessa linha
except:
    istr = -1  # esse será o comando default
print('First', istr)

astr = '123'
try:
    istr = int(astr)  # se der erro nessa linha
except:
    istr = -1  # esse será o comando default
print('First', istr)


# ----------------------
# ajustando entrada
# ----------------------
rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('not a number')


# ---------------
# exercise 3.1
# ---------------
hrs = input("Enter Hours:")
h = float(hrs)
tx = input("Enter rate per hour:")
t = float(tx)

if h <= 40:
    payment = h * t
else:
    plus = (h % 40) * (t*1.50)
    payment = (40*t) + plus

print(payment)


# ---------------
# exercise 3.3
# ---------------
score = input("Enter Score: ")
try:
    s = float(score)
    if s < 0.6:
        print("F")
    elif s >= 0.6 and s < 0.7:
        print("D")
    elif s >= 0.7 and s < 0.8:
        print("C")
    elif s >= 0.8 and s < 0.9:
        print("B")
    elif s >= 0.9 and s <= 1:
        print("A")
    else:
        print("-1")
except:
    print("-1")

# ----------
# FUNCTIONS
# ----------
# DRY DON'T REPEAT YOURSELF


def thing():
    print('Hello')
    print('Fun')


thing()

# exemplo 2
x = 5
print("Hello")


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


print("Yo")
print_lyrics()  # invoke /call
x = x + 2
print(x)


# exemplo 2
def greet(lang):
    if lang == 'es':
        print('hola')
    elif lang == 'fr':
        print('bonjour')
    elif lang == 'pt':
        print('Ola')
    else:
        print('hello')


greet('pt')  # passando o parametro


# exemplo 3
def addtwo(a, b):
    added = a + b
    return added


x = addtwo(1000, 33)
print(x)

# funcoes frutiferas retornam valores, funcoes nao frutiferas no retorna valores

# exercise 4.6


def computepay(h, r):
    if h <= 40:
        p = h * r
    else:
        plus = (h % 40) * (r*1.50)
        p = (40*r) + plus

    return p


hrs = input("Enter Hours:")
h = float(hrs)

rate = input("Enter your rate")
r = float(rate)

p = computepay(h, r)
print("Pay", p)


# ---------------------------
# LOOPS AND INTERATIONS
# ---------------------------


# while
n = 5
while n > 0:
    print(n)
    n = n - 1
print('Blastoff')
print(n)


# using BREAK para parar o loop
while True:
    line = input('> ')
    if line[0] == '#':  # ele nao insere nada e volta ao topo do loop
        continue
    if line == 'done':
        break
    print(line)
print('done')

# -----------------------------------
# LOOP PREDEFINIDO - DEFINITED LOOP
# ------------------------------------

# FOR
for i in [5, 4, 3, 2, 1]:
    print(i)
print('blastoff!')

friends = ['a', 'b', 'c']
for friend in friends:
    print('happy new year', friend)
print('blastoff!')


# pegando o maior numero da lista
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)

print('After', largest_so_far)

# usando loops
count = 0
sum = 0
print('before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum/count)


# pegando o menor numero da lista
smallest_so_far = None  # colocando um flag

print('Before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

# exercise5.2
largest = None
smallest = None
List_collector = []
while True:
    try:
        num = input("Enter a number: ")
        if num == 'done':
            break
        n = int(num)
        List_collector.append(n)
        largest = max(List_collector)
        smallest = min(List_collector)
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)
