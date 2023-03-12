import os
from machine import Pin, ADC
import ustruct , time

analog_value = machine.ADC(28)
conversion_factor =3.3/(4096)

nowtm = time.time()
# while nowtm+5 >= time.time():
sample_name = "off"#input("enter sample name: ")
dir_name = "samples_" + sample_name
samplenum = 0
try:
    os.mkdir(dir_name)
except:
    pass
endprogram = False
while True:
    samples = []
    input("Enter to record after 0.5 seconds")
    time.sleep(0.5)
    print("say")
#     for _ in range(700):
    for _ in range(40):
        try:
            reading = int(analog_value.read_u16()*conversion_factor*100)/100
            samples.append(reading) #
#             print(reading)
#             time.sleep(0.001)
            time.sleep(0.02)
        except:
            endprogram = True
    if endprogram:
        break
    else:
        with open(dir_name+"/"+sample_name+"_"+str(samplenum)+".txt", 'w') as output:
            output.write(str(samples))
        print("done sample", samplenum)
        samplenum += 1
    



with open('Voice.bin', 'w') as output:
     output.write(",".join(samples))