# Importar las bibliotecas necesarias
import click
from rich.console import Console
from rich.table import Table
from art import text2art
# Definir la clase Cafe que tiene un nombre, costo e ingredientes
class Cafe:
    # El constructor inicializa el objeto Cafe con nombre, costo e ingredientes
    def __init__(self, nombre, costo, ingredientes):
        self.nombre = nombre
        self.costo = costo
        self.ingredientes = ingredientes

# Definir la clase Cafetera que contiene el menú de cafés
class Cafetera:
    # El constructor inicializa el objeto Cafetera con un menú de objetos Cafe
    def __init__(self):
        # Los cafés disponibles son almacenados como una lista de objetos Cafe
        self.menu = [
            Cafe("Café expreso", 12.80, {"agua": 100, "cafe": 76}),
            Cafe("Café latte", 15.50, {"agua": 100, "leche": 50, "cafe": 76}),
            Cafe("Café capuchino", 14.75, {"agua": 100, "leche": 50, "cafe": 76}),
            Cafe("Café americano", 10.25, {"agua": 150, "cafe": 76})
        ]

    # El método mostrar_menu imprime el menú de cafés en consola
    def mostrar_menu(self):
        # Instancia del objeto Console de la biblioteca Rich
        console = Console()
        # Imprimir en consola el título del menú
        console.print(text2art("Bienvenido a la Cafetera!"))
        # Instancia del objeto Table de la biblioteca Rich
        table = Table(show_header=True, header_style="bold violet" )
        # Añadir las columnas a la tabla
        table.add_column("Número", style="dim")
        table.add_column("Café", style="dim")
        table.add_column("Costo", justify="right")
        # Para cada café en el menú, añadir una fila a la tabla
        for i, cafe in enumerate(self.menu):
            table.add_row(str(i + 1), cafe.nombre, f"${cafe.costo}")
        # Imprimir en consola la tabla
        console.print(table)

    # El método obtener_cafe devuelve el café seleccionado por su índice
    def obtener_cafe(self, indice):
        # Si el índice está dentro del rango de la lista, devuelve el café correspondiente
        if indice >= 1 and indice <= len(self.menu):
            return self.menu[indice - 1]
        # Si no, devuelve None
        else:
            return None

    # El método procesar_pago recoge el dinero introducido por el usuario hasta cubrir el costo
    def procesar_pago(self, costo):
        # Lista para almacenar las monedas introducidas
        monedas = []
        # Mientras el dinero introducido no cubra el costo, seguir pidiendo más monedas
        while sum(monedas) < costo:
            moneda = click.prompt("Inserta una moneda (10, 5 o 1)", type=click.Choice(["10", "5", "1"]))
            monedas.append(int(moneda))
        # Devolver la suma de las monedas introducidas
        return sum(monedas)

    # El método servir_cafe imprime en consola el café servido y sus ingredientes
    def servir_cafe(self, cafe):
        # Instancia del objeto Console de la biblioteca Rich
        console = Console()
        # Imprimir en consola el café servido
        console.print("[bold][green]🍵 ¡Pago aceptado! Sirviendo café...[/green][/bold]")
        console.print(f"[bold][cyan]Café seleccionado:[/cyan][/bold] {cafe.nombre}")
        console.print("[bold][cyan]Ingredientes:[/cyan][/bold]")
        # Para cada ingrediente en el café, imprimir su nombre y cantidad
        for ingrediente, cantidad in cafe.ingredientes.items():
            console.print(f"- {ingrediente.capitalize()}: {cantidad} ml")

    # El método devolver_cambio imprime en consola el cambio a devolver, si lo hay
    def devolver_cambio(self, pago, costo):
        # Calcular el cambio a devolver
        cambio = pago - costo
        # Instancia del objeto Console de la biblioteca Rich
        console = Console()
        # Si hay cambio, imprimir en consola el monto a devolver
        if cambio > 0:
            console.print(f"[bold][cyan]💵 Devuelve cambio:[/cyan][/bold] ${cambio}")
        # Si no, imprimir que no hay cambio a devolver
        else:
            console.print("[bold][cyan]💰 No hay cambio que devolver.[/cyan][/bold]")

# La función main es la función principal que coordina el flujo del programa
@click.command()
def main():

    cafetera = Cafetera()
    # Mostrar el menú de cafés
    cafetera.mostrar_menu()
    # Pedir al usuario que seleccione el número del café
    indice = click.prompt("Seleccione el número del café", type=int)
    # Obtener el café seleccionado
    cafe_seleccionado = cafetera.obtener_cafe(indice)
    # Si se ha obtenido un café válido
    if cafe_seleccionado:
        # Instancia del objeto Console de la biblioteca Rich
        console = Console()
        # Imprimir en consola el café seleccionado y sus ingredientes
        console.print(f"[bold][cyan]☕ Café seleccionado:[/cyan][/bold] {cafe_seleccionado.nombre}")
        console.print("[bold][cyan]🌟 Ingredientes:[/cyan][/bold]")
        for ingrediente, cantidad in cafe_seleccionado.ingredientes.items():
            console.print(f"- {ingrediente.capitalize()}: {cantidad} ml")
        # Imprimir en consola el costo del café
        console.print(f"[bold][cyan]💲 Costo:[/cyan][/bold] ${cafe_seleccionado.costo}")
        # Procesar el pago
        pago = cafetera.procesar_pago(cafe_seleccionado.costo)
        # Servir el café
        cafetera.servir_cafe(cafe_seleccionado)
        # Devolver el cambio, si lo hay
        cafetera.devolver_cambio(pago, cafe_seleccionado.costo)
    # Si no se ha obtenido un café válido, imprimir en consola un mensaje de error
    else:
        console = Console()
        console.print("[bold][red]❌ El café seleccionado no está disponible. Por favor, seleccione una opción válida.[/red][/bold]")
        return
    # Imprimir en consola un mensaje de despedida
    console.print("[bold][cyan]👋 ¡Gracias por usar la cafetera! Vuelve pronto.[/cyan][/bold]")

# Si este archivo se está ejecutando como el principal, iniciar la función main
if __name__ == "__main__":
    main()
