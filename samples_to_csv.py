import os

os.chdir('Samples')

file_data = ""
for sample_folder in os.listdir():
    class_name = sample_folder.replace('samples_', '')
    for file in os.listdir(sample_folder):
        data = eval(open(sample_folder+'/'+file, 'r').read())
        x_data = ",".join([str(i) for i in data])
        if file_data == "":
            headers_csv = ",".join([str(i) for i in range(1,len(data)+1)])
            file_data += f"{headers_csv},text\n"
        file_data += f"{x_data},{class_name}\n"
os.chdir("../")

open('result_on_and_off.csv', 'w').write(file_data)