import json

class GeneradorInstrucciones:
    def __init__(self, nombre_archivo="instrucciones.json"):
        self.nombre_archivo = nombre_archivo

    def crear_archivo_instrucciones(self, instrucciones):
        with open(self.nombre_archivo, "w") as archivo:
            json.dump(instrucciones, archivo, indent=4)
        print(f"📄 Archivo {self.nombre_archivo} creado con los siguientes datos:")
        print(json.dumps(instrucciones, indent=4))

# Crear las instrucciones a enviar
instrucciones_1 = {
    "Carro_1":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_2 = {
    "Carro_2":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_3 = {
    "Carro_3":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_4 = {
    "Carro_4":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_5 = {
    "Carro_5":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_6 = {
    "Carro_6":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_7 = {
    "Carro_7":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_8 = {
    "Carro_8":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_9 = {
    "Carro_9":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_10 = {
    "Carro_10":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_11 = {
    "Carro_11":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":45, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

instrucciones_12 = {
    "Carro_12":{
        "Paso_1":{
            "Movimiento":{"distancia_mm":100, "velocidad_mm_s":50, "radio_mm":"inf"},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_2":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_3":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_4":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_5":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":45, "t_ser":2}
            },
        "Paso_6":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":40, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_7":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":3}
            },
        "Paso_8":{
            "Movimiento":{"distancia_mm":50, "velocidad_mm_s":50, "radio_mm":50},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_9":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_10":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_11":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":-90, "angulo1_grados":80, "angulo2_grados":0, "t_ser":2}
            },
        "Paso_12":{
            "Movimiento":{"distancia_mm":0, "velocidad_mm_s":0, "radio_mm":0},
            "Brazo":{"angulo0_grados":0, "angulo1_grados":80, "angulo2_grados":45, "t_ser":3}
            }
        }
    }

# Usar la clase para guardar las instrucciones
generador_1 = GeneradorInstrucciones("instrucciones_carro_1.json")
generador_1.crear_archivo_instrucciones(instrucciones_1)

generador_2 = GeneradorInstrucciones("instrucciones_carro_2.json")
generador_2.crear_archivo_instrucciones(instrucciones_2)

generador_3 = GeneradorInstrucciones("instrucciones_carro_3.json")
generador_3.crear_archivo_instrucciones(instrucciones_3)

generador_4 = GeneradorInstrucciones("instrucciones_carro_4.json")
generador_4.crear_archivo_instrucciones(instrucciones_4)

generador_5 = GeneradorInstrucciones("instrucciones_carro_5.json")
generador_5.crear_archivo_instrucciones(instrucciones_5)

generador_6 = GeneradorInstrucciones("instrucciones_carro_6.json")
generador_6.crear_archivo_instrucciones(instrucciones_6)

generador_7 = GeneradorInstrucciones("instrucciones_carro_7.json")
generador_7.crear_archivo_instrucciones(instrucciones_7)

generador_8 = GeneradorInstrucciones("instrucciones_carro_8.json")
generador_8.crear_archivo_instrucciones(instrucciones_8)

generador_9 = GeneradorInstrucciones("instrucciones_carro_9.json")
generador_9.crear_archivo_instrucciones(instrucciones_9)

generador_10 = GeneradorInstrucciones("instrucciones_carro_10.json")
generador_10.crear_archivo_instrucciones(instrucciones_10)

generador_11 = GeneradorInstrucciones("instrucciones_carro_11.json")
generador_11.crear_archivo_instrucciones(instrucciones_11)

generador_12 = GeneradorInstrucciones("instrucciones_carro_12.json")
generador_12.crear_archivo_instrucciones(instrucciones_12)