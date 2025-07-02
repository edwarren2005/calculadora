print("¡Bienvenido a la calculadora básica!")
print("Opciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Elige una opción (1/2/3/4): ")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == '1':
    resultado = num1 + num2
    operacion = "suma"
elif opcion == '2':
    resultado = num1 - num2
    operacion = "resta"
elif opcion == '3':
    resultado = num1 * num2
    operacion = "multiplicación"
elif opcion == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacion = "división"
    else:
        resultado = "No se puede dividir entre cero."
        operacion = "división"
else:
    resultado = "Opción inválida"
    operacion = "ninguna"

print(f"Resultado de la {operacion}: {resultado}")
