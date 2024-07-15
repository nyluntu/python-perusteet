# 06 Syötteen vastaanottaminen
#
# Syötteella tarkoitetaan tässä osiossa ohjemalle annettavaa
# arvoa sen käyttäjän toimesta.

print("Ohjelma odottaa nimeäsi. Kirjoita nimi ja paina ENTER.")
# Pythonin sisäänrakennettu input() -funktion kutsuminen odotttaa
# syötettä käyttäjältä.
henkilon_nimi = input()
print("Nimesi on", henkilon_nimi)

print("Kiitos! Kerrotko vielä pituutesi metreinä.")
henkilon_pituus = input()
print("Sinun pituus on", henkilon_pituus, "metriä")

# Kun syöte annetaan, on aina hyvä suorittaa tyyppimuunnos.
# Syöte on aina oletuksena merkkijono huolimatta siitä antaako
# käyttäjä numeroarvon vai ei. Siksi jos tiedät tarvitsevasi 
# annettua arvoa laskemiseen, tee aina tyyppimuunnos.
# Esimerkissä on käytetty float() kutsua, joka muuttaa 
# syötetyn arvon liukulukutyyppiseksi.
henkilon_pituus = float(henkilon_pituus) + 0.5
print("Sinun pituus on", henkilon_pituus, "metriä")