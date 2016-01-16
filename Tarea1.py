# -*- coding: utf-8 -*-

#import packages
import csv as csv
import numpy as np
import os
import re

os.getcwd()
#Open csv file in to a Python object
csv_file_object = csv.reader(open('data.csv', 'rb'))

    

#leer la primera linea de la data y eliminar indice
header = csv_file_object.next()
header.pop(0)

#crear data
data=[]

#filas que se borran
badRows=[]

#guardar los datos del csv en la variable data
#Eliminar la columna Indice
for row in csv_file_object:
    row.pop(0);
    data.append(row)

data = np.array(data)

#se crea la lista final llamada minable
minable = []
for row in data:
    minable.append([])

newHeader = []

data

#*********************************************#
#               Cedula
#*********************************************#
#cambiar posicion de la cedula en la lista y
#ponerlo como indice
for i in xrange(0,len(data)):
    minable[i].append(data[i][1])

newHeader.append(header[1])

#*********************************************#
#               Periodo academico
#*********************************************#
for i in xrange(0,len(data)):
    sem = data[i][0]
    sem
    if((sem.find('2014') >= 0) or (sem.find('14') >= 0)):
        minable[i].append(2014)
    else:
        if((sem.find('2015') >= 0) or (sem.find('15') >= 0)):
            minable[i].append(2015)
        else:
            badRows.append(i);
    
    
newHeader.append(header[0])
#missing change
    
#*********************************************#
#               Fecha de Nacimiento
#*********************************************#
for i in xrange(0,len(data)):
    date = data[i][2]

    #arreglar fechas
    #areglar fechas con el separador '/'
    if (date.find('/') > 0):
       numbers = date.split('/')
       if(len(numbers[0]) != 2):
           numbers[0]='0'+numbers[0]
       if(len(numbers[1]) != 2):
           numbers[1]='0'+numbers[1]
       if(len(numbers[2]) != 4):
           numbers[2]='19'+numbers[2]
       newDate=numbers[0]+'/'+numbers[1]+'/'+numbers[2]
       minable[i].append(newDate)

     #areglar fechas con el separador ' '
    elif (date.find(' ') > 0):
       numbers = date.split(' ')
       if(len(numbers[0]) != 2):
           numbers[0]='0'+numbers[0]
       if(len(numbers[1]) != 2):
           numbers[1]='0'+numbers[1]
       if(len(numbers[2]) != 4):
           numbers[2]='19'+numbers[2]
       newDate=numbers[0]+'/'+numbers[1]+'/'+numbers[2]
       minable[i].append(newDate)
       
     #areglar fechas con el separador '-'
    elif (date.find('-') > 0):
       numbers = date.split('-')
       if(len(numbers[0]) != 2):
           numbers[0]='0'+numbers[0]
       if(len(numbers[1]) != 2):
           numbers[1]='0'+numbers[1]
       if(len(numbers[2]) != 4):
           numbers[2]='19'+numbers[2]
       newDate=numbers[0]+'/'+numbers[1]+'/'+numbers[2]
       minable[i].append(newDate)
    
    else:
        badRows.append(i);
        
newHeader.append(header[2])

#*********************************************#
#                   Edad
#*********************************************#
#Verificar que la edad sean solo numeros de
#lo contrario se sacan los numeros de la celda
for i in xrange(0,len(data)):
    old = re.findall(r'\d+',data[i][3]) 
    minable[i].append(old[0])

newHeader.append(header[3])

#*********************************************#
#               Estado Civil
#*********************************************#
#Cambiar los estados a numeros como se explica
#en el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][4] == 'Casado (a)' or data[i][4] == 'Unido (a)'):
        minable[i].append(1)
        
    elif(data[i][4] == 'Soltero (a)'):
        minable[i].append(2)
        
    elif(data[i][4] == 'Viudo (a)'):
        minable[i].append(3)
    

newHeader.append(header[4])

