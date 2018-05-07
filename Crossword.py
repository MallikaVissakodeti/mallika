n = int(input("Enter row size : "))
m = int(input("Enter column size : "))
a = []
b = []
l = []
r = [0]*n
print("Enter words and input should be ending with 0")
for i in range(n) :
    r[i] = [0]*m
s = input()
while s != '0' :
    a.append(s)
    s = input()
c = 1
for i in range(0, 1) :
    for j in range(0, m) :
        if a[i][j] != '*' :
            b.append(c)
            c = c + 1
        else :
            b.append(' ')
for i in range(1,n) :
    for j in range(m) :
        if a[i][j] == '*' :
            b.append(' ')
        elif (a[i][j] != '*' and a[i-1][j] == '*' or a[i][j-1] == '*') :
            b.append(c)
            c = c + 1
        elif j == 0 and j < i and a[i][j] != '*' :
            b.append(c)
            c = c + 1
        else:
            b.append('')
count = 0
for i in range(n) :
    for j in range(m) :
        r[i][j] = b[count]
        count = count + 1
print("puzzle#1")
across = {}
print("ACROSS:")
s = ""
for i in range(n):
    for j in range(m):
        if a[i][j] != '*' :
            s = s + str(a[i][j])
        if a[i][j] == '*' and a[i][j - 1] != '*' and j != 0 and j != m - 1 :
            across[r[i][j - len(s)]] = s
            s = ""
        if j == m - 1 and a[i][j] != '*' :
            j = j + 1
            across[r[i][j-len(s)]] = s
            s = ""
        if j == m - 1 and a[i][j] == '*' and a[i][j-1] != '*' :
            across[r[i][j - len(s)]] = s
            s = ""
list1 = across.keys()
for key in list1 :
    print("%s.%s"%(key,across[key]))
print("DOWN:")
s = ""      
down = {}
for j in range(m) :                              
    for i in range(n) : 
        if a[i][j] != '*' :
            s = s + str(a[i][j])
        if (a[i][j] == '*' and i != 0) or i == n - 1 :
            if a[i][j] == '*' and a[i-1][j] != '*' and i != n-1 :
                down[r[i-len(s)][j]] = s
                s = ""
            if i == n - 1 and a[i][j] != '*' :
                i = i + 1
                down[r[i-len(s)][j]] =  s
                s = ""
            if i == n - 1 and a[i][j] == '*' and a[i-1][j] != '*' :
                down[r[i-len(s)][j]] = s
                s = ""
list2 = down.keys()
for key in sorted(list2) :
    print("%s.%s"%(key,down[key]))
