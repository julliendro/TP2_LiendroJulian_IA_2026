def funcion_heuristica(posicion_actual, posicion_objetivo):
    """
    Funcion heuristica que calcula la distancia estimada al objetivo (A)
    utilizando el perfil del relieve superficial.
    """
    return abs(posicion_actual - posicion_objetivo)

def busqueda_heuristica(posicion_inicial, posicion_objetivo, paso):
    """
    Simula una busqueda heuristica (Primero el Mejor) guiada 
    por la distancia estimada hacia la meta.
    """
    print(f"--- INICIO BUSQUEDA HEURISTICA ---")
    pos_actual = posicion_inicial
    intentos = 0
    
    print(f"Posicion inicial (B): {pos_actual}, Objetivo (A): {posicion_objetivo}")
    
    while abs(pos_actual - posicion_objetivo) > (paso / 2):
        intentos += 1
        candidato_izq = pos_actual - paso
        candidato_der = pos_actual + paso
        
        h_izq = funcion_heuristica(candidato_izq, posicion_objetivo)
        h_der = funcion_heuristica(candidato_der, posicion_objetivo)
        
        print(f"Intento {intentos} | Actual: {pos_actual:.2f} | H(izq) = {h_izq:.2f}, H(der) = {h_der:.2f}")
        
        if h_izq < h_der:
            pos_actual = candidato_izq
            print(f"-> Moviendo a la IZQUIERDA hacia {pos_actual:.2f}")
        else:
            pos_actual = candidato_der
            print(f"-> Moviendo a la DERECHA hacia {pos_actual:.2f}")
            
    print(f"Posicion de montaje A alcanzada con exito en {pos_actual:.2f}! Total de pasos: {intentos}")
    return pos_actual

if __name__ == "__main__":
    busqueda_heuristica(posicion_inicial=10.0, posicion_objetivo=7.5, paso=0.5)