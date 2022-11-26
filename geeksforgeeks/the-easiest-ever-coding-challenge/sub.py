s = "WomensDAY"

count = 0
st = []
count_u = 0
count_l = 0

sub = ""
j = 0
for i in range(len(s)):
    if ord(s[i]) >= 97 and count_u == count_l:
        print(s[i])
        sub = sub + s[i]
        
    if ord(s[i]) <= 96 and count_u == count_l:
        print(s[i])
        sub = sub + s[i]
        
    j=j+1

    if j >= 2 and count_u != count_l:
        st.append(sub)
        sub = ""
        j = 0
        count_l =0
        count_u =0
            
print(st)