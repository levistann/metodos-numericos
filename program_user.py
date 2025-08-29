import flet as ft
import matplotlib as plt
import sympy as sp

#importamos los metodos disponibles
'''from newton_raphson import new_raph
from biseccion import bis_sect
from muller import muller
from punto_fijo import punto_fijo
from steffensen import punto_fijo
from secante import sec'''

#Esquematizacion principal del programa
def main(page: ft.Page): #Funcion principal de la estructura del programa
    page.title = 'Metodos Numericos'
    page.bgcolor = ft.Colors.WHITE38
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    #Titulo
    titulo = ft.Text(
        value = 'Programa para aproximaciones con Metodos Numericos',
        size = 30,
        font_family='Verdana',
        weight = ft.FontWeight.NORMAL
        )
    page.add(titulo)
    
    #Encontrar raiz usando el metodo seleccionado
    #def hallar_raiz(algoritmo, )

    #Colocar funcion y valores de intervalo o primera aproxmacion para Newton Raphson
    funcion_texto = ft.TextField(hint_text = 'Ingresa tu funcion, ej. "sin(x)**2 + 1/(x+2)"', width=350 )
    intervalo_inf = ft.TextField(hint_text = 'Valor inf del intervalo (si aplica) o primera aprox. para NewtonRap', width = 400)
    intervalo_sup = ft.TextField(hint_text = 'Valor sup del intervalo (si aplica)', width = 400)


    page.add(
    ft.Row([
    funcion_texto,
    intervalo_inf,
    intervalo_sup,
    ft.ElevatedButton(text = "Hallar raiz")
    ]
    )
    )

    #Metodos disponibles para hallar la raiz
    metodo = ft.Dropdown(
        label = "Selecciona un metodo",
        options = [
            ft.dropdown.Option("Biseccion"),
            ft.dropdown.Option("Newton Raphson"),
            ft.dropdown.Option("Punto fijo"),
            ft.dropdown.Option("Muller"),
            ft.dropdown.Option("steffensen")
        ],
        width = 300,
        alignment = ft.alignment.center_right
    )
    page.add(ft.Row(controls = [metodo], alignment = "Start" ))  

    

ft.app(target = main)
