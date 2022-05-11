password = input()
lower_count = 0
upper_count = 0
digit_count = 0
output = 'Invalid'
isValid = True

if len(password) > 7 and len(password) < 13:
    for char in password:
        if char.isalpha() or char.isdigit():
            if char.islower() == True:
                lower_count += 1
            elif char.isupper() == True:
                upper_count += 1
            else:
                digit_count += 1
        else:
            isValid = False
            break

if isValid and (lower_count >= 3 and upper_count >= 2 and digit_count >= 1):
    output = 'Valid'

print(output)
