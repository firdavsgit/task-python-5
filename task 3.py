shu_masalani_n = int(input("Sonni kiriting: "))
result = []
i = 1

while i <= shu_masalani_n:
    if i % 4 == 0:
        amplified_number = 10 * i
        result.append(amplified_number)
    else:
        result.append(i)
    i += 1

print("Natija:", result)