
'''
x = input('>> ').split()
for i in range(len(x)):
    x[i] = int(x[i])
print(x)
'''

x = list(map(int, input('>> ').split()))
x.sort(reverse=True)
print(x)
