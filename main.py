class Auto: 
    cantidadCreados = 0 

    def __init__(self, modelo, asientos, marca, motor, registro, precio):
        self.modelo = modelo
        self.asientos = asientos
        self.marca = marca
        self.motor = motor 
        self.registro = registro
        self.precio= precio
        
    def cantidadAsientos(self):
        numeroAsientos = 0
        for Asiento in self.asientos: 
            if isinstance(self.asientos, Asiento): #isinstance(object, type) returns a boolean when the object is in the type
                numeroAsientos += 1
        return (numeroAsientos)
    
    def verificarIntegridad(self): 
        if self.motor.registro != self.registro: 
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento != None: 
                if asiento.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto Original"

class Asiento: 
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores: 
            self.color = color

class Motor: 
    def __init__(self, numeroCilinros, tipo, registro):
        self.numeroCilindros = numeroCilinros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro (self, registro):
        self.registro = registro    

    def asignarTipo(self, tipo):
        tipos =["electrico", "gasolina"]
        if tipo in tipos:
            self.tipo = tipo
            