import random

def primitive_roots(num):
  roots=[]
  for i in range(2, num):
    mod=[]
    for j in range(1, num):
      if i**j%num not in mod:
        mod.append(i**j%num)
    if len(mod)==num-1:
      roots.append(i)
  return roots

p = int(input('p: '))
g = random.choice(primitive_roots(p))
print("g: ", g)
print()

print('USER 1')
a = int(input('a: '))
xa = (g ** a) % p
print('Xa:', xa)
print('Xa transmitted to USER 2')
print()

print('USER 2')
b = int(input('b: '))
xb = (g ** b) % p
print('Xb:', xb)
print('Xb transmitted to USER 1')
print()

ka = (xb ** a) % p
print('Key for USER 1:', ka)

kb = (xa ** b) % p
print('Key for USER 2:', kb)