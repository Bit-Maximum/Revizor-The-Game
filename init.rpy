# Определение переменных
define dolg = -1000
define stelth = 0

# Определение персонажей игры.
define n = Character(None, kind=nvl)
define a = Character(callback=name_callback, cb_name=None)

define servant = Character('Осип, слуга', color="#b36822", image='servant', callback=name_callback, cb_name="servant")
define khlestakov = Character('Иван Хлестаков, чиновник', color="#c92222", image='khlestakov', callback=name_callback, cb_name="khlestakov")

define tavern = Character('Трактирный слуга', color="#328817", image='tavern', callback=name_callback, cb_name="tavern")

define mayor = Character('Антон Сквозник-Дмухановский, городничий', color="#dfd21f", image='mayor', callback=name_callback, cb_name="mayor")
define judge = Character('Аммос Ляпкин-Тяпкин, судья', color="#c8ffc8", image='judge', callback=name_callback, cb_name="judge")
define trustee = Character('Артемий Земляника, попечитель богоугодных заведений', color="#fc950f", image='trustee', callback=name_callback, cb_name="trustee")
define caretaker = Character('Лука Хлопов, смотритель училищ', color="#328817", image='caretaker', callback=name_callback, cb_name="caretaker")

define bobchin = Character('Пет`р Иванович Бобчинский, городской помещик', color="#fc950f", image='bobchin', callback=name_callback, cb_name="bobchin")
define dobchin = Character('Петр Иванович Добчинский, городской помещик', color="#b36822", image='dobchin', callback=name_callback, cb_name="dobchin")
define postmen = Character('Иван Шпекин, почтмейстер', color="#b36822", image='postmen', callback=name_callback, cb_name="postmen")

define trademen = Character('Купец', color="#b36822", image='trademen', callback=name_callback, cb_name="trademen")

define wife_m = Character('Анна Андреевна, жена городничего', color="#fc950f", image='wife_m', callback=name_callback, cb_name="wife_m")
define child_m = Character('Марья Антоновна, дочь городничего', color="#b36822", image='child_m', callback=name_callback, cb_name="child_m")

define poshlepkina = Character('Февронья Пошлепкина, слесарша', color="#328817", image='poshlepkina', callback=name_callback, cb_name="poshlepkina")
define wife_o = Character('Жена унтер-офицера', color="#c8ffc8", image='wife_o', callback=name_callback, cb_name="wife_o")

define cop = Character('Жандарм', color="#d42316", image='cop', callback=name_callback, cb_name="cop")
define officer = Character('Степан Уховертов, частный пристав.', color="#881f17", image='officer', callback=name_callback, cb_name="officer")

# Определение спрайтов персонажей.
# Спрайты Слуги.
image servant normala = At("servant normal", sprite_highlight('servant'))
image servant feara = At("servant fear", sprite_highlight('servant'))
image servant halloa = At("servant hallo", sprite_highlight('servant'))
image servant happya = At("servant happy", sprite_highlight('servant'))
image servant sada = At("servant sad", sprite_highlight('servant'))
image servant warminga = At("servant warming", sprite_highlight('servant'))

# Спрайты Хлестакова.
image khlestakov normala = At("khlestakov normal", sprite_highlight('khlestakov'))
image khlestakov angreea = At("khlestakov angree", sprite_highlight('khlestakov'))
image khlestakov discustinga = At("khlestakov discusting", sprite_highlight('khlestakov'))
image khlestakov lovefulla = At("khlestakov lovefull", sprite_highlight('khlestakov'))
image khlestakov ragea = At("khlestakov rage", sprite_highlight('khlestakov'))
image khlestakov spechlessa = At("khlestakov spechless", sprite_highlight('khlestakov'))
image khlestakov surea = At("khlestakov sure", sprite_highlight('khlestakov'))
image khlestakov surprisea = At("khlestakov surprise", sprite_highlight('khlestakov'))

# Спрайты Трактирного слуги.
image tavern normala = At("tavern normal", sprite_highlight('tavern'))
image tavern angreea = At("tavern angree", sprite_highlight('tavern'))
image tavern carefulla = At("tavern carefull", sprite_highlight('tavern'))
image tavern happya = At("tavern happy", sprite_highlight('tavern'))
image tavern ragea = At("tavern rage", sprite_highlight('tavern'))

# Спрайты Купца.
image trademen normala = At("trademen normal", sprite_highlight('trademen'))
image trademen carefulla = At("trademen carefull", sprite_highlight('trademen'))
image trademen happya = At("trademen happy", sprite_highlight('trademen'))


