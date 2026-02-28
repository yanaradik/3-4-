a = int(input("введите место:"))
if a % 2 == 0 and a<37:
    print("верхнее в купе")
elif a % 2 != 0 and (a<37):
    print("нижнее в купе")
elif a % 2 == 0 and a>37:
    print("верхнее боковое")
else:
    print("нижнее боковое")

