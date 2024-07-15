# 05 Tietotyypit Python ohjelmointikielissä
#
# TIETOTYYPIT
#
# Pääasiassa seuraavat tietotyypit on hyvä tuntea,
# koska ne vaikuttavat ohjelman toimintaan ja laskutoimituksiin.
#
# Merkkijono = string, str
# Kokonaisluku = integer, int
# Liukuluku/Desimaalit = float 
# Kokoelmat/Listat = list
#
# OPERAATTORIT
#
# + yhteenlasku
# - vähennyslasku
# * kertolasku
# / jakolasku
# % jakojäännös (modulo)
# // jakolasku (pyöristaa kokonaismäärään, tasajako)
# ** potenssilasku
#
# TYYPPIMUUNNOKSET
#
# merkkijono = str()
# kokonaisluku = int()
# liukuluku = float()
#
# LASKUSÄÄNNÖT
#
# 1	Sulkeet
# 2	Eksponentti
# 3	Kerto
# 4	Jako
# 5	Summa
# 6	Erotus


# Merkkijonoilla (kutsutaan string) tarkoitetaan mitä tahansa tekstimuotoista sisältöä.
# Kaikki numeropohjainen tietokin voidaan esittää tekstimuotoisena
# ohjelman näkökannalta.
# Voidaan ajatella myös tietoa mikä ei ole laskettavissa.

nimi = "Matti Mallikas"
syntymaaika = "20.9.1988"
postinumero = "00150"
puhelinnumero = "04012383929"
auton_merkki = "Toytota"
auton_vari = "Sininen"

# Kokonaislukua kutsutaan integer termillä. Ei sisällä desimaaleja ja
# voidaan käyttää erilaisissa laskutoimituksissa. Ei voi alkaa nollalla
# ja etunollat tippuvt tyyppimuunnoksessa pois.

ika = 31
henkilon_pituus = 181
ovien_lukumaara = 3
# postinumero = 00150
# puhelinnumero = 04012383929
# puhelinnumero_vaarin = int(puhelinnumero)
# print("Puhelinnumero on:", puhelinnumero_vaarin)

# postinumero_vaarin = int(postinumero)
# print("Postinumero on:", postinumero_vaarin)


# Liukulukua kutsutaan float termillä. On desimaalilukuinen arvo ja 
# voidaan myös käyttää erilaisissa laskutoimituksissa. Jos lasketaan
# kokonaislukua ja liukulukua niin pythonissa tulos käyttää
# aina tarkinta muotoa.

paino_kiloissa = 74.8
moottorin_tilavuus = 1.6

# Lasketaan painoindeksi
# painoindeksi = paino / pituus^2

henkilon_paino_kiloissa = 84
henkilon_pituus_metreissa = 1.85

painoindeksi = henkilon_paino_kiloissa / henkilon_pituus_metreissa ** 2

# painoindeksi = henkilon_paino_kiloissa / henkilon_pituus_metreissa / henkilon_pituus_metreissa

# print("1) Painoindeksi on:", int(painoindeksi))
# print("2) Painoindeksi on:", round(painoindeksi, 2))
# print("3) Painoindeksi on:", "{:.6f}".format(painoindeksi))

# Painoindeksin laskeminen mutta kun syotteet
# ovat annettu merkkijonoina.

henkilon_paino_kiloissa = float("84")
henkilon_pituus_metreissa = float("1.85")

painoindeksi = henkilon_paino_kiloissa / henkilon_pituus_metreissa ** 2
#print("4) Painoindeksi on:", round(painoindeksi, 2))

merkkijono1 = "Ykkönen"
merkkijono2 = "Kakkonen"
merkkijono3 = "kolmonen"
merkkijono4 = "Nelonen"

print(merkkijono1 + merkkijono2 + merkkijono3)
print(merkkijono4 * 5)