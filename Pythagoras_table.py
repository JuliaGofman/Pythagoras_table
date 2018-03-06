a, b, c, d = int(input()), int(input()), int(input()), int(input())
for i in range(c, d+1):
  print('\t', i, end=' ')
for j in range(a, b+1):
    print()
    print(j, end='\t')
    for n in range(c, d+1):
        print(j*n, end='\t')