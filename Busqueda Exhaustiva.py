def busqueda_exhaustiva(posicion_inicial, posicion_objetivo, paso, limite_intentos=50):
    """
    Simula una busqueda exhaustiva simetrica (tipo anchura) 
    a partir de la posicion inicial B buscando la posicion de montaje A.
    """
    print(f"--- INICIO BUSQUEDA EXHAUSTIVA ---")
    print(f"Posicion inicial (B): {posicion_inicial}, Posicion objetivo (A): {posicion_objetivo}")
    
    intentos = 0
    for i in range(1, limite_intentos + 1):
        pos_derecha = posicion_inicial + (i * paso)
        intentos += 1
        print(f"Intento {intentos}: Probando a la derecha -> Posicion {pos_derecha:.2f}")
        if abs(pos_derecha - posicion_objetivo) < (paso / 2):
            print(f"Posicion de montaje A encontrada en {pos_derecha:.2f} (Derecha)! Total de intentos: {intentos}")
            return pos_derecha
            
        pos_izquierda = posicion_inicial - (i * paso)
        intentos += 1
        print(f"Intento {intentos}: Probando a la izquierda -> Posicion {pos_izquierda:.2f}")
        if abs(pos_izquierda - posicion_objetivo) < (paso / 2):
            print(f"Posicion de montaje A encontrada en {pos_izquierda:.2f} (Izquierda)! Total de intentos: {intentos}")
            return pos_izquierda
            
    print("No se encontro el objetivo dentro del limite.")
    return None

if __name__ == "__main__":
    busqueda_exhaustiva(posicion_inicial=10.0, posicion_objetivo=7.5, paso=0.5)