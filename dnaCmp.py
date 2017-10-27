#Name: Neil Felix
#Date: 10/17
#Info: ask user for DNA string out puts its complement

dnaStr = input('Enter DNA: ')
dnaComp = ""
for i in dnaStr:
    if i == 'A':
        dnaComp += 'T'
    elif i == 'C':
        dnaComp += 'G'
    elif i == 'G':
        dnaComp += 'C'
    elif i == 'T':
        dnaComp += 'A'

print('The complementary strand is ' +  dnaComp)
