############### String literal #################
#print('''
#Olá
#''')

#print('Olá'
#      'Olá novamente!')

#imprimi a palabra três vezes
#print(3 * 'Python')

#concatenar
#print(3 * 'py' + 'thon')
#print(3 * 'py'  'thon')

########################### Variáveis #############
#b = 2
#a = 4
#print(a+b)
#concatenar e tranformar em string
#h = 'z'
#print(h + str(b))

#x,c,v = 4,5,6
#print(x+c+v)


########################## Indexando e Fatiando #############
#palavra = 'python'

#print(palavra[0])
#print(palavra[1:3])
#print(palavra[2:5]) #caractéres da posição 2 até a 5 (cinco não incluído)
#print(palavra[:3])
#print(palavra[1:])

#print(len(palavra)) #contar quantos elementos tem a string


##################### criando lista #############
#notas = [7,8,5,4,8,10,9,5]
#len(notas)
#sum(notas)

#media = sum(notas)/len(notas)
#print(media)

#notas.append(6) #adicionando mais uma nota a lista
#media = sum(notas)/len(notas)
#print(media)

#print(notas)
#notas.pop() #caso nao seja especificado um numero, ele vai tirar o ultimo (-1)
#print(notas)


################# Operadores lógicos e de comparação #########

#dois = 2

#print(dois == 2)
#print(dois != 2)
#print(dois < 3)

#mentira = 'false'
#verdade = 'true'

#print(verdade and mentira) ou print(verdade & mentira)
#print(verdade or mentira) ou print(verdade | mentira)

#print(not mentira)
#print(not verdade)


####################### Métodos e funções
#def minha_funcao_imprimir():
  #  print('Olá!')
   # print('Mundo')
#print(minha_funcao_imprimir())

#def dois_valores(valor1,valor2):
#    '''
 #       Está função suma dois valores e retorna o resultado.
  #  '''
#    return valor1 + valor2
#print(dois_valores(123,246))


##################### condicionais
#devo_continuar = True
#if devo_continuar == True:
#    print('continue')

#criando lista
#pessoas_conhecidas = ['Joao', 'Maria', 'Josefa', 'Ana']
#pessoa = input('Entre com o nome da pessoa: ')
#print(pessoa)

#if pessoa in pessoas_conhecidas:
#    print('Você conhece essa pessoa')
#if pessoa not in pessoas_conhecidas:
#    print('Você conhece essa pessoa')
#else:
#    print('Você não conhece essa pessoa')

###################### Condicionais - elif
'''
temperatura = float(input('Por favor digite a temperatura corporal: '))
if temperatura < 36:
    print("Paciente com hipotermia")
elif (temperatura >=36) & (temperatura<=37.5):
    print("Paciente com temperatura normal")
elif (temperatura >37.5) & (temperatura<=39.5):
    print("Paciente com Febre")
elif (temperatura >39.5) & (temperatura<=41):
    print("Paciente com Febre alta")
else:
    print("Paciente com Hipertermia")

'''

'''
#Sistema para saber se um pessoa pode votar ou não, através da idade.
idade = int(input('Informe sua idade: '))
if idade < 16:
    print('Você não pode votar!')
elif (idade >= 16) & (idade <=17):
    print('É opcional você votar!')
elif (idade>= 18) & (idade<=69):
    print('É obrigatório você votar!')
else:
    print('É opcional você votar!')
'''
'''
# Código resumido
idade = int(input('Informe sua idade: '))
if idade <= 16:
    print('Você não pode votar!')
elif (idade == 16) | (idade ==17) | (idade >= 70):
    print('É opcional você votar!')
else:
    print('É obrigatório você votar!')
'''

notas = [1,2,3,4,5,6,7]
minha_variavel = "Olá mundo!"
'''
print(minha_variavel[0])
print(minha_variavel[1])
print(minha_variavel[2])
print(minha_variavel[3])
print(minha_variavel[4])

#forma resumida para imprimir toda a lista
for letra in minha_variavel:
    print(letra)
'''
'''
# Utilizando range
print(range(5,20,2))
print(list(range(5,20,2)))

for numero in range(5,20,2):
    print(numero + 28)
'''

