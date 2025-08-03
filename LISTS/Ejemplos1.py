""" cat_names = []
while True:
    print('Enter the name of cat ' + str(len(cat_names) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name]  # List concatenation
print('The cat names are:')
for name in cat_names:
    print('  ' + name) """

########################################################################

""" lista = [2, 1, 2, 3]
for i in range(len(lista)):
    print(lista[i]) """

########################################################################

""" for i in [0,1,2,3,4]:
    print(i) """

########################################################################

""" supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) """


########################################################
#########  Los operadores in y not in ##################
########################################################

""" my_pets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.') """


########################################################
#########   desempaquetado de tuplas  ##################
########################################################

""" cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(f"{size} - {color} - {disposition}") """

##############################################################

""" cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

print(f"{size} - {color} - {disposition}") """


########################################################
#########  Enumeración de elementos de lista  ##########
########################################################

""" supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
     print('Index ' + str(index) + ' in supplies is: ' + item) """

### CODIGO SIN ENUMERATE     

""" supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i]) """


########################################################
#########  Selección y ordenamiento aleatorio  #########
########################################################

""" import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets)) """

#####################################################

""" import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)   # Esta función modifica la lista, en lugar de devolver una nueva lista.
print(people) """


########################################################
#############  Encontrar valores #######################
########################################################

""" spam = ['hello', 'hi', 'howdy', 'heyas','howdy']

print(spam.index('hello'))
print(spam.index('hi'))
print(spam.index('howdy')) """ # Cuando la lista contiene duplicados del valor, el método devuelve el índice de su primera aparición


########################################################
#############  Añadiendo valores #######################
########################################################

""" spam = ['cat', 'dog', 'bat']
spam.append('moose')        

print(spam) """

#################################################################

""" spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
print(spam) """


########################################################
############# Eliminando valores #######################
########################################################

""" spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam) """

########################################################
############# Ordenar valores  #########################
########################################################

""" spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam) """

###############################################################

""" spam = [2, 5, 3.14, 1, -7]
spam.sort(reverse=True)
print(spam) """

###############################################################

""" spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam) """
      

########################################################
############# Ordenar valores  #########################
########################################################

""" spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam) """

########################################################
### Operadores booleanos de cortocircuito  #############
########################################################

# Ejemplo 1
""" spam = ['cat', 'dog']
if spam[0] == 'cat':
    print('A cat is the first item.')
else:
    print('The first item is not a cat.') """

############################################################

""" spam = []
if len(spam) > 0 and spam[0] == 'cat':
    print('A cat is the first item.')
else:
    print('The first item is not a cat.') """

########################################################
########### Tipos de datos de secuencia  ###############
########################################################

""" name = 'Zophie'
print(name[0])

print(name[-2])


print(name[0:4])

print('Zo' in name)

print('z' in name)

print('p' not in name)

for i in name:
     print('* * * ' + i + ' * * *') """

""" palabra ="palabra de prueba"

for index, item in enumerate(palabra):
     print('Index ' + str(index) + ' in supplies is: ' + item) """


########################################################
####### Tipos de datos mutables e inmutables  ##########
########################################################
""" La forma correcta de “mutar” una cadena es usar cortes y 
concatenación para construir una nueva cadena copiando 
partes de la cadena anterior: """

""" name = 'Zophie a cat'
print(name)

new_name = name[0:7] + 'the' + name[8:12]
print(new_name) """

########################################################
########### El tipo de datos Tupla #####################
########################################################

""" eggs = ('hello', 42, 0.5)
eggs[1] = 99 # esto da error.... """

########################################################

""" print(type(('hello',))) # Si solo tiene un valor en su tupla, puede indicarlo 
                        # colocando una coma después del valor dentro del paréntesis

print(type(('hello'))) # De lo contrario, Python considerará que ha ingresado un 
                       # valor dentro de paréntesis regulares.
 """

########################################################
####### Conversión de tipos de listas y tuplas #########
########################################################

""" lista1 = ['cat', 'dog', 5]
print(type(lista1))
lista2 = tuple(lista1)
print(type(lista2)) """

############################################################

""" palabra = "Hola Mundo Bonito"
print(type(palabra))
palabra2 = list(palabra)
print(palabra2) """

########################################################
##############      Referencias    #####################
########################################################
""" La asignación de variables no reescribe el valor, 
sino que modifica la referencia. """

""" spam = 42
print(spam) # 42
eggs = spam
print(eggs) #42
spam = 92
print(spam) # 92
print(eggs) # 42 """

####################################################

""" Pero las listas no funcionan así, porque sus 
valores pueden cambiar; es decir, son mutables """

""" spam = [0, 1, 2, 3]
eggs = spam  # The reference, not the list, is being copied.
eggs[1] = 'Hello!'  # This changes the list value.

print(spam)

print(eggs)  # The eggs variable refers to the same list. """


####################################################
##############   Argumentos    #####################
####################################################

""" def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)  # Prints [1, 2, 3, 'Hello'] """


##########################################################
###########  Las funciones copy() y deepcopy() ###########
##########################################################

""" Aunque pasar referencias suele ser la forma más práctica de 
trabajar con listas y diccionarios, si la función modifica la 
lista o el diccionario que se le pasa, es posible que no desee 
que estos cambios se apliquen al valor original de la lista o 
el diccionario. Para controlar este comportamiento, Python 
proporciona un módulo llamado copy que proporciona las 
funciones copy() y deepcopy() . La primera de estas, copy.copy() , 
puede crear una copia duplicada de un valor mutable, como una lista 
o un diccionario, no solo una copia de una referencia.  """

""" lista1 = [1,2,3,4]
lista2 = lista1
print(lista1)
print(lista2)
lista1.append("HolaMundo")
print(lista1)
print(lista2)
 """
#############################################

""" import copy
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)  # Creates a duplicate copy of the list
cheese[1] = 42  # Changes cheese
print(spam)  # The spam variable is unchanged.

print(cheese)  # The cheese variable is changed.
 """