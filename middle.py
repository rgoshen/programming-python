bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())
middle_bowl = 0

if (bowl1 >= bowl2 and bowl1 <= bowl3) or (bowl1 <= bowl2 and bowl1 >= bowl3):
    middle_bowl = bowl1
elif (bowl2 >= bowl1 and bowl2 <= bowl3) or (bowl2 <= bowl1 and bowl2 >= bowl3):
    middle_bowl = bowl2
elif (bowl3 >= bowl1 and bowl3 <= bowl2) or (bowl3 <= bowl1 and bowl3 >= bowl2):
    middle_bowl = bowl3

print(middle_bowl)
