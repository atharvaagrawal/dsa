s = str(num)
n = '9'*len(s)

if n == str(num):
    return num

num = [i for i in str(num)] 

# print(num[0])

for i in range(len(num)):
    if num[i] != '9':
        num[i] = '9'
        break

s = ""
s = s.join(num)

return int(s)

