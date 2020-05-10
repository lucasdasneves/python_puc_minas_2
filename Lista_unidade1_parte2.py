#!/usr/bin/env python
# coding: utf-8

# # Listas
# - Lista é uma coleção de elementos
# - Cada elemento possui um aposição dentro de uma lista. Essa posição é chamada de índice
# - O primeiro elemento fica aramazenado na posição _0_, enquanto o último elemento fica armazenado na posição _n-1_ (onde _n_ é a quantidade de elementos da lista)
# 
# O que eu irei aprender nessa aula
# 
# 1. - [ ] Como criar uma lista
# - [ ] Como acessar elementos de uma lista
# - [ ] Como modificar elementos de uma lista
# - [ ] Principais métodos de um objeto lista
# - [ ] Funções aplicáveis a uma lista

# ### 1. Como criar uma lista

# In[8]:


# Criando ma lista vazia
lista_vazia = []
lista_vazia2 = list()


# In[10]:


#visualizando o tipo
type(lista_vazia)


# In[11]:


#visualizando o tipo
type(lista_vazia)


# In[12]:


#verificando o tamanho da lista
len(lista_vazia)


# In[16]:


# Criando listas com elementos
lista = [23, 56, 10, 2, 18,0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_strings = ["Rodrigo", "Python", "PUC Minas", "Ciência de Dados e Big Data"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste"]
lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_aninhadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[14]:


# Visualizando a lista
lista


# In[15]:


lista_reais


# In[16]:


lista_strings


# In[17]:


lista_booleanos


# In[18]:


lista_misturada


# In[25]:


lista_misturada2


# In[26]:


listas_aninhadas


# ### 2. Como acessar elementos de uma lista

# In[27]:


# Acessando o índice 0 (primeira posição)
lista[0]


# In[28]:


lista


# In[29]:


lista[2]


# In[30]:


lista_strings[3]


# In[31]:


lista_strings


# In[33]:


lista_misturada[3]


# In[34]:


lista_misturada


# In[36]:


lista_misturada2[4][1]


# In[37]:


lista_misturada2


# In[38]:


lista[20]


# ### 3. Como modificar elementos de uma lista

# In[4]:


# Visualizando a lista
lista


# In[40]:


# Alterando o elemento do índice 1 de 56 para 18
lista[1] = 18


# In[41]:


# Visualizando a alteração realizada
lista


# In[42]:


# Modificando o elemento do índice2. Ele receba a soma dos dois elementos anteriores
lista[2] = lista [0] + lista [1]


# In[43]:


lista


# ### 4. Principais métodos de um objeto lista
# Método | Descrição | Exemplo
# :----- | :-------- | :------
# append | Adiciona um elemento no final da lista | `lista.append(5)`
# clear  | Apaga um elemento no final da lista | `lista.clear()`
# copy | Retorna uma cópia dos elementos da lista | `lista.clear()`
# count | Retorna a quantidade de ocorrências de um elemento na lista | `qt = lista.count(5)`
# extend | Adiciona os elementos de outra lista passada por parâmetro | `lista.extend(outra_lista)`
# index | Retorna o índice do elemento passado por parâmetro (primeira posição) | `pos5 = lista.index(5)`
# insert | Adiciona um elemnto em uma posição passada por parâmetro (provoca um erro caso a posição não exista) | `lista.insert(3, "João")`
# pop | Remove o elemento na posição passada por parâmetro (erro caso a posição não exista) | `elemento = lista.pop()3`
# remove | Remove o elemento passado por parâmetro (erro caso o elemento não exista) | `lista.remove(5)`
# reverse | Inverte a ordem dos elementos de uma lista | `lista.reverse()`
# sort | Ordena os objetos de uma lista | lista.sort()
#       |                               | lista.sort(reverse=True)

# ### 4.1 - append()

# In[6]:


# Visualizando a lista de dados antes da chamada do método append()
lista


# In[7]:


# Adicionando o elemento 17 no final da lista
lista.append(17)


# In[8]:


# Visualizando a lista após a chamada do método append()
lista


# ### 4.2 - clear()

# In[3]:


# Visualizando lista_reais antes da chamada ao método clear()
lista_reais


# In[4]:


# Removendo todos os elementos de lista_reais
lista_reais.clear()


# In[5]:


# Visualizando lista_reais após chamada ao método clear()
lista_reais


# ### 4.3 - copy()

# In[6]:


# Copiando uma lista para outra?
copia = lista


# In[7]:


copia


# In[8]:


# Alterando o elemento do índice 0 de 23 para 5
copia[0] = 5


# In[9]:


# Visualizando o conteúdo de copia
copia


# In[10]:


# VIsualizando o conteúdo de lista (perceba que o elemento 23 também foi alteradona lista, não apenas em copia)
lista


# In[12]:


# Desfazendo a alteração no índice 0, modificando de 5 para 23
lista[0] = 23


# In[19]:


# A maneira correta de copiar uma lista pra outra é através da chamada ao método copy()
copia = lista.copy()


# In[17]:


# Visualizando o conteúdo de lista
lista


# In[20]:


# Visualizando o conteúdo de copia
copia


# In[21]:


# Alterando o elemento do índice 0 de 23 para 5
copia[0] = 5


# In[22]:


# Visualizando o conteúdo de lista
lista


# In[23]:


# Visualizando o conteúdo de lista - Agora sim, apena o índice 0 de copia foi alterado
copia


# ### 4.4 - count()

# In[24]:


# Verificando quantas vezes o número 5 aparece em copia
copia.count(5)


# ### 4.5 - extend()

# In[25]:


# Suponha que temos uma lista chamada numeros que contém os elemento [1, 2, 3]
numeros = [1, 2, 3]


# In[26]:


# Queremos adicionar os elementos [4, 5] à lista números e usamos o método append()
numeros.append([4, 5])


# In[27]:


# Ao invés de adicionarmos os elemtnos 4 e 5, adicionamos uma lista contendo os elementos [4, 5]
numeros


# In[28]:


# A maneira correta de adicionar novos elementos de uma lista, a partis de outra lista, é através d método extend()
numeros = [1, 2, 3]
numeros.extend([4, 5])
numeros


# ### 4.6 - index()

# In[31]:


# Redefinindo os elementos da lista
lista = [1, 3, 7, 2, 3, 8, 4]


# In[33]:


# O método index nos permite saber em que posição determinado elemento está armazenado
lista.index(7)


# In[34]:


# Podemos guardar esse valor em uma variável
posicao8 = lista.index(8)


# In[35]:


posicao8


# In[36]:


# O método index() retorna a posição da primeira ocorrência do elemento procurado.
posicao3 = lista.index(3)


# In[37]:


posicao3


# In[38]:


# Caso o elemento não exista, ocorre um erro
lista.index(19)


# ### 4.7 - insert()

# In[40]:


# O método inset() permite adicionar um elemento em qualquer posição da lista.
# Caso a posição não exista, ele insere o elemento desejado na última posição
lista.insert(2, "ABC")
lista


# In[41]:


lista.insert(100, "XYZ")
lista


# In[42]:


lista.index('XYZ')


# ### 4.8 - pop()

# In[43]:


# Utilizamos o método pop() quando desejamos apagar uma posição da lista
# Removendo o elemento no índice 2
valor = lista.pop(2)


# In[44]:


# Visualizando o valor retornado
valor


# In[45]:


# Removendo o elemento da última posição
lista.pop(-1)
# Visualizando a lista após a remoção
lista


# In[46]:


# O método pop() provoca um erro caso a posição não exista
lista.pop(45)


# ### 4.9 - remove()

# In[47]:


# Utilizamos o metodo remove() quando desejamos apagar um elemento esepcífico da lista
# Visualizando lista_strings antes da remoção
lista_strings


# In[48]:


# Removendo "Rodrigo"
lista_strings.remove("Rodrigo")


# In[49]:


#Visualizando lista_strings após a remoção
lista_strings


# In[50]:


# O método remove() provoca um erro caso o elemento não exista
lista.remove("Java")


# ### 4.11 - sort()

# In[51]:


# Redefinindo os elementos de lista
lista = [6, 3, 1, 4, 2, 5]
# Visualizando a lista antes da chamada ao método sort()
lista


# In[52]:


# Ordenando os elementos em ordem crescente
lista.sort()


# In[53]:


# Visualizando a lista após a chamada ao método sort()
lista


# In[54]:


# Redefinindo os elementos de lista
lista = [6, 3, 1, 4, 2, 5]
# Visualizando a lista antes da chamada ao método sort()
lista


# In[55]:


# Ordenando os elementos em ordem decrescente
lista.sort(reverse=True)


# In[56]:


# Visualizando a lista após a chamada ao método sort()
lista


# In[58]:


# Ordenando lista de caracteres
lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]
lista_letras.sort()
lista_letras


# In[59]:


# Ordenando lista de strings
lista_strings = ["GHI", "XYZ", "DEF", "ABC", "KLM"]
lista_strings.sort()
lista_strings


# In[60]:


# Não é possível ordenar uma lista com elementos de diferentes tipos
lista_misturada = [2, "ABC", 3.14]
lista_misturada.sort()
lista_misturada


# ### 5. Funções aplicáveis a uma lista
# Função | Descriçao | Exemplo
# :------| :-------- | :------
# len | Retorna a quantidade de elementos de uma lista | `print(len(lista))`
# max | Retorna o maior elemento de uma lista | `maior = max(lista)`
# min | Retorna o menor elemento de uma lista | `menor = min(lista)`
# sum | Retorna o somatório dos elementos de uma lista | `soma = sum(lista)`

# In[61]:


# Redefinindo os elementos de lista e lista_letras
lista = [8, 3, 21, 2, 45]
lista_letras = ["Q", "W", "E", "R", "T", "Y", "A", "S", "D"]


# In[62]:


# A função len() retorna a quantidade de elementos de uma lista
len(lista)


# In[63]:


# A função max() retorna o maior elemento de uma lista
max(lista)


# In[64]:


max(lista_letras)


# In[65]:


# A função min() retorna o menor elemento de uma lista
min(lista)


# In[66]:


min(lista_letras)


# In[67]:


# A função sum() retorna a soma dos elementos de uma lista numérica
sum(lista)


# In[ ]:




