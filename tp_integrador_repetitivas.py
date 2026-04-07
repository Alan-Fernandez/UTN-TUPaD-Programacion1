def pedir_nombre_cliente():
    while True:
        nombre = input("Cliente: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacio.")
            continue
        if not nombre.isalpha():
            print("Error: el nombre debe contener solo letras.")
            continue
        return nombre


def pedir_cantidad_productos():
    while True:
        cantidad = input("Cantidad de productos: ").strip()
        if not cantidad.isdigit():
            print("Error: ingrese un numero entero positivo.")
            continue
        cantidad_int = int(cantidad)
        if cantidad_int <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
            continue
        return cantidad_int


def pedir_precio_producto(numero_producto):
    while True:
        precio = input(f"Producto {numero_producto} - Precio: ").strip()
        if not precio.isdigit():
            print("Error: el precio debe ser un numero entero.")
            continue
        return int(precio)


def pedir_descuento_producto():
    while True:
        tiene_descuento = input("Descuento (S/N): ").strip().lower()
        if tiene_descuento not in ("s", "n"):
            print("Error: ingrese S o N.")
            continue
        return tiene_descuento


def ejercicio_1_caja_kiosco():
    print("\n--- Ejercicio 1: Caja del Kiosco ---")
    cliente = pedir_nombre_cliente()
    cantidad = pedir_cantidad_productos()

    total_sin_descuentos = 0
    total_con_descuentos = 0.0

    for i in range(1, cantidad + 1):
        precio = pedir_precio_producto(i)
        descuento = pedir_descuento_producto()

        total_sin_descuentos += precio

        if descuento == "s":
            precio_final = precio * 0.9
        else:
            precio_final = float(precio)

        total_con_descuentos += precio_final

    ahorro_total = float(total_sin_descuentos) - total_con_descuentos
    promedio_producto = total_con_descuentos / cantidad

    print(f"\nCliente: {cliente}")
    print(f"Total sin descuentos: ${total_sin_descuentos}")
    print(f"Total con descuentos: ${total_con_descuentos:.2f}")
    print(f"Ahorro: ${ahorro_total:.2f}")
    print(f"Promedio por producto: ${promedio_producto:.2f}")


def login_campus(usuario_correcto, clave_correcta):
    intentos_maximos = 3

    for intento in range(1, intentos_maximos + 1):
        usuario = input(f"Intento {intento}/3 - Usuario: ").strip()
        clave = input("Clave: ").strip()

        if usuario == usuario_correcto and clave == clave_correcta:
            print("Acceso concedido.")
            return clave_correcta

        print("Error: credenciales invalidas.")

    print("Cuenta bloqueada")
    return None


def cambiar_clave(clave_actual):
    while True:
        nueva_clave = input("Ingrese nueva clave: ").strip()
        if len(nueva_clave) < 6:
            print("Error: la clave debe tener al menos 6 caracteres.")
            continue

        confirmacion = input("Confirme nueva clave: ").strip()
        if nueva_clave != confirmacion:
            print("Error: las claves no coinciden.")
            continue

        print("Clave cambiada correctamente.")
        return nueva_clave


def menu_campus(clave_inicial):
    clave_actual = clave_inicial

    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opcion: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            continue

        opcion_int = int(opcion)
        if opcion_int < 1 or opcion_int > 4:
            print("Error: opcion fuera de rango.")
            continue

        if opcion_int == 1:
            print("Inscripto")
        elif opcion_int == 2:
            clave_actual = cambiar_clave(clave_actual)
        elif opcion_int == 3:
            print("Segui practicando: cada linea de codigo te acerca a tu objetivo.")
        else:
            print("Saliendo del campus...")
            break


def ejercicio_2_campus_menu_seguro():
    print("\n--- Ejercicio 2: Acceso al Campus y Menu Seguro ---")
    usuario_correcto = "alumno"
    clave_correcta = "python123"

    clave_activa = login_campus(usuario_correcto, clave_correcta)
    if clave_activa is None:
        return

    menu_campus(clave_activa)


def main():
    while True:
        print("\n=== TP Integrador ===")
        print("1) Ejercicio 1 - Caja del Kiosco")
        print("2) Ejercicio 2 - Acceso al Campus")
        print("3) Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un numero valido.")
            continue

        opcion_int = int(opcion)

        if opcion_int == 1:
            ejercicio_1_caja_kiosco()
        elif opcion_int == 2:
            ejercicio_2_campus_menu_seguro()
        elif opcion_int == 3:
            print("Programa finalizado.")
            break
        else:
            print("Error: opcion fuera de rango.")


if __name__ == "__main__":
    main()
