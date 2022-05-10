pizza_width = int(input())
cheesiness = int(input())
satisfaction = ''

if pizza_width == 3 and cheesiness >= 95:
    satisfaction = 'absolutely'
elif pizza_width == 1 and cheesiness <= 50:
    satisfaction = 'fairly'
else:
    satisfaction = 'very'

print(f'C.C. is {satisfaction} satisfied with her pizza.')
