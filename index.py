# REVIEWING BASIC PYTHON CONCEPTS

## SHOWING ANYTHING ON THE SCREEN
print ("Hello World, have a good day")

## THESE ARE SOME VARIABLES IN PYTHON

### STRING <- They are used for text
name = "josé"
print(type(name))

### INT <- They are used for whole numbers
age = 28
print(type(age))

### FLOAT <- They are used for decimal numbers
height = 1.70
print(type(height))

### BOOLS < They are used for say whether it is true or false
hiv = False
print(type(hiv))

### LIST <- They are used for list anything
comprar = ["rice","beans","meat","suggar","salt"]
print(type(comprar))

### TUPLES <- they are used for the information cannot be changed.
cordenadas = (150,203)
print(type(cordenadas))

### SET <- they are used when data doesn't need to be ordered and isn't repeated.
conj = {1,2,3,"rice",4}
print(type(conj))

### DICT <- They are used like a card, very common in databases.
json = {
    "name": "jose",
    "age": 28,
    "have HIV?": False
}
print(type(json))

## THESE ARE PYTHON OPERATIONS

### SUM
x = 18
y = 5
result = x+y
print(result)

### SUBTRACTION
x = 18
y = 5
result = x-y
print(result)

### MULTIPLICATION
x = 18
y = 5
result = x*y
print(result)

### DIVISION
x = 18
y = 2
result = x/y
print(result)

### TO THE POWER   
x = 18
y = 2
result = x**y
print(result)

## INPUT DATA

x = float(input("Input your first value: "))
y = float(input("Input your second value: "))

#### In this case, f-string was used to insert a variable in the middle of the string.
print(f"Sum = {x+y}")
print(f"Sub = {x-y}")
print(f"Mult = {x*y}")
print(f"Div = {x/y}")
print(f"Pow = {x**y}")

## IF, ELIF AND ELSE

t = float(input("input any value:\n"))
g = float(input("input any value:\n"))

o = input(""" Digite o valor para escolher sua operação
1 - soma
2 - subtração
3 - Multiplicação
4 - Divisão
""")

if o=="1":
    print(t+g)
elif o=="2":
    print(t-g)
elif o=="3":
    print(t*g)
elif o=="4":
    print(t/g)
else:
    print("opção inválida")

## LOOPS
### FOR <- These are used when you know when to stop -  when loops thats limited for anything
for i in range(5):
    print(i)
#### in that case "i", its anything and "range" is the top of you get

### WHILE