# Utilizando while
'''
num = 1
while num <= 9:
    print(num)
    num = num +2 # ou num += 2

usuario_quiser = True
while usuario_quiser:
    usuario_input = input("Quer continuar? (s/n)")
    if usuario_input == 'n':
        usuario_quiser = False

for num in range(10):
    if num % 2 == 0: #resto da divisão por 2 igual a 0
        print(f'{num} é par') # o f é o format string, string do tipo format
    else:
        #print('{} é ímpar'.format(num)) ou pode usar o código abaixo 
        #print(num, 'é ímpar')
        # ou também pode contatenar e covnerter para string
        print(str(num) + ' é ímpar')

# Usando continue
for num in range(10):
    if num % 2 == 0:
        print(f'{num} é par')
        continue # passe para o próximo número
    print(f'{num} é ímpar')

# Usando break
for numero in range(2,10):
     for divisor in range(2, numero):
         if numero % divisor == 0:
             print(f'{numero} é divisível por {divisor}')
             break
     else:
         print(numero, ' é primo')

# usando listas
# adicionando elementos com dict
telefone = dict([('Josi', 1234), ('Manu', 878787), ('Fred', 232323)])
print(telefone)
telefone["Felipe"]= 909090 #adicionando um elemento na lista
print(telefone)
# removendo elementos com del
del telefone['Josi'] # remover elemento da lista
print(telefone)
# colocar em ordem alfabética
print(sorted(telefone))
#verificar se está na lista
print('Felipe' in telefone) #Caso esteja na lista retornará True
# outra forma
print(telefone.get('Danilo')) # não está na lista, e não retornará erro, apenas None
print(telefone.get('Felipe'))



#Compreesão de listas
print([x for x in range(10) if x % 2 == 1]) # lendo: X para cada elemento X dentro de um range de 10, se o resto de X igual a 1, ele vai imprimir apenas os números ímpares

# trabalhando de outra forma as listas
pessoas_conhecidas = [' Ana', 'Manuela', 'feLipe', 'pEDRO']

print(pessoas_conhecidas, ' => lista desorganizada')

pessoas_normalizadas = [pessoa.strip().capitalize() for pessoa in pessoas_conhecidas]
#strip() -> remove os espaços
#capitalize() -> primeira letra maiúcula e o resto menúscula
print(pessoas_normalizadas)


#compreensão de lista com mais de um for
# como saber os amigos em comuns entre dois amigos?

amigos_de_fred = ['jose', 'felipe', 'pedro', 'léo']
amigos_de_davi = ['antonio', 'chica', 'pedro', 'marcos']
# af = amigos de fred
# ad = amigos de davi
#print([af for af in amigos_de_fred for ad in amigos_de_davi if af == ad]) # está percorrendo as duas listas e identificando os amigos em comum
#amigos_em_comum = [(af,ad) for af in amigos_de_fred for ad in amigos_de_davi if af != ad]
amigos_em_comum = [(af,ad) for af in amigos_de_fred \
                   for ad in amigos_de_davi if af != ad]
#print(amigos_em_comum)
# usando um outro código para fazer a mesma coisa, mas com mais linhas de código
nao_amigos = []
for af in amigos_de_fred:
    for ad in amigos_de_davi:
        if af != ad:
            nao_amigos.append((af,ad))
print(nao_amigos)


# usando a função Lambda
#ao_quadrado = lambda x: x**2
#print(ao_quadrado(4))

def soma_dois_numeros(a,b):
    return a+b
print(soma_dois_numeros(2,5))


def impar_ou_par(n):
    if n%2 == 0:
        print(f'{n} é par')
    else:
        print(f'{n} é ímpar')
impar_ou_par(33)

impopar = lambda n: print(f'{n} é par') if n%2 == 0 else print(f'{n} é ímpar')
impopar(32323232)

#usando *args ou argumentos, mas o que vale é o asterisco
def soma(*args):
    return sum(args)
#def soma(*argumentos):
#    return sum(argumentos)
print(soma(3,6,90,32,12))

#kwargs é usando dois asteriscos, serve para desembrulhar a lista
def formata_hora(horas, minutos='00', segundos='00'):
    print(f'{horas}:{minutos}:{segundos}')
tempo = {
    'horas':'15',
    'minutos':'19',
    'segundos':'54'
}
print(tempo)
formata_hora(**tempo)

l1 = 'banana batata couve frango'.split()
l2 = 'fruta legumes verdura carne'.split()

print(l1,l2)
lista_zipada = zip(l1,l2)
print(lista_zipada) #arquivo zipado
print(list(lista_zipada)) #retirado do arquivo zipado

# trabalhando de outra forma com for
indexes = range(4)
campos = 'nome idade sexo cidade'.split()
dados = 'Pedro 39 Masculino Santos'.split()
for idx, campos, dados in zip(indexes, campos, dados):
    print(f'{idx}| {campos}: {dados}')

#Alfabeto
alfabeto = list('abcdefg')
print(alfabeto)

idx=0
for letra in alfabeto:
    print(f'{idx} --> {letra}')
    idx += 1
#usando ENUMERATE para o caso acima
for i, letra in enumerate(alfabeto,0):
    print(f'{i} --> {letra}')

#código para mostra uma mensagem informando que não existe o elemento na lista
alfabeto = list('abcdefg')
def encontra_idx(lista, elemento):
    for idx, el in enumerate(lista):
        if el == elemento:
            return idx
    return  print(f"O elemento '{elemento}' não está na lista!")
print(encontra_idx(alfabeto,'k'))

#Usando map() e comparando
numeros= list(range(1,11))
def quadrado(x):
    return x ** 2
map(quadrado, numeros)

#map com função
list(map(quadrado, numeros))

#map com lambda
list(map(lambda  x: x**2, numeros))

#compreesão de lista
[x**2 for x in numeros]

#for normal , com mais linhas de códigos
nova_lista=[]
for x in numeros:
    nova_lista.append(x**2)

print(list(map(quadrado, numeros)), ' --> metodo com função')
print(list(map(lambda  x: x**2, numeros)), ' --> metodo com lambda')
print([x**2 for x in numeros], ' --> metodo com compresao de lista')
print(nova_lista, ' --> metodo normal')
#os códigos acima fazem a mesma coisa

######### usando o método Filter
numeros = [1,2,3,4,5,6,7,8,9,10]

#print(filter(lambda x: x> 5, numeros))

#print(list(filter(lambda x: x>5, numeros)))

#print([x for x in numeros if x >5])

dados = ['0','0.0','b', 'c', '', '', 'f', '', 'h', 'i']

#print(dados) #vai trazer todos os dados, inclusive os aspas fazios
print(list(filter(None, dados))) #tratar os dados, um problema é que o númeral zero ele vai entender como vazio, e em muitos casos não será
#uma forma para tratar isso é usando a seguinte função
def vazio(x):
    if x == '':
        return False
    return True
print(list(filter(vazio, dados)))
##### observação: nessa versão do python ele está tratando os dados, não trazendo os campos em branco e trazendo os campos com zero.

########## trabalhando com REDUCE
from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
print(sum(numeros))
print(reduce(lambda x,y: x*y,numeros))

'''