#*********************************************#
#                   Sexo
#*********************************************#
#Cambiar el dato de Sexo a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][5] == 'Femenino'):
        minable[i].append(0)
        
    elif(data[i][5] == 'Masculino'):
        minable[i].append(1)
    

newHeader.append(header[5])

#*********************************************#
#                   Escuela
#*********************************************#
#Cambiar el dato de Escuela a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][6][0] == 'E'):
        minable[i].append(0)
        
    elif(data[i][6][0] == 'B'):
        minable[i].append(1)
    

newHeader.append(header[6])

#*********************************************#
#             Ano de Ingreso
#*********************************************#
#Solo se copia el dato
for i in xrange(0,len(data)):
        minable[i].append(data[i][7])

newHeader.append(header[7])

#*********************************************#
#                   Modalidad
#*********************************************#
#Cambiar el dato de Modalidad a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    sec = data[i][8].split(' ')
    sec
    
    if(sec[1] == 'Interinstitucionales'):
        minable[i].append(2)
    
    elif(sec[1] == 'Interna'):
        minable[i].append(1)
        
    elif(sec[1] == 'Internos'):
        minable[i].append(3)
    
    elif(sec[1] == 'OPSU'):
        minable[i].append(4)

newHeader.append(header[8])

#*********************************************#
#              Semestre actual
#*********************************************#
#Se obtienen los numeros del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][9]) 
    minable[i].append(num[0])

newHeader.append(header[9])

#*********************************************#
#              Cambio de hogar
#*********************************************#
#Cambiar el dato de Cambio de habitacion a 
#numeros como lo indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][10] == 'No'):
        minable[i].append(0)
        
    elif(data[i][10] == 'Si'):
        minable[i].append(1)
    

newHeader.append(header[10])

#*********************************************#
#         Numero de materias Inscritas
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][12]) 
    minable[i].append(num[0])

newHeader.append(header[12])

#*********************************************#
#         Numero de materias Aprobadas
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][13]) 
    minable[i].append(num[0])

newHeader.append(header[13])

#*********************************************#
#         Numero de materias Retiradas
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][14]) 
    minable[i].append(num[0])

newHeader.append(header[14])

#*********************************************#
#         Numero de materias Reprobadas
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][15]) 
    minable[i].append(num[0])

newHeader.append(header[15])

#*********************************************#
#         Verificar Numero de materias
#*********************************************#
#Se verifica que el numero de materias
#aprobadas + retiradas + reprobadas
#sea menor a inscritas. En caso contrario
#se elimina la fila.
for i in xrange(0,len(data)):
    a=int(re.findall(r'\d+',data[i][13])[0])
    b=int(re.findall(r'\d+',data[i][14])[0])
    c=int(re.findall(r'\d+',data[i][15])[0])
    d=int(re.findall(r'\d+',data[i][12])[0])
    if(a+b+c > d):
        badRows.append(i)
        
#*********************************************#
#                   Promedio
#*********************************************#
#Se obtienen el promedio y se verifica que 
#el numero sea menor igual a 20
        
for i in xrange(0,len(data)):
    num = float(data[i][16]) 
    dat = str(num)
    if(num>20.0):
        dat= data[i][16][:2]+'.'+data[i][16][2:]
        dat
    minable[i].append(dat)

newHeader.append(header[16])

#*********************************************#
#                   Eficiencia
#*********************************************#
#Se obtienen la eficiencia y se verifica que 
#el numero sea menor igual a 1
        
for i in xrange(0,len(data)):
    num = float(data[i][17]) 
    dat = str(num)
    num
    if(num>1.0):
        if(num == 1000 or num == 10000):
            dat='1.0'
        else:
            dat= '0.'+data[i][17][0:]
    dat
    minable[i].append(dat)

newHeader.append(header[17])

#*********************************************#
#         Numero de materias actuales
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = re.findall(r'\d+',data[i][19]) 
    minable[i].append(num[0])

newHeader.append(header[19])

