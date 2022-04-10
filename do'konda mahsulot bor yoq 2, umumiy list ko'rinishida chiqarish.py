mahsulotlar = ["un", "moy", "piyoz", "banan", "kartoshka", "apelsin", "olma", "qulpinoy", "anor", "anjir" ]
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} mahsulotni qo'shing: "))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
s = len(mavjud_emas)
if s > 0 :
    print(f"Quyidagi mahsulotlar do'konimizda yo'q: \n {mavjud_emas}")
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")