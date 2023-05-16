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

primitive_roots(5)