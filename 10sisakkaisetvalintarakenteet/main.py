# 10 Sisäkkäiset valintarakenteet
#
# Tutustutaan harjoituksissa seuraaviin valintarakenteisiin:
#
# - if
# - if-else
# - if-elif
# - if-elif-else
#
# VERTAILUOPERAATTORI
# < pienempi kuin
# > suurempi kuin
# == yhtäsuuri
# <= pienempi tai yhtäsuuri kuin
# >= suurempi tai yhtäsuuri kuin

print("Kerro sinun ikäsi kokonaislukuna?")
henkilon_ika = input()
henkilon_ika = int(henkilon_ika)

if henkilon_ika <= 2:
  # Toteutuu jos luku on pienempi tai yhtäsuuri kuin 2
  print("Vauva")

  if henkilon_ika < 10:
    # Toteutuu jos luku on suurempi kuin 2 ja pienempi kuin 10
    print("Lapsi")

    if henkilon_ika == 10:
      # Toteutuu jos luku on yhtäsuuri kuin 10
      print("Olen kymmenen vuotta.")

      if henkilon_ika < 18:
        # Toteutuu jos luku on suurempi kuin 10 ja pienempi kuin 18
        print("Ei täysi ikäinen")
      else:
        # Toteutuu jos luku on suurempi kuin 18
        print("Nuori aikuinen")
