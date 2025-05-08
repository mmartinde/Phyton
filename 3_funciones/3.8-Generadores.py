##https://www.youtube.com/watch?v=536fB1qvSeE&t=12s
 #GENERADORES
# #Un generador es una función que utiliza la palabra clave yield para devolver un valor y pausar su ejecución, permitiendo que se reanude más tarde.
# #Los generadores son una forma de crear iteradores de manera más sencilla y eficiente en comparación con las funciones tradicionales.
# #Cuando se llama a un generador, no se ejecuta inmediatamente. En su lugar, devuelve un objeto generador que se puede iterar.
# #Cada vez que se llama a la función next() en el generador, se reanuda la ejecución desde el último yield y se devuelve el siguiente valor.
# #Los generadores son útiles para trabajar con grandes conjuntos de datos o flujos de datos, ya que permiten generar valores bajo demanda sin cargar todo en memoria.
# #Esto es especialmente útil en situaciones donde se necesita procesar datos de manera eficiente y evitar el uso excesivo de memoria.

def return_valores():
   print("Hola, soy un generador")
   return True

def generador(*args):
    for valor in args:
        yield valor *10, True #Un ejemplo de generador que multiplica cada valor por 10 y devuelve True

for valor_uno, valor_dos in generador(1,2,3,4,5):
    print(valor_uno, valor_dos) 

