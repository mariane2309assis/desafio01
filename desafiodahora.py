horaentrada1 = int(input("Qual a hora da 1º entrada? "))
minentrada1 = int(input("Qual os minutos da 1º entrada? "))
horaentrada2 = int(input("Qual a hora da 2º entrada? "))
minentrada2 = int(input("Qual os minutos da 2º entrada? "))

horadasaida = horaentrada1 + horaentrada2
mindasaida = minentrada1 + minentrada2

if mindasaida >= 60:
    horadasaida = horadasaida + 1
    mindasaida = mindasaida - 60
if horadasaida > 12:
    horadasaida = horadasaida - 12
if horadasaida > 24:
    horadasaida = horadasaida - 24

print(horadasaida, ":", mindasaida)
