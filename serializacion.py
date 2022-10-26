import csv
import email
import pickle
import json
class Persona:
    def __init__(self, nombre, id, email, edad):
        self.__nombre = nombre
        self.__edad = edad
        self.__email = email
        self.__id = id

    def __gt__(self, other): 
        return self.__id > other.__id

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email
    
    def get_edad(self):
        return int(self.__edad)

    # def __repr__(self) -> str:
    #     return repr(self.__id)

# archivo = "Taller_herencia.txt"
# archivo = open(archivo)
# next(archivo)
# data = archivo.read()
# lista_visitantes = data.replace('\n', ' ').split(" ")
# new_lista_visitantes = []
# for visitante in lista_visitantes:
#     visit = visitante.split("\t")
#     new_lista_visitantes.append(visit)

# gestor = []
# for visitante in new_lista_visitantes:
#     if len(visitante) != 4:
#         new_lista_visitantes.remove(visitante)
#     else:
#         gestor.append(Persona(visitante[0], visitante[1], visitante[2], visitante[3]))


# with open("serializado.pickle", "wb") as f:
#     pickle.dump(gestor, f) 

# with open("serializado.pickle", "rb") as archivo:
#   lista_personas = pickle.load(archivo)


# def ordenadosPorId(lista_invitados):
#     len(lista_invitados)
#     for i in range(len(lista_invitados)):
#         for j in range(len(lista_invitados)-i-1): 
#             if lista_invitados[j] > lista_invitados[j+1]:
#                 lista_invitados[j], lista_invitados[j+1] = lista_invitados[j+1], lista_invitados[j]
#     return lista_invitados

# print(ordenadosPorId(lista_personas))

archivo = "Taller_herencia.csv"
archivo = open(archivo)
lista_visitantes = []
reader = csv.reader(archivo)
first = True
for row in reader:
    if first:
        first = False
        continue
    lista_visitantes.append(row)
gestor =[]
for visitante in lista_visitantes:
    if len(visitante) == 1:
        visit = visitante[0].split('**')
    else:
        gestor.append(Persona(visitante[0], visitante[1], visitante[2], visitante[3]))



d = []
for i in gestor:
    d.append({"nombre":i.get_nombre(), "id":i.get_id(), "email": i.get_email(), "edad":i.get_edad()})

json_string = json.dumps(d)

json_cargado = json.loads(json_string)


for person in json_cargado:
    person["edad"] = len(person["email"])
    del person["email"]


json_string = json.dumps(json_cargado)

json_people = json.loads(json_string)