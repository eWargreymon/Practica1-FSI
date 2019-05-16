# Practica1-FSI Eduardo Hernández Parra
Código de la práctica 1

Ejemplo de ejecución para, por ejemplo, nodos G y S.
Como heurística he utilizado la distancia en linea recta entre dos puntos calculada de la forma: (|x1-x2|)+(|y1-y2|) + el coste del camino.
-----Búsqueda por branch and bounding con subestimación-----
Número de nodos: 5 (Node S, Node R, Node P, Node B, Node G)

Hagamos el recorrido:
Partimos de G, de donde expande B, al que accedemos. En B generamos los nodos F(con valor 106+211), U(con valor 356+85) y P(con valor 202+101). Siendo P el de
menor coste, accedemos a él. Desde P, generamos los nodos R(con valor 73+97) y C(con valor 215+138), accediendo a R. En R se genera de nuevo
el nodo C(con valor 215+146) y el nodo S(con valor 80). Accedemos al nodo S, que además es el nodo objetivo, finalizando el recorrido de la 
forma: G->B->P->R->S, coincidiendo con la suministrada por el programa.