# Спрайты Слесарши.
image poshlepkina normala = At("poshlepkina normal", sprite_highlight('poshlepkina'))
image poshlepkina angreea = At("poshlepkina angree", sprite_highlight('poshlepkina'))
image poshlepkina sada = At("poshlepkina sad", sprite_highlight('poshlepkina'))

# Спрайты жены офицера.
image wife_o normala = At("wife_o normal", sprite_highlight('wife_o'))
image wife_o happya = At("wife_o happy", sprite_highlight('wife_o'))


# Спрайты Городничего.
image mayor normala = At("mayor normal", sprite_highlight('mayor'))
image mayor angreea = At("mayor angree", sprite_highlight('mayor'))
image mayor happya = At("mayor happy", sprite_highlight('mayor'))
image mayor ragea = At("mayor rage", sprite_highlight('mayor'))
image mayor sada = At("mayor sad", sprite_highlight('mayor'))

# Спрайты Судьи.
image judge normala = At("judge normal", sprite_highlight('judge'))
image judge carefulla = At("judge carefull", sprite_highlight('judge'))
image judge happya = At("judge happy", sprite_highlight('judge'))
image judge speechlessa = At("judge speechless", sprite_highlight('judge'))
image judge surpruseda = At("judge surprused", sprite_highlight('judge'))

# Спрайты Попечителя.
image trustee normala = At("trustee normal", sprite_highlight('trustee'))
image trustee angreea = At("trustee angree", sprite_highlight('trustee'))
image trustee feara = At("trustee fear", sprite_highlight('trustee'))
image trustee happya = At("trustee happy", sprite_highlight('trustee'))
image trustee sada = At("trustee sad", sprite_highlight('trustee'))
image trustee surpriseda = At("trustee surprised", sprite_highlight('trustee'))

# Спрайты Смотрителя.
image caretaker normala = At("caretaker normal", sprite_highlight('caretaker'))
image caretaker discustinga = At("caretaker discusting", sprite_highlight('caretaker'))
image caretaker happya = At("caretaker happy", sprite_highlight('caretaker'))
image caretaker speechlessa = At("caretaker speechless", sprite_highlight('caretaker'))
image caretaker surpriseda = At("caretaker surprised", sprite_highlight('caretaker'))


# Спрайты почтальона.
image postmen normala = At("postmen normal", sprite_highlight('postmen'))
image postmen angreea = At("postmen angree", sprite_highlight('postmen'))
image postmen happya = At("postmen happy", sprite_highlight('postmen'))
image postmen sada = At("postmen sad", sprite_highlight('postmen'))

# Спрайты Бобчинского.
image bobchin normala = At("bobchin normal", sprite_highlight('bobchin'))
image bobchin discustinga = At("bobchin discusting", sprite_highlight('bobchin'))
image bobchin happya = At("bobchin happy", sprite_highlight('bobchin'))
image bobchin ragea = At("bobchin rage", sprite_highlight('bobchin'))
image bobchin surpriseda = At("bobchin surprised", sprite_highlight('bobchin'))

# Спрайты Добчинского.
image dobchin normala = At("dobchin normal", sprite_highlight('dobchin'))
image dobchin carefulla = At("dobchin carefull", sprite_highlight('dobchin'))

# Спрайты жены городничего.
image wife_m normala = At("wife_m normal", sprite_highlight('wife_m'))
image wife_m carefulla = At("wife_m carefull", sprite_highlight('wife_m'))
image wife_m happya = At("wife_m happy", sprite_highlight('wife_m'))
image wife_m playfulla = At("wife_m playfull", sprite_highlight('wife_m'))
image wife_m sada = At("wife_m sad", sprite_highlight('wife_m'))

# Спрайты дочери городничего.
image child_m normala = At("child_m normal", sprite_highlight('child_m'))
image child_m discantinga = At("child_m discanting", sprite_highlight('child_m'))
image child_m happya = At("child_m happy", sprite_highlight('child_m'))
image child_m sada = At("child_m sad", sprite_highlight('child_m'))

# Спрайты полицейского.
image cop normala = At("cop normal", sprite_highlight('cop'))

# Спрайты пристава.
image officer normala = At("officer normal", sprite_highlight('officer'))
image officer sada = At("officer sad", sprite_highlight('officer'))


# Определение фоновых изображений.
image bg_house = "bg/mayor_house.png" 
image bg_city = "bg/city.png" 
image bg_hotel = "bg/hotel.png" 

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Определение положений спрайтов
init:
    $ left2 = Position(xalign=0.2, yalign=1.0)
    $ left3 = Position(xalign=0.35, yalign=1.0)
    $ right2 = Position(xalign=0.8, yalign=1.0)
    $ right3 = Position(xalign=0.6, yalign=1.0)