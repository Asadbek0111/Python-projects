person1 = {
    "ism":"Abu Abdulloh Muhammad ibn Ismoil",
    "yil":810,
    "joy":"Buhoro",
    "umr":60,
    "asar":["Al jome' as-sahih", "al-Adab al-mufrad", "al-kabir", "at-tarix as-sag'ir"]
    }
person2 = {
    "ism":"Abdulla Qodiriy",
    "yil":1894,
    "joy":"Toshkent",
    "umr":44,
    "asar":["o'tkan kunlar", "Obid ketmon", "mehrobdan chayon"]
    }
person3 = {
    "ism":"Erkin Vohidov",
    "yil":1936,
    "joy":"Farg'ona",
    "umr":80,
    "asar":["tong nafasi", "qo'shiqlarim sizga", "o'zbegim", "qiziquvchan Matsuma"]
    }
person4 = {
    "ism":"Alisher Navoiy",
    "yil":1441,
    "joy":"Xirot",
    "umr":60,
    "asar":["xamsa", "lison ut-Tayir", "mahbub ul-Qulub", "munojot"]
    }
people = [person1, person2, person3, person4]
for person in people:
    print(f"{person['ism']}ning asarlari:"
          f" {person['asar']}"
          )