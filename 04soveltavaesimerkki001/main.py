# 04 Automatkan hinnan laskeminen
#
# Sovelletaan tähän asti opittua.
# - Tulostaminen
# - Kommentointi
# - Muuttujat

# Luodaan yksinkertainen ohjelma laskemaan automatkan
# hinta perustuen annettuihin arvoihin.

# Matkan kokonaishinta lasketaan seuraavalla kaavalla.
# (matkanpituus, km / 100) x kulutus x litrahinta
matkanpituus_kilometreina = 689
kulutus_litroina = 6.6
litrahinta_euroina = 1.59

matkan_kokonaishinta = (matkanpituus_kilometreina / 100) * kulutus_litroina * litrahinta_euroina

print("Matka tulee maksamaan: ", int(matkan_kokonaishinta), " euroa")