#*********************************************#
#              Realizando Tesis
#*********************************************#
#Cambiar el dato de Tesis a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][10] == 'No'):
        minable[i].append(0)
        
    elif(data[i][10] == 'Si'):
        minable[i].append(1)
    

newHeader.append(header[20])

#*********************************************#
#           Vez de Tesis
#*********************************************#
#Cambiar el dato de Vez de Tesis a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    sec = data[i][21].split(' ')
    
    if(sec[0] == 'Primera'):
        
        minable[i].append(1)
    
    elif(sec[0] == 'Segunda'):
        
        minable[i].append(2)
    
    elif(sec[0] == ''):
        
        minable[i].append('')
        
    else:
        minable[i].append(3)

newHeader.append(header[21])

#*********************************************#
#               Procedencia
#*********************************************#
#Cambiar el dato de Procedencia a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    sec = data[i][22].split(' ')
    
    if(sec[0] == 'Municipio'):
        
        minable[i].append(0)
    
    else:
        minable[i].append(1)

newHeader.append(header[22])

#*********************************************#
#               Residencia
#*********************************************#
#Cambiar el dato de Procedencia a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    sec = data[i][23].split(' ')
    
    if(sec[0] == 'Municipio'):
        
        minable[i].append(0)
    
    else:
        minable[i].append(1)

newHeader.append(header[23])

#*********************************************#
#               Residencia
#*********************************************#
#Cambiar el dato de Procedencia a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    sec = data[i][23].split(' ')
    
    if(sec[0] == 'Municipio'):
        
        minable[i].append(0)
    
    else:
        minable[i].append(1)

newHeader.append(header[23])

#*********************************************#
#              Matrimonio
#*********************************************#
#Cambiar el dato de Matrimonio a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][28] == 'No'):
        minable[i].append(0)
        
    elif(data[i][28] == 'Si'):
        minable[i].append(1)
    

newHeader.append(header[28])

#*********************************************#
#              Solicitud
#*********************************************#
#Cambiar el dato de Solicitud a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][29] == 'No'):
        minable[i].append(0)
        
    elif(data[i][29] == 'Si'):
        minable[i].append(1)
    

newHeader.append(header[29])

#*********************************************#
#              Realiza Actividad
#*********************************************#
#Cambiar el dato de Solicitud a numeros como lo
#indica el documento informe.pdf
for i in xrange(0,len(data)):
    if(data[i][31] == 'No'):
        minable[i].append(0)
        
    elif(data[i][31] == 'Si'):
        minable[i].append(1)
    

newHeader.append(header[31])

#*********************************************#
#           Monto de la Beca
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = int(re.findall(r'\d+',data[i][33])[0])
    if(num > 2000 or num < 1000):
        badRows.append(i)
    else:
        minable[i].append(num)

newHeader.append(header[33])

#*********************************************#
#           Aporte del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][34] == 'NA'):
        minable[i].append(0)    
        data[i][34] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][34])[0])
        minable[i].append(num)

newHeader.append(header[34])

#*********************************************#
#           Aporte de Fam.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][35] == 'NA'):
        minable[i].append(0)     
        data[i][35] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][35])[0])
        minable[i].append(num)

newHeader.append(header[35])

#*********************************************#
#           Aporte de Act.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][36] == 'NA'):
        minable[i].append(0)   
        data[i][36] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][36])[0])
        minable[i].append(num)

newHeader.append(header[36])

#*********************************************#
#           Aporte Total.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    a= int(re.findall(r'\d+',data[i][33])[0])
    b= int(re.findall(r'\d+',data[i][34])[0])
    c= int(re.findall(r'\d+',data[i][35])[0])
    d= int(re.findall(r'\d+',data[i][36])[0])
    total = a+b+c+d
    minable[i].append(total)

newHeader.append(header[37])

#*********************************************#
#           Gasto de Aliment.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][38] == 'NA'):
        minable[i].append(0)   
        data[i][38] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][38])[0])
        minable[i].append(num)

