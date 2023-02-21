################################################
#
#  testar o modulo airtravel

################################################

import airtravel
from airtravel import Flight, Aircraft, Aircraft_boing777, Aircraft_airbus319
import pprint
from pprint import pprint

""" modulo para testar classes Flight e Aircraft assim 
como a funcao console_card_printer() do modulo airtravel """


print ("################ TESTES DE RESERVAS")

print("Criacao do Voo L-345-1 \n")
f = Flight("BA758", Aircraft("L-345-1", "airbus A319", 22, 6))

print(" Reservas dos lugares 12A, 15F, 15E, 1C e 1D \n")
f.allocate_seat("12A", "Manel dos anzois")
# f.allocate_seat("12A","Maria antonieta")
f.allocate_seat("15F", "Hanz dos algarves")
f.allocate_seat("15E", "Antonio SImoes")
# f.allocate_seat("E27","Yukuriri")
f.allocate_seat("1C", "John Major")
f.allocate_seat("1D", "Richard")
# f.allocate_seat("DD","Larry Page")
pprint(f._seating)

print ("################ TESTES DE ALTERACAO DE RESERVAS")
print ("mudança de lugar do 12A para o 15D \n")
f.relocate_passageiro("12A", "15D")
pprint(f._seating)


print ("################ LUGARES DISPONIVEIS POR VOO")
print(f.number())
print(f.aircraft_model())
pprint(f._seating)
print(f.num_available_seats())


print ("################ IMPRESSO DOS CARTOS DE EMBARQUE DE UM VOO")
f.make_boarding_cards(airtravel.console_card_printer)

print ("################ CLASSE Aircraft_boing777")
g777 = Flight("BA758", Aircraft_boing777  ("L-335-2", "Boing 777", 56, 6))
g777.allocate_seat("8A", "Manel dos anzois")
g777.allocate_seat("16F", "Hanz dos algarves")
g777.allocate_seat("16E", "Antonio SImoes")
g777.allocate_seat("3C", "John Major")
g777.allocate_seat("3D", "Richard")

print ("################ CLASSE aircraft_airbus319")
h319 = Flight("BA758", Aircraft_airbus319("L-645-6", "airbus A319", 22, 6))
h319.allocate_seat("10A", "Manel dos anzois")
h319.allocate_seat("13F", "Hanz dos algarves")
h319.allocate_seat("13E", "Antonio SImoes")
h319.allocate_seat("5C", "John Major")
h319.allocate_seat("5D", "Richard")

g777.make_boarding_cards(airtravel.console_card_printer)
print(g777.num_available_seats())
h319.make_boarding_cards(airtravel.console_card_printer)
print(h319.num_available_seats())
