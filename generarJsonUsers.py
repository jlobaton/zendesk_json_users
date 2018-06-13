#!/usr/bin/python
# -*- coding: utf-8 -*-
# Bash que permite transformar de CSV a Json 
# Para usarlo en la API Console de Zendesk

# El archivo csv debe de tener los campos tal cual como esta en zendesk
# para los campos personalizados:
# tiene que anteceder el nombre del campo con "custom_fields"
#
# Ej: custom_fields.nombre_campo
#

import sys, argparse, getopt
import csv
import json
import codecs
import os
import re
import pyperclip
reload(sys)

def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

def ClipBoard(file): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
  	    #print 'cat '+file+' | xclip -selection clipboard'
      	os.system('cat '+file+' | xclip -selection clipboard')
    elif os.name == ("ce", "nt", "dos"):
        os.system ("")

#sys.setdefaultencoding('utf8')

def salir(mensaje, leer):
	#clear()
	print "--- ERROR EN LA VALIDACION --"
	print "Linea: " + str(leer.line_num)
	print "Mensaje: "+mensaje
	print "-----------------------------"
	#break
	exit()

def verificar_correo(correo):
	valido = False
	if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
		valido = True

	return valido


def generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output):
	#print (custom_fields)
	#exit()
##### bueno
	if len(custom_fields) > 0:
		if campo == "custom_field_options":
			df = []
			df.append(custom_fields)  
			row_json[campo] = df
			cabecera[migrar] = row_json
			

			#cabecera = custom_fields
			row_json[campo] = custom_fields
 
			output.append(row_json)
			cabecera[migrar] = output #row_json			
			#exit()
		else:
			row_json[campo] = custom_fields
#######
	if campo == "custom_field_options":
		df = []
		df.append(row_json)  
		#row_json[campo] = df
		cabecera[migrar] = df
		
		print row_json
		#exit
		#cabecera = custom_fields
		row_json[campo] = custom_fields

		output.append(row_json)
		cabecera[migrar] = output #row_json			
		#exit()
	else:
		df = []
		df.append(row_json)  
		output.append(row_json)
		cabecera[migrar] = output #row_json
	return cabecera


def generar_jsonv1(row_json,campo,custom_fields,cabecera,migrar,output):
	print (campo)
	exit()
##### bueno
	if len(custom_fields) > 0:
		if campo == "custom_field_options":
			df = []
			df.append(custom_fields)  
			row_json[campo] = df
			cabecera[migrar] = row_json
			
			print custom_fields

			#cabecera = custom_fields
			#row_json[campo] = custom_fields
 
			#output.append(row_json)
			#cabecera[migrar] = output #row_json			
			exit()
		else:
			row_json[campo] = custom_fields
#######
	else:
		df = []
		df.append(row_json)  
		output.append(row_json)
		cabecera[migrar] = output #row_json
	return cabecera

def generar_archivo(output,archivo,i):
	file = archivo+`i`+'.json'
	salida = open(file,'w')
	#print salida
	json.dump(output, 
					salida, 
					indent=2, 
					sort_keys=False,
					encoding="utf-8",
					ensure_ascii=False)
	#pyperclip.copy(sali|da)
	#Copia al Portapapeles el resultado del Archivo
	ClipBoard(file)

	#return archivo+`i`+'.json'
	return file

def recortar(palabra, buscar):
	palab = palabra.strip()
	posicion = palab.index(buscar)
	tamano = len(palab)
	return palab[posicion+1:tamano]