newHeader.append(header[38])

#*********************************************#
#           Gasto de Trans.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][39] == 'NA'):
        minable[i].append(0)   
        data[i][39] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][39])[0])
        minable[i].append(num)

newHeader.append(header[39])

#*********************************************#
#           Gasto de Medicos
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][40] == 'NA'):
        minable[i].append(0)   
        data[i][40] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][40])[0])
        minable[i].append(num)

newHeader.append(header[40])

#*********************************************#
#           Gasto de odonto.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][41] == 'NA'):
        minable[i].append(0)   
        data[i][41] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][41])[0])
        minable[i].append(num)

newHeader.append(header[41])

#*********************************************#
#           Gasto de Person.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][42] == 'NA'):
        minable[i].append(0)   
        data[i][42] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][42])[0])
        minable[i].append(num)

newHeader.append(header[42])

#*********************************************#
#           Gasto de Resid.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][43] == 'NA'):
        minable[i].append(0)   
        data[i][43] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][43])[0])
        minable[i].append(num)

newHeader.append(header[43])

#*********************************************#
#           Gasto de Materiales
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][44] == 'NA'):
        minable[i].append(0)   
        data[i][44] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][44])[0])
        minable[i].append(num)

newHeader.append(header[44])

#*********************************************#
#           Gasto de Recreacion
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][45] == 'NA'):
        minable[i].append(0)   
        data[i][45] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][45])[0])
        minable[i].append(num)

newHeader.append(header[45])

#*********************************************#
#           Otros Gastos
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][46] == 'NA'):
        minable[i].append(0)   
        data[i][46] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][46])[0])
        minable[i].append(num)

newHeader.append(header[46])

#*********************************************#
#           Gasto Total.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    a= int(re.findall(r'\d+',data[i][38])[0])
    b= int(re.findall(r'\d+',data[i][39])[0])
    c= int(re.findall(r'\d+',data[i][40])[0])
    d= int(re.findall(r'\d+',data[i][41])[0])
    e= int(re.findall(r'\d+',data[i][42])[0])
    f= int(re.findall(r'\d+',data[i][43])[0])
    g= int(re.findall(r'\d+',data[i][44])[0])
    h= int(re.findall(r'\d+',data[i][45])[0])
    j= int(re.findall(r'\d+',data[i][46])[0])
    total = a+b+c+d+e+f+g+h+j
    minable[i].append(total)

newHeader.append(header[47])

#*********************************************#
#           Carga Familiar
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = int(re.findall(r'\d+',data[i][49])[0])
    minable[i].append(num)

newHeader.append(header[49])

#*********************************************#
#           Ingreso del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][50] == 'NA' or data[i][50] ==''):
        minable[i].append(0)   
        data[i][50] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][50])[0])
        minable[i].append(num)

newHeader.append(header[50])

#*********************************************#
#           Otros Ing. del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][51] == 'NA' or data[i][51] =='' or data[i][51] =='No'):
        minable[i].append(0)   
        data[i][51] = '0'
    else:
        num = int(re.findall(r'\d+',data[i][51])[0])
        num
        minable[i].append(num)

newHeader.append(header[51])

#*********************************************#
#           Ingreso Total del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    a= int(re.findall(r'\d+',data[i][50])[0])
    b= int(re.findall(r'\d+',data[i][51])[0])
    total = a+b
    minable[i].append(total)

newHeader.append(header[52])

#*********************************************#
#           Egresos Vivienda del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][53] == 'NA' or data[i][53] ==''):
        minable[i].append(0)   
        data[i][53] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][53]))==0):
            badRows.append(i)
            data[i][53] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][53])[0])
            num
            minable[i].append(num)

newHeader.append(header[53])

#*********************************************#
#           Egresos Alimentacion del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][54] == 'NA' or data[i][54] ==''):
        minable[i].append(0)   
        data[i][54] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][54]))==0):
            badRows.append(i)
            data[i][54] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][54])[0])
            num
            minable[i].append(num)

