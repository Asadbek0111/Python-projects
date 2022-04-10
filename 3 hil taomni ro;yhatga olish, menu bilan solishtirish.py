menu = {"osh":25000,
        "manti":5000,
        "somsa":6000, 
        "sho'rva":25000, 
        "shashlik":12000
        }
print("3 ta taomga buyurtma bering: ")
orders = []
for n in range(3):
    orders.append(input(f"{n+1}-buyurtmani kiriting:").lower())
for order in orders:
    if order in menu:
        print(f"{order.title()} - {menu[order]} so'm")
    else:
        print(f"{order.title()} - menuda yo'q")
    