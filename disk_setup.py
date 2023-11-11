from random import randint
ALPHABET = "qwertyuiopasdfghjklzxcvbnm"

alphabet_left = [x for x in ALPHABET]
alphabet_right = [x for x in ALPHABET]
left_disk = []
right_disk = []
for _ in range(26):
    index_left = randint(0, len(alphabet_left) - 1)
    index_right = randint(0, len(alphabet_right) - 1)
    left_disk.append(alphabet_left.pop(index_left))
    right_disk.append(alphabet_right.pop(index_right))
print(left_disk)
print(right_disk)