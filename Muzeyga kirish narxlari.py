yosh = int(input("Yoshingizni kiriting: "))

if yosh<= 4 or yosh>=60:
    narx = "Siz uchun bepul :)"
elif yosh < 18:
    narx = "10.000so'm"
else:
    narx = "20.000so'm"
print(narx)