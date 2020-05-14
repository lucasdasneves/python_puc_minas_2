#!/usr/bin/env python
# coding: utf-8

# # Tuplas
# 
# - Assim como uma lista, uma tupla também é uma coleção de elementos. A diferença entre elas é que a tupla é imutável. Ou seja, uma vez definidos os seus elementos, a tupla não pode mais ser alterada
# - Cada elemento possui uma posição dentro de uma lista. Essa posição é chamada de índice
# - O primeiro elemento fica armazenado na posição zero ( 0 ), enquanto o último elemento fica armazenado na posição _n-1_ (onde _n_ é a quantidade de elementos da lista)
# 
# O que veremos nessa aula:
# 
# 1. Como criar uma tupla
# 2. Como acessar elementos de uma tupla
# 3. A mutabilidade de uma tupla
# 4. Principais métodos de um objeto tupla
# 5. Funções aplicáveis a uma tupla
# 6. Convertendo uma tupla em uma lista

# ### 1. Como criar uma tupla

# In[1]:


# Criando tuplas vazias
tupla_vazia = ()
tupla_vazia = tuple()


# In[2]:


# Verificando o tipo de tupla_vazia
type(tupla_vazia)


# In[5]:


# Verificando se tupla_vazia2 é uma instância de tuple
isinstance(tupla_vazia, tuple)


# In[6]:


# Para saber a qtd de elementos da tupla
len(tupla_vazia)


# In[2]:


# Criando tuplas com elementos
tupla1 = (3, 19, 4, 21, 3, 5, 13)
tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla",(1, 2, 3))
tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla", [1, 2, 3])


# In[10]:


# Visualizando os elementos de tupla1
tupla1


# In[11]:


# Visualizando os elementos de tupla2
tupla2


# In[13]:


# Visualizando os elementos de tupla3
tupla3


# ### 2. Como acessar elementos de uma tupla

# In[14]:


# Acessando o índdice 0 (primeira posição) de tupla1
tupla1[0]


# In[15]:


# Visualizando os elementos de tupla1
tupla1


# In[17]:


# Acessando o índice 5 (sexta posição) de tupla2
tupla2[5]


# In[18]:


# Visualizando os elementos de tupla2
tupla2


# In[19]:


# Acessando o índice 8 (nona posição) de tupla3
tupla3


# In[20]:


# Tentando acesso a um índice inexistente
tupla3[20]


# ### 3. A imutabilidade de uma tupla

# In[3]:


# Atribuindo o valor 5 ao índice 0 de tupla1 provocará um erro
tupla1[0] = 5


# In[4]:


# O mesmo ocorre se tentarmos atribuir o string "imutável" para o índice 1 de tupla2
tupla2[1] = "imutável"


# In[6]:


# O índice 8 de tupla2 contém uma outra tupla contendo 3 valores (1, 2, 3).
# Tentar atribuir 5 ao índice 1 dessa tupla interna, provocará um erro de execução
tupla3[8][1] = 5


# In[7]:


tupla3


# In[8]:


# Podemos adicionar elementos à lista armazenada no índice 8 da tupla
tupla3[8].extend([4, 5, 6])


# In[9]:


tupla3


# In[10]:


# Entretanto, mantendo a característica de imutabilidade, não podemos subsituir a lista do índice 8 por outra
tupla3[8] = [-1, -2, -3]


# ### 4. Principais métodos de um objeto tupla

# In[11]:


# Verificando quantas vezes o número 3 aparece em tupla1
tupla1.count(3)


# In[12]:


tupla1


# In[13]:


#Verificando em que posição está armazendo o elemento 21
tupla1.index(21)


# ### 5. Funções aplicáveis a uma tupla

# In[14]:


len(tupla1)


# In[15]:


max(tupla1)


# In[16]:


min(tupla1)


# In[17]:


sum(tupla1)


# ### 6. Convertendo uma tupla em lista

# In[18]:


lista = list(tupla1)


# In[19]:


lista


# In[20]:


tupla1[6] = -1 # A imutabilidade da tupla não permite a alteração de um valor


# In[21]:


lista[6] = -1 # A lista resultante da conversão da lista permite a alteração


# In[22]:


lista


# In[ ]:




