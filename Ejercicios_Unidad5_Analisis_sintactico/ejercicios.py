import re  # libreria de expresiones regulares

path = 'Codigo.js'

try:
    archivo = open(path, 'r')
except:
    print('El archivo que intentas abrir no existe')
    quit()

texto = ''

for linea in archivo:
    texto += linea


# setencia de asignacion
exp = re.compile('(\w+( |)=( |)[\d+\.\d+|\w]+);')  
result = exp.findall(texto)
for date in result:
    print("Sentencias de asignación: "  + date[0])

# Operaciones Aritmeticas basicas
exp2 = re.compile(
    '(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+);')  
result = exp2.findall(texto)
for date in result:
    print("Operaciones Aritmeticas basicas: " 
           + date[0])

# Operaciones Aritmeticas basicas
exp3 = re.compile(
    '([\d+\.\d+|\w]+[ |](\={2,3}|\>|\<|\!|\>=|\<=|\!=)[ |][\d+\.\d+|\w]+)')  
result = exp3.findall(texto)
for date in result:
    print("Expresiones Booleanas: \t"  + date[0])

# Operaciones Aritmeticas basicas
exp4 = re.compile(
    '(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\(\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+\));')  
result = exp4.findall(texto)
for date in result:
    print("Operacines Avanzadas: \t"  + date[0])

# Operaciones Aritmeticas basicas
exp5 = re.compile(
    '([if|for|while|switch|forEach].*[\(]\w.*[\)]){')  
result = exp5.findall(texto)
for date in result:
    print("Estructuras de Control: \t" + date)
