
s = 'test_Stringss'
list_s  = [str(i) for i in s]
for i in range(1,len(list_s)-1):
    if list_s[i] == 's':
        list_s[i] = str(list_s[i-1])*2 + str(list_s[i+1])
print(list_s)