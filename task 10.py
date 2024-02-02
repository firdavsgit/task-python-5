
name_dub = input("enter name:")
name = ["Firdavs", "Shuhrat", "Sardor"]

i = 0

while i < len(name):
    x = name[i]
    i += 1
    if x == name_dub:
        name.remove(x)
        print(name)





