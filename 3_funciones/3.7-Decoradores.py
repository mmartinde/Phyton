#https://www.youtube.com/watch?v=c9J7FHLjBds&t=13s
#Decoradores
#Un decorador es una función que recibe otra función como argumento y la envuelve para extender su funcionalidad sin modificar su código original.
#Los decoradores son una forma de aplicar un patrón de diseño llamado "decorador" en programación orientada a objetos.
#En Python, los decoradores se utilizan comúnmente para agregar funcionalidades a funciones o métodos existentes de manera sencilla y legible.
#Un decorador se define como una función que toma otra función como argumento y devuelve una nueva función que generalmente llama a la función original.
#El decorador se aplica a una función utilizando el símbolo "@" seguido del nombre del decorador antes de la definición de la función.
#Ejemplo de un decorador simple

def decorador(is_valid=False): #decorador que recibe un argumento is_valid
    def _decorador(funcion): #decorador función que ejecuta todo o Wrapper
        
        def before_action():
            print("El decorador es válido")
        
        def after_action():
            print("Adiós, soy un decorador")
        
        def nueva_funcion(*arg,**kwargs):
            if is_valid:
                before_action()
                
            resultado = funcion(*arg,**kwargs) #llama a la función original y la ejecuta
            
            after_action()
            return resultado
        return nueva_funcion #retorna la nueva función
    
    return _decorador #retorna el decorador. Decorador que imprime un mensaje antes y después de ejecutar la función original

@decorador (True)
def saluda():
    print("Hola, ¿cómo estás?")

@decorador()
def suma(num_uno, num_dos):
    return(num_uno+num_dos)

# Ejemplo de uso
resultado = suma(80,20)
print(resultado)
