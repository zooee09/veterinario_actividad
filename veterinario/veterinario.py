class Animal:
    def __init__(self, nombre, especie, peso, edad, duenio):
        self.nombre = nombre
        self.especie = especie
        self.peso = peso
        self.edad = edad
        self.duenio = duenio

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {self.peso} kg, {self.edad} años, dueño: {self.duenio}"


class Veterinaria:
    def __init__(self):
        self.animales = []
        self.clientes = {}

    def registrar_animal(self):
        nombre = input('Nombre del animal: ').strip()
        especie = input('Especie (perro/gato): ').strip().lower()
        if especie not in ('perro', 'gato'):
            especie = 'otro'
        peso = self._leer_flotante('Peso en kg: ')
        edad = self._leer_entero('Edad en años: ')
        duenio = input('Nombre del dueño: ').strip()
        if not nombre or not duenio:
            print('Nombre del animal y del dueño son obligatorios.')
            return
        tipo_cliente = input('Cliente nuevo o viejo? (nuevo/viejo): ').strip().lower()
        if tipo_cliente == 'viejo':
            self.clientes[duenio] = max(self.clientes.get(duenio, 0), 2)
        else:
            self.clientes[duenio] = self.clientes.get(duenio, 0) + 1
            tipo_cliente = 'nuevo' if self.clientes[duenio] == 1 else 'viejo'
        self.animales.append(Animal(nombre, especie, peso, edad, duenio))
        print(f'Animal registrado. Cliente {duenio} es {tipo_cliente}.')

    def mostrar_resumen(self):
        print('\n--- Animales registrados ---')
        if not self.animales:
            print('No hay animales registrados.')
        for i, animal in enumerate(self.animales, 1):
            print(f'{i}. {animal}')
        print('\n--- Clientes ---')
        if not self.clientes:
            print('No hay clientes registrados.')
        for nombre, visitas in self.clientes.items():
            estado = 'viejo' if visitas > 1 else 'nuevo'
            print(f'{nombre} - {estado} (visitas: {visitas})')

    def retirar_mascota(self):
        if not self.animales:
            print('No hay animales registrados.')
            return
        print('\n--- Retirar mascota ---')
        for i, animal in enumerate(self.animales, 1):
            print(f'{i}. {animal}')
        indice = self._leer_entero('Ingrese el número de la mascota a retirar: ')
        if indice < 1 or indice > len(self.animales):
            print('Número inválido.')
            return
        mascota = self.animales.pop(indice - 1)
        duenio = mascota.duenio
        visitas_actuales = self.clientes.get(duenio, 0) - 1
        if visitas_actuales > 0:
            self.clientes[duenio] = visitas_actuales
            estado = 'viejo' if visitas_actuales > 1 else 'nuevo'
        else:
            self.clientes.pop(duenio, None)
            estado = 'eliminado'
            visitas_actuales = 0
        print(f'Se retiró a {mascota.nombre}. Cliente {duenio}: {visitas_actuales} visitas ({estado}).')

    def _leer_entero(self, mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= 0:
                    return valor
            except ValueError:
                pass
            print('Ingrese un número entero válido.')

    def _leer_flotante(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor > 0:
                    return valor
            except ValueError:
                pass
            print('Ingrese un número válido mayor a 0.')

    def ejecutar(self):
        while True:
            print('\n=== Veterinaria ===')
            print('1. Registrar animal')
            print('2. Mostrar resumen')
            print('3. Salir')
            print('4. Retirar mascota')
            opcion = input('Seleccione una opción: ').strip()
            if opcion == '1':
                self.registrar_animal()
            elif opcion == '2':
                self.mostrar_resumen()
            elif opcion == '3':
                print('Saliendo. Gracias.')
                break
            elif opcion == '4':
                self.retirar_mascota()
            else:
                print('Opción no válida.')


if __name__ == '__main__':
    clinica = Veterinaria()
    clinica.ejecutar()