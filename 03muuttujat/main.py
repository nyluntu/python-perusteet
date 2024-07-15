# 03 Muuttujat
#
# Varatut termit, joita ei voi käyttää muuttujien
# nimeämisissä.
#
# and, as, assert, break, class, continue, def, del
# elif, else, except, finally, for, from, global, 
# if, import, in, is, lambda, not, or, pass, raise,
# return, try, while, with, yield
#
# Muuttujien tarkoitus on varastoida tietoa ohjelman
# suorituksen aikana. Muuttuja voi sisältää eri tyyppistä
# tietoa, esimerkiksi numeroita ja merkkijonoja.
#
# Muuttujien tietoja voidaan myös hyödyntää laskemisessa.

# Muuttujan luominen onnistuu esittelemällä ensin sen nimi.
# Tämän jälkeen tulee yhtäsuuri merkki, jota ohjelmointikielessä
# kutsutaan sijoitusoperaattoriksi.
# Yhtäsuuri merkin jälkeen, lainausmerkkien sisälle, voidaan 
# kirjoittaa mitä tahansa tekstiä yhdelle riville.
viesti = "Minä olen merkkijono muotoinen muuttuja."

# print() funktiolla voidaan tulostaa myös muuttujan sisältö
# antamalla muuttuja funktion parametriksi. Parametrilla tarkoitetaan
# jotakin arvoa. Funktioksi kutsutaan sellaista komentoa, jossa
# on sulkeet, kuten print komennossa on.
print("Tulostetaan viesti-muuttujan sisälö:")
print(viesti)

# Muuttuja voi olla myös numeroarvo eli silloin sijoitetaan vain 
# pelkkä numero yhtäsuuri merkin jälkeen. Jos ei käytetä pistettä
# desimaalierottimena niin kyseessä on tällöin kokonaisluku.
numeroarvo = 45

# Merkkijono tyyppinen muuttuja.
tulostuksen_otsikko = "Tulostetaan numeroarvo-muuttuja: "

# print() -funktiolla voi tulostaa myös useita arvoja erottamalla
# ne pilkulla toisistaan.
print(tulostuksen_otsikko, numeroarvo)

# Muuttujien arvoja voidaan laskea myös erilaisilla laskuoperaattoreilla.
# Summa (+)
# Erotus (-)
# Jako (-)
# Kerto (*)

# Ensin muuttujan ikä arvoksi asetetaan 30.
ika = 30
# ika muuttujaan lisätään luku 13 ja sitten se sijoitetaan
# uudelleen ika nimiseen muuttujaan. Tällöin vanha alkuperäinen
# arvo 30 korvautuu.
ika = ika + 13
# Tulostetaan ika muuttuja.
print("Henkilön ikä on: ", ika)

# Huomaa tässä print() -funktion tulostama viestin sisältö.
# viesti -muuttuja on asetettu ohjelman alussa jo ja sen arvo
# on "Minä olen merkkijono muotoinen muuttuja."
viesti = viesti + str(500)
# Viestin perään tulostuu luku 500.
print(viesti)

# Usea merkkijono muuttuja voidaan yhdistää + merkillä.
esine1 = "Omena"
esine2 = "Banaani"
esine3 = "Päärynä"

# Tulostetaaan kolme eri muuttujaa ja muotoillaan ne pilkulla
# erotetuiksi.
kokonainen_viesti = esine1 + ", " + esine2 + ", " + esine3
print("Tulostetaan kokonainen viesti: ", kokonainen_viesti)