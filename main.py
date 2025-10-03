import hashlib

password = "passwort"
block1 = list(password[:len(password)//2])
block2 = list(password[len(password)//2:])
multiplier = []
mul = 1
total = 0
sum_list = []

encoded_password = password.encode()
hash_value = hashlib.sha256(encoded_password)

for i in range(len(block1)):
    if i % 4 == 0:
        mul = 1
    else:
        mul = mul * 64
    multiplier.append(mul)
    total += ord(block1[i]) * mul
    sum_list.append(total)

for x, y, z in zip(block1, multiplier, sum_list):

    print(f"{x} | Ascii {ord(x)} | M {y} | Ascii*M: {ord(x)*y} | Hash: {z} | Hexadecimal: {hex(z)}")

total_block2 = total
for x, y, z in zip(block2, multiplier, sum_list):
    total_block2 += ord(x) * y
    print(f"{x} | Ascii {ord(x)} | M {y} | Ascii*M: {ord(x)*y} | Hash: {total_block2} "
          f"| Hexadecimal: {hex(total_block2)}")