def procesar(archivo,row,option):
	entrada = open(archivo+'.csv','r')
	mensaje = "Archivo: "
	migrar = option #'users'
	filtrar2 = ''
	#filtrar1 = ''
	campo = ''	
	campo2 = ''	

	if migrar == 'users': 
		filtrar1 = 'custom_fields'  #PARAMETRO PARA FILTRAR EL CAMPO FIELDS
		campo = 'user_fields'  #CAMPO QUE VA A COLOCAR COMO EL NOMBRE DEL ARREGLO

		filtrar2 = 'tags'	
		campo2 = 'tags'

	elif migrar == 'gm': 
		filtrar1 = 'custom_fields'
		migrar = 'group_memberships'  

	elif migrar == 'tickets' :  #tickets
		filtrar1 = 'custom_fields' 	
		campo1 = 'custom_fields'

		filtrar2 = 'comment' 	
		campo2 = 'comment'

	elif migrar == 'groups':
		filtrar1 = 'custom_fields' 	
		campo = 'custom_fields'

	elif migrar == 'organizations':
		filtrar1 = 'custom_fields' 	
		campo = 'custom_fields'

	elif migrar == 't-cfo':
		migrar = 'ticket_field'
		filtrar1 = 'custom_field_options' 	
		campo = 'custom_field_options'


	output = []
	leer = csv.DictReader(entrada)
	fieldnames = leer.fieldnames
	id_fieldnames = ('','','','0001','0002','0003','0003','0003','0003','0003','0003','0003','0003');
	j = 0
	i = 0

	for valor in leer:			
		cabecera = {}
		row_json = {}
		row_tags = []
		custom_fields = {}

		for field in fieldnames:
			#Validaciones
			if field.find('email') >= 0 :
				if (verificar_correo(valor[field]) == False):
					salir("Error en el Correo",leer)

			#fin
			
			# TICKET's
			if migrar == 'tickets':
				if field.find(filtrar1) >= 0:   #custom_fields
					#custom_fields[recortar(field,'.')] = valor[field]
					custom_fields["id"] = recortar(field,'.')
					custom_fields["value"] = valor[field]
					#custom_fields = {}
				 	campo = campo1
				 	#row_json[campo] = custom_fields
				 	#row_json['id'] = campo
				 	#print custom_fields
				 	#exit()

				elif field.find(filtrar2) >= 0: #comment
					custom_fields["body"] = valor[field]
					#print custom_fields["body"]
					#exit()
					#custom_fields = {}
					campo = campo2
					row_json[campo] = custom_fields
					#print custom_fields			
				
				else:
					row_json[field] = valor[field]

			# USUARIOS
			else: 
			#migrar == 'users' or migrar == 'groups' or migrar == 'organizations':
				if field.find(filtrar1) >= 0:  
					custom_fields[recortar(field,'.')] = valor[field]
					#campo = campo

				else:

					if filtrar2 and field.find(filtrar2) >= 0: #tags
						row_tags.append(valor[field])
						campo = campo2
						row_json[campo] = row_tags

					if migrar == 'ticket_field':  #ticket_field_options
						# funciona custom_fields[field] = valor[field]
						row_json[field] = valor[field]
					else:
						row_json[field] = valor[field]


			#row_json[field] = valor[field]

		if (i >= int(row)):
			j = j+1
			i = 0	
			file = generar_archivo(arch,archivo,j)
			print "/// "+mensaje+file
			output = []
			arch = generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output)
		else:	
			arch = generar_jsonv2(row_json,campo,custom_fields,cabecera,migrar,output)
		
		i=i+1

	j = j+1
	file = generar_archivo(arch,archivo,j)
	return "/// "+mensaje+file


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
parser.add_argument("-f", "--file", help="Nombre de archivo CSV a procesar")
parser.add_argument("-r", "--row", help="Cuantos Registros se va a Generar por archivo")
parser.add_argument("-o", "--option", help="Debe especificar si es users, tickets, groups, organzation")

args = parser.parse_args()
clear()

#group_memberships.json
# {
#   "group_membership": 
#     {
#       "user_id":    363155019994,
#       "group_id":   360001035554,
#       "default":    true
#     }
# }

if args.option == 'users': 
		url = 'users/create_many.json  -  users/create_or_update_many.json'

elif args.option == 'tickets' :  
		url = 'tickets.json'

elif args.option == 'groups':
		url = 'groups.json'

elif args.option == 'organizations':
		url = 'organizations/create_many.json'

elif args.option == 't-cfo':
		url = 'ticket_fields/_id_.json'; 

elif args.option == 'gm':
		url = 'group_memberships/create_many.json'; 


print "///////////////////////////////////////////////////////"
print "///"
print "/// API: https://developer.zendesk.com/requests/new"
print "/// URL: "+url
print procesar(args.file, args.row, args.option)
print "/// Use Ctrl + V y para pegarlo en la API Console"
print "///"
print "//////////////////////////////////////////////////////"

