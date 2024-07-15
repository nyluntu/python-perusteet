# 09 Valintarakenteet ja vertailuoperaattorit
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
#
# BOOLEAN tietotyyppi
# 
# Voi olla True tai False. Päällä tai pois. 1 tai 0.

print("Kerro ostostesi loppusumma:")
ostokset_yhteensa = input()
ostokset_yhteensa = float(ostokset_yhteensa)

pankkitilin_saldo = 1400
saa_ostaa = False

if pankkitilin_saldo > 1800:
  saa_ostaa = True


if ostokset_yhteensa > 0 and ostokset_yhteensa < 50:
  print("Voit hyvillä mielin ostaa vielä herkkuja!")
elif ostokset_yhteensa >= 50 and ostokset_yhteensa < 100:
  print("Harkitse vakavasti herkkujen ostamista, pitäisiköhän säästää kuitenkin?")
elif ostokset_yhteensa > 200 and saa_ostaa == False:
  print("Älä osta enempää.")

print("Ohjelman suoritus loppui.")