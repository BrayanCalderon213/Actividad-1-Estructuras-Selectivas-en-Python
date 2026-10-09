"""
Programa: Calculadora de Calificaciones Finales
Descripción: Calcula la calificación final de un estudiante ponderando
los parciales (40%), el proyecto (30%) y el examen final (30%),
validando que las calificaciones ingresadas se encuentren en el rango de 0 a 100.
"""

# Constantes para los porcentajes de evaluación
PESO_PARCIALES = 0.40
PESO_PROYECTO = 0.30
PESO_EXAMEN = 0.30

def calcular_calificacion_final():
    print("--- Calculadora de Calificaciones Finales ---")
    
    try:
        # Entrada de datos convirtiéndolos a float
        parciales = float(input("Ingresa la calificación de parciales (0-100): "))
        proyecto = float(input("Ingresa la calificación del proyecto (0-100): "))
        examen_final = float(input("Ingresa la calificación del examen final (0-100): "))
        
        # Validación de rangos con estructuras if-else
        if (0 <= parciales <= 100) and (0 <= proyecto <= 100) and (0 <= examen_final <= 100):
            
            # Proceso: cálculo del promedio ponderado
            calificacion_final = (parciales * PESO_PARCIALES) + \
                                 (proyecto * PESO_PROYECTO) + \
                                 (examen_final * PESO_EXAMEN)
            
            # Salida de resultados usando f-strings y formato de decimales
            print("\n--- Resultado del Estudiante ---")
            print(f"Calificación final ponderada: {calificacion_final:.2f}")
            
            if calificacion_final >= 60:
                print("Estado: Aprobado")
            else:
                print("Estado: No aprobado")
        else:
            print("\nError: Las calificaciones deben estar estrictamente en el rango de 0 a 100.")
            
    except ValueError:
        print("\nError: Ingresa un valor numérico válido.")

if __name__ == "__main__":
    calcular_calificacion_final() 