newHeader.append(header[54])

#*********************************************#
#           Egresos Transporte del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][55] == 'NA' or data[i][55] ==''):
        minable[i].append(0)   
        data[i][55] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][55]))==0):
            badRows.append(i)
            data[i][55] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][55])[0])
            num
            minable[i].append(num)

newHeader.append(header[55])

#*********************************************#
#           Egresos Medicos del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][56] == 'NA' or data[i][56] ==''):
        minable[i].append(0)   
        data[i][56] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][56]))==0):
            badRows.append(i)
            data[i][56] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][56])[0])
            num
            minable[i].append(num)

newHeader.append(header[56])

#*********************************************#
#           Egresos Odontologicos del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][57] == 'NA' or data[i][57] ==''):
        minable[i].append(0)   
        data[i][57] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][57]))==0):
            badRows.append(i)
            data[i][57] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][57])[0])
            num
            minable[i].append(num)

newHeader.append(header[57])

#*********************************************#
#           Egresos Educativos del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][58] == 'NA' or data[i][58] ==''):
        minable[i].append(0)   
        data[i][58] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][58]))==0):
            badRows.append(i)
            data[i][58] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][58])[0])
            num
            minable[i].append(num)

newHeader.append(header[58])

#*********************************************#
#           Egresos Serv. Pub. del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][59] == 'NA' or data[i][59] ==''):
        minable[i].append(0)   
        data[i][59] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][59]))==0):
            badRows.append(i)
            data[i][59] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][59])[0])
            num
            minable[i].append(num)

newHeader.append(header[59])

#*********************************************#
#           Egresos Condominio del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][60] == 'NA' or data[i][60] ==''):
        minable[i].append(0)   
        data[i][60] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][60]))==0):
            badRows.append(i)
            data[i][60] = '0'
        else:
            num = int(re.findall(r'\d+',data[i][60])[0])
            num
            minable[i].append(num)

newHeader.append(header[60])

#*********************************************#
#           Otros Egresos del Resp.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    if(data[i][61] == 'NA' or data[i][61] ==''):
        minable[i].append(0)   
        data[i][61] = '0'
    else:
        if(len(re.findall(r'\d+',data[i][61]))==0):
            data[i][61] = '0'
            badRows.append(i)
        else:
            num = int(re.findall(r'\d+',data[i][61])[0])
            num
            minable[i].append(num)

newHeader.append(header[61])

#*********************************************#
#           Gasto Total.
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    a= int(re.findall(r'\d+',data[i][53])[0])
    b= int(re.findall(r'\d+',data[i][54])[0])
    c= int(re.findall(r'\d+',data[i][55])[0])
    d= int(re.findall(r'\d+',data[i][56])[0])
    e= int(re.findall(r'\d+',data[i][57])[0])
    f= int(re.findall(r'\d+',data[i][58])[0])
    g= int(re.findall(r'\d+',data[i][59])[0])
    h= int(re.findall(r'\d+',data[i][60])[0])
    j= int(re.findall(r'\d+',data[i][61])[0])
    total = a+b+c+d+e+f+g+h+j
    minable[i].append(total)

newHeader.append(header[62])

#*********************************************#
#               Opinion
#*********************************************#
#Se obtienen el numero del string
for i in xrange(0,len(data)):
    num = int(re.findall(r'\d+',data[i][63])[0])
    minable[i].append(num)

newHeader.append(header[63])

#*********************************************#
#            Borrar filas Malas
#*********************************************#
cont = 0
badRows = sorted(set(badRows))
for i in xrange(0,len(badRows)):
    minable.pop(badRows[i] - cont);
    cont=cont + 1

#*********************************************#
#            Crear archivo minable
#*********************************************#
final = []
final.append(newHeader)

for i in xrange(0, len(minable)):
    final.append(minable[i])

with open('minable.csv','wb') as f:
    writer = csv.writer(f)
    writer.writerows(final)



