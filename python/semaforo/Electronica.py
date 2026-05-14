
import time
import gpiod
from gpido.line import Direction, Value

DI_00 = 2
D0_00 = 14
#configuracion de pines de entradas
chip = gpiod.Chip("/dev/gpiochip0")
request = chip.request_lines(
    consumer = "parpadeo"
    config = {
        DI_00: gpiod.LineSettings(direction = Direction.INPUT)
        D0_00: gpiod.LineSettings(direction = Direction.OUYPUT, output_value = Value)
    }
)

#Activavion de las señales
try:    
    while True:
         valor = request.get_value(DI_00)
         print (valor)
         request.set_value
        #request.set_value(D0_00, request.get_value(DI_00))
except KeyboardInterrupt:
    print("interrumpcion por el usuario")
finally:
        request.release()
        chip.close()
