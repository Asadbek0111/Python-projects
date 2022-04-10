python_izohli_lugati = {
    "integer":"Butun son",
    "float":"O'nlik son",
    "string":"Matn",
    "list":"Ro'yhat",
    "tuple":"O'zgarmas ro'yhat"
    }
sorov = input("So'z kiriting: ").lower()
javob = python_izohli_lugati.get(sorov)
if javob == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{sorov.title()} so'zi {javob} deb tarjima qilinadi")