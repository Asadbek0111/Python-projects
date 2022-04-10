mahsulotlar = ["banan", "olma", "apelsin", "anjir", "shaptoli", "o'rik", "pamidor", "anor", "uzum", "gilos", "mango"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konimizda {mahsulot} bor!")
    else:
        print(f"Do'konimizda {mahsulot} yo'q -_-")