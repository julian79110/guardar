import re
import json

with open('132-14150.json','r', encoding='utf-8') as f:
    data=json.load(f)

with open('132-22359.json','r', encoding='utf-8') as f:
    data2=json.load(f)

with open('132-1808.json','r', encoding='utf-8') as f:
    data3=json.load(f)

with open('132-45993.json','r', encoding='utf-8') as f:
    data4=json.load(f)

with open('156-1206.json','r', encoding='utf-8') as f:
    data5=json.load(f)

decision=1
while decision==1:
    respuesta = input('Que Archivo Desea Mirar?: ')
    if int(respuesta) == 0:
        decision=0
        print('finalizado')
    elif int(respuesta) == 1:
        if data:
            for item in data['textoAnotaciones']:
                cadena = item
                for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}', cadena):
                    print(i)
        else:
            print('No hay datos disponibles')
    elif int(respuesta) == 2:
        if data2:
            for item in data2['textoAnotaciones']:
                cadena = item
                for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}',cadena):
                    print(i)
        else:
            print('No hay datos disponibles')
    elif int(respuesta) == 3:
        if data3: 
            for item in data3['textoAnotaciones']:
                cadena = item
                for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}'):
                    print(i)
        else:
            print('No hay datos disponibles')
    elif int(respuesta) == 4:
        if data4:
            for item in data4['textoAnotaciones']:
                cadena = item
                for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}',cadena):
                    print(i)
        else:
            print('No hay datos disponibles')
    elif int(respuesta) == 5:
        if data5:
            for item in data5['textoAnotaciones']:
                cadena = item
                for i in re.findall(r'ESPECIFICACION: [0-9]{3,5}',cadena):
                    print(i)
        else:
            print('No hay datos disponibles')
