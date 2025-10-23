s1 = input("Enter the string of 0's and 1's as subunit1: ")
s2 = input("Enter the string of 0's and 1's as subunit2: ")

# Pad shorter string with zeros
max_len = max(len(s1), len(s2))
s1 = s1.zfill(max_len)[::-1]
s2 = s2.zfill(max_len)[::-1]

res = ""
c = '0'
for i, j in zip(s1, s2):
    if i == '0' and j == '0' and c == '0':
        res += '0'
        c = '0'
    elif i == '0' and j == '0' and c == '1':
        res += '1'
        c = '0'
    elif i == '0' and j == '1' and c == '0':
        res += '1'
        c = '0'
    elif i == '0' and j == '1' and c == '1':
        res += '0'
        c = '1'
    elif i == '1' and j == '0' and c == '0':
        res += '1'
        c = '0'
    elif i == '1' and j == '0' and c == '1':
        res += '0'
        c = '1'
    elif i == '1' and j == '1' and c == '0':
        res += '0'
        c = '1'
    elif i == '1' and j == '1' and c == '1':
        res += '1'
        c = '1'
if c == '1':
    ans = ""
    for i in res:
        if i == '1' and c == '1':
            ans += '0'
            c = '1'
        elif i == '0' and c == '0':
            ans += '0'
            c = '0'
        else:
            ans += '1'
            c = '0'
    res = ans
final = ""
for i in res:
    if i == '1':
        final += '0'
    else:
        final += '1'

print("Checksum of two subunits: ", final[::-1].strip())
