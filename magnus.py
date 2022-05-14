word = input().upper()
block = 'HONI'
output = [''] * 4
count = 0

for i in range(len(word)):
    if word[i] == block[0] and output[0] == '':
        output[0] = word[i]
    elif word[i] == block[1] and output[1] == '' and output[0] != '':
        output[1] = word[i]
    elif word[i] == block[2] and output[2] == '' and output[1] != '':
        output[2] = word[i]
    elif word[i] == block[3] and output[3] == '' and output[2] != '':
        output[3] = word[i]
    else:
        continue

    if all(output):
        count += 1
        output = [''] * 4

print(count)
