
# a)
def S(n):
  if (n >= 2):
    return S(n-1) + 10
  elif (n == 1):
    return 10
n = 0
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))
resultado_final = S(n)
print(f"O resultado de algoritmo recursivo é {resultado_final}")

# b)
def A(n):
  if (n >= 2):
    return A(n-1) ** -1
  elif (n == 1):
    return 2
n = 0
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))
resultado_final = A(n)
print(f"O resultado de algoritmo recursivo é {resultado_final}")

# c)
def B(n):
  if (n >= 2):
    return B(n-1) + n ** 2
  elif (n == 1):
    return 1
n = 0
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))
resultado_final = B(n)
print(f"O resultado de algoritmo recursivo é {resultado_final}")

#d)
def P(n):
  if (n >= 2):
    return (n ** 2) * P(n-1) + (n-1)
  elif (n == 1):
    return 1
n = 0
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))
resultado_final = P(n)
print(f"O resultado de algoritmo recursivo é {resultado_final}")

# e)
def letraE(n):
  if n==1:
      return 3
  elif n == 2:
      return 5
  elif n > 2:
      return (n - 1) * letraE(n - 1) + (n - 2) * letraE(n - 2)
n = -1
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))

# f)
resultado_final = letraE(n)
print(f'O resultado do algoritimo recursivo é {resultado_final}')
def letraF(n):
  if n==1:
      return 2
  elif n == 2:
      return 5
  elif n > 2:
      return letraF(n - 1) * letraF(n - 2)
n = -1
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))

# g)
resultado_final = letraF(n)
print(f'O resultado do algoritimo recursivo é {resultado_final}')
def letraG(n):
  if n == 1:
      return 1
  elif n == 2:
      return 2
  elif n == 3:
      return 3
  else:
      return letraG(n - 1) + 2 * letraG(n - 2) + 3 * letraG(n - 3)
n = 0
while n <= 0:
  n = int(input("Digite um valor maior que 0 para n: "))
resultado_final = letraG(n)
print(f'O resultado do algoritmo recursivo é {resultado_final}')

## 2

# F(1) = a1
# F(n) = a1 * r^(n - 1) para n > 1
# Nessa definição recursiva, F(n) representa o termo geral, a1 representa o valor inicial,
# r representa a razão e n representa a posição do termo. O símbolo "^" está representando
# Potenciação.


## 3
def T(n):
  if n == 2:
      return True
  if n > 2 and (T(n-3) or T(n/2)):
      return True

  return False

print(T(6))
print(T(7))
print(T(19))
print(T(12))

## 4
def funcao(n):
  if n == 2 or n ==3:
      return True
  elif n < 2:
      return False
  else:
      return funcao(n - 2) or funcao(n - 3)

n = int(input("Digite um valor para n: "))


if funcao(n) == True:
  print(f'{n} pertence a M')
elif funcao(n) == False:
  print(f'{n} não pertence a M')

## 5
def S(n):
  if n == 'a' or n == 'b':
      return True
  if len(n) >= 2 and n[-1] == 'b' and n != 'b' and S(n[:-1]):
      return True

  return False

print(S('a'))
print(S('ab'))
print(S('aba'))
print(S('aaab'))
print(S('bbbbb'))

## 7

# B(0) = 1
# B(n) = 2*B(n-1)

# Para cada 1 adicionado, o resultado é 2 vezes o anterior, o que significa que o mesmo será 
# F(n) será sempre ímpar.

## 8

#a
def a(n):
    return a(n * 3)
a(1)
#b
def b(x):
    return b(x / 2)
b(2)
#c
def c(a, b):
    print(a)
    c(a + b)
#d
def d(p, q):
    print(p)
    d(p - q)
    d(p + q)










