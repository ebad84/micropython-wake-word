from machine import Pin, ADC
import ustruct , time

from svm_min10 import score

from machine import Pin

led = Pin(25, Pin.OUT)

analog_value = machine.ADC(28)
conversion_factor =3.3/(4096)

samples = []
nowtm = time.time()
endprogram = False
last_res = None
nospeak = True
while True:
    samples = []
#     input("Enter to record after 0.5 seconds")
#     time.sleep(0.5)
    print("say")
#     for _ in range(700):

    for _ in range(40):
        try:
            reading = int(analog_value.read_u16()*conversion_factor*100)/100
            samples.append(reading) #
#             print(reading,",")
#             time.sleep(0.001)
            time.sleep(0.02)
        except:
            endprogram = True
    print("done")
    if endprogram:
        break
    else:
        prediction = score(samples)
        print(prediction)
        if any(i > 28.5 or i < 25.5 for i in samples):
            print("speek detected")
            prediction[-1] = -100
#             print(prediction)
        else:
            print("no speek")
            prediction[-1] = 100
        print(prediction.index(max(prediction)))
        res = prediction.index(max(prediction))
        if res != 2 and last_res != res:
            last_res = res
            if res == 0:
                led.value(0)
                print("off")
            elif nospeak and res == 1:
                led.value(1)
                print("on")
                nospeak = False
            else:
                nospeak = True
        else:
            nospeak = True
#                 if prediction[1] < 1:
#                     if prediction[0] > 0.3:
#                         led.value(0)
#                         print("off")
#                 else:
#                     led.value(1)
#                     print("on")
        
#     break
#         if prediction < 0:
#             print(2, prediction, int(prediction))
#         else:
#             print(1, prediction, int(prediction))



