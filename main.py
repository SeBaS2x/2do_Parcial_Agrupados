
from funciones import *
from controlador import *
from archivos import *
import sys
from game import*
juego = solicitar_string("iniciar Juego: [si/no] ? ")

while juego != "si":
    juego = solicitar_string("iniciar Juego: [si/no] ? ")
main()
