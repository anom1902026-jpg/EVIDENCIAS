from blessed import Terminal
import math

term = Terminal()


# =======================
# CLASES DE FIGURAS
# =======================

class Rectangulo:
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def area(self) -> float:
        return self.ancho * self.alto

    def perimetro(self) -> float:
        return 2 * (self.ancho + self.alto)


class Cuadrado:
    def __init__(self, lado: float):
        self.lado = lado

    def area(self) -> float:
        return self.lado ** 2

    def perimetro(self) -> float:
        return 4 * self.lado


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    def area(self) -> float:
        return math.pi * self.radio ** 2

    def perimetro(self) -> float:
        return 2 * math.pi * self.radio


class Triangulo:
    def __init__(self, base: float, altura: float, lado2: float, lado3: float):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self) -> float:
        return (self.base * self.altura) / 2

    def perimetro(self) -> float:
        return self.base + self.lado2 + self.lado3


# =======================
# MENÚ
# =======================

class MenuFiguras:
    def __init__(self):
        self.ejecutar()

    def pedir_float(self, mensaje):
        while True:
            try:
                valor = float(input(term.cyan(mensaje)))
                if valor <= 0:
                    raise ValueError
                return valor
            except ValueError:
                print(term.red("❌ Error: Ingresa un número mayor que 0"))

    def mostrar_resultados(self, figura):
        print(term.green("\n📊 Resultados"))
        print(term.green(f"Área: {figura.area():.2f}"))
        print(term.green(f"Perímetro: {figura.perimetro():.2f}\n"))
        input(term.yellow("Presiona ENTER para continuar..."))

    def ejecutar(self):
        while True:
            print(term.clear)
            print(term.bold_blue("=== MENÚ DE FIGURAS GEOMÉTRICAS ==="))
            print(term.yellow("1. Rectángulo"))
            print(term.yellow("2. Cuadrado"))
            print(term.yellow("3. Círculo"))
            print(term.yellow("4. Triángulo"))
            print(term.yellow("0. Salir"))

            opcion = input(term.cyan("\nSelecciona una opción: "))

            if opcion == "1":
                ancho = self.pedir_float("Ancho: ")
                alto = self.pedir_float("Alto: ")
                self.mostrar_resultados(Rectangulo(ancho, alto))

            elif opcion == "2":
                lado = self.pedir_float("Lado: ")
                self.mostrar_resultados(Cuadrado(lado))

            elif opcion == "3":
                radio = self.pedir_float("Radio: ")
                self.mostrar_resultados(Circulo(radio))

            elif opcion == "4":
                base = self.pedir_float("Base: ")
                altura = self.pedir_float("Altura: ")
                lado2 = self.pedir_float("Lado 2: ")
                lado3 = self.pedir_float("Lado 3: ")
                self.mostrar_resultados(Triangulo(base, altura, lado2, lado3))

            elif opcion == "0":
                print(term.green("\n👋 Programa finalizado"))
                break

            else:
                print(term.red("❌ Opción inválida"))
                input(term.yellow("Presiona ENTER para continuar..."))


# =======================
# PROGRAMA PRINCIPAL
# =======================

if __name__ == "__main__":
    MenuFiguras()