
import time
import gpiod
from gpido.line import Direction, Value

LED = 14
#configuracion de pines de entradas
chip = gpiod.Chip("/dev/gpiovhip0")
request = chip.request_lines(
    consumer = "parpadeando"
    config = {
        LED: gpiod.LineSettings(
            dierction = Direction.OUTPUT, output_value = value.INACTIVE
        )
    }
)

#Activavion de las señales
try:    
    while True:
        request.set_value(LED, Value.INACTIVE)
        time.sleep(1)
        request.set_value(LED, Value.ACTIVATE)
        time.sleep(1)
except KeyboardInterrupt:
    print("interrumpcion por el usuario")
finally:
        request.realse()
        chip.close()
