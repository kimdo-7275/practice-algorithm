num = int(input())
distance = 1
max_room = 1
while num > max_room:
    max_room += 6*distance
    distance += 1

print(distance)