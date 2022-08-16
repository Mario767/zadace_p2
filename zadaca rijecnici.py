import random

lista = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']
novi = {}

for ime in lista:
    if ime not in novi:
        i = random.randint(1,5)
        novi[ime] = i
print(novi)

jedan = 0
dva = 0
tri = 0
cetiri = 0
pet = 0
ukupno = 0



for i in novi:
    ukupno += 1
    
    if novi[i] == 1:
        jedan += 1
    if novi[i] == 2:
        dva += 1
    if novi[i] == 3:
        tri += 1
    if novi[i] == 4:
        cetiri += 1
    if novi[i] == 5:
        pet += 1
prolaznost = round(((dva+tri+cetiri+pet)/ukupno),2)
print("ukupno ",ukupno)
print("Ima:",jedan,"ocjene 1")
print("Ima:",dva,"ocjene 2")
print("Ima:",tri,"ocjene 3")
print("Ima:",cetiri,"ocjene 4")
print("Ima:",pet,"ocjene 5")
print("Prolaznost je :",prolaznost*100,"%")
    
