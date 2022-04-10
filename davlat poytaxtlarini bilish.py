davalat_poytaxt = {"uzbekistan":"Tashkent", "Rassiya":"Maskva", "Malaysia":"kuala-lampur","aqsh":"washington", "Avg'oniston":"kobul"}
sorov = input("Qaysi davlatning poytaxtini bilishni istaysiz ?: ")
if sorov in davalat_poytaxt.keys():
    print(davalat_poytaxt[sorov])
else:
    print('bizda bundek malumot yoq')