import sys
import textwrap
import requests
import time
import os

from ipm import e2e

def show(text):
	print(textwrap.dedent(text))

def show_passed():
	print('\033[92m', "    Passed", '\033[0m')

def show_not_passed(e):
	print('\033[91m', "    Not passed", '\033[0m')
	print(textwrap.indent(str(e), "    "))

def lanzo_aplicacion(path):
	process, app = e2e.run(path = path, name = None, timeout = None)
	if app is None:
		process and process.kill()
		assert False, f"There is no aplication {path} in the desktop"

	return (process, app)

def stop(process):
    if process is not None:
        process.kill()

#Devuelve una lista con los objetos que tengan dicho rol y/o nombre
def get_objects(parent, role=None, name=None):
	def _check(obj):
		return (role is None or obj.get_role_name() == role) and (name is None or obj.get_name() == name)
	return [obj for _, obj in e2e.tree_walk(parent) if _check(obj)]

def get_object(parent, role=None, name=None):
	def _check(obj):
		return (role is None or obj.get_role_name() == role) and (name is None or obj.get_name() == name)
	list = [obj for _, obj in e2e.tree_walk(parent) if _check(obj)]
	return list[0]

# FUNCIONES AUXILIARES
def veo_objeto(app, obj_role, obj_name):
	label = get_object( app, role=obj_role, name=obj_name)
	assert label and label.get_name()==obj_name

def cuento_objetos(app, obj_role, obj_name, expected_num):
	objetos = get_objects(app, role=obj_role, name=obj_name)
	num = len(objetos)
	assert objetos and num==expected_num

def find_objeto(app, role, name):
	objetos = e2e.find_all_objs(app)
	objeto_final = None
	for objeto in objetos:
		if(objeto.get_name()==name and objeto.get_role_name() == role): 
			objeto_final = objeto
			
			break
	return objeto_final 

def do(app, action, role, name):
	
	
	a=0
	num_action=0
	objeto=find_objeto(app, role, name)
	i=objeto.get_n_actions()
	for a in range(0, objeto.get_n_actions()):
		if (objeto.get_action_name(a)==action):
			num_action = a
			break
	
	objeto.do_action(num_action)

def obtengo_datos_accesos(app, userId):
	
	string_final=[]
	r = requests.get("http://localhost:8080/api/rest/user_access_log/"+userId, 
		headers={"x-hasura-admin-secret":"myadminsecretkey"})
	
	for a in range(len(r.json()['access_log'])):
		dic=[]
		dic.append(str(r.json()['access_log'][a]['temperature']))   
		dic.append(str(r.json()['access_log'][a]['timestamp'])) 
		dic.append(str(r.json()['access_log'][a]['type']))    
		dic.append(str(r.json()['access_log'][a]['facility']['name']))
		dic.append(str(r.json()['access_log'][a]['facility']['address']))
		dic.append(str(r.json()['access_log'][a]['facility']['id'])) 
		string_final.append(dic)
	return string_final

def datos_aux(string_final, userId):
	string_final2=[]
	rep=[]
	salida=[]
	salida_final=[]
	
	for a in range(len(string_final)):
		if(a%2==0):
			string_final2=[]
			string_final2.append(string_final[a][5])
			string_final2.append(string_final[a][3])
			string_final2.append(string_final[a][1])
			string_final2.append(string_final[a+1][1])
			rep.append(string_final2)
	
	for b in range(len(rep)):
		r = requests.get( "http://localhost:8080/api/rest/facility_access_log/"+rep[b][0]+"/daterange?offset=0&limit=100", 
            headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
            json={"startdate": rep[b][2], "enddate": rep[b][3]})

		for c in range(len(r.json()['access_log'])): 
			if(userId!=r.json()['access_log'][c]['user']['uuid']):
				l=0
				salida=[]
				salida.append(str(r.json()['access_log'][c]['user']['uuid']))
				salida.append(rep[c][0] + "(" +rep[c][1]+")")
				salida.append(rep[c][2]+" - "+rep[c][3])

                
			if(salida!=[]):
				l=0
				for i in range (len(salida_final)):
					if salida_final[i][0] == salida[0]:
						if salida_final[i][2] == salida[2]:
							l+=1 
				if (l==0):
					salida_final.append(salida)
	
	return salida_final

def obtengo_datos_rastreo(app, userId):
	string_final=obtengo_datos_accesos(app, userId)
	rastreo=datos_aux(string_final, userId)
	return rastreo

def obtengo_datos_rastreo_filtrado(userId, finicio, ffin):
	
    lug_final=[]
    string_final=[]

    r = requests.get( "http://localhost:8080/api/rest/user_access_log/"+userId+"/daterange", 
        headers={"x-hasura-admin-secret":"myadminsecretkey"},
		json={"startdate": finicio, "enddate": ffin})
    
    for a in range(len(r.json()['access_log'])):
        dic=[]
        dic.append(str(r.json()['access_log'][a]['temperature']))   
        dic.append(str(r.json()['access_log'][a]['timestamp'])) 
        dic.append(str(r.json()['access_log'][a]['type']))    
        dic.append(str(r.json()['access_log'][a]['facility']['name']))
        dic.append(str(r.json()['access_log'][a]['facility']['address']))
        dic.append(str(r.json()['access_log'][a]['facility']['id'])) 
        string_final.append(dic)
        lug_final.append((str(r.json()['access_log'][a]['facility']['id'])))
		
    result=datos_aux(string_final, userId)
    
    return result

def obtengo_datos_iniciales():
	
    string_final=[]
    
    r = requests.get("http://localhost:8080/api/rest/users", 
        headers={"x-hasura-admin-secret":"myadminsecretkey"})
       
        
    for a in range(len(r.json()['users'])):
        dic=[]
        dic.append(str(r.json()['users'][a]['uuid']))         
        dic.append(str(r.json()['users'][a]['name']))
        dic.append(str(r.json()['users'][a]['surname']))
        dic.append(str(r.json()['users'][a]['email']))
        dic.append(str(r.json()['users'][a]['phone']))
        dic.append(str(r.json()['users'][a]['is_vaccinated']))
        string_final.append(dic)
            
    return string_final

def obtengo_datos_iniciales_filtrados(nombre, apellido):
	string_final=[]
	if nombre is not None:
		if apellido is not None:
			r = requests.get("http://localhost:8080/api/rest/user?name="+nombre+"&surname="+apellido, 
                headers={"x-hasura-admin-secret":"myadminsecretkey"})
		else:
			r = requests.get("http://localhost:8080/api/rest/user?name="+nombre, 
                headers={"x-hasura-admin-secret":"myadminsecretkey"})

	for a in range(len(r.json()['users'])):
            dic=[]
            dic.append(str(r.json()['users'][a]['uuid']))         
            dic.append(str(r.json()['users'][a]['name']))
            dic.append(str(r.json()['users'][a]['surname']))
            dic.append(str(r.json()['users'][a]['email']))
            dic.append(str(r.json()['users'][a]['phone']))
            dic.append(str(r.json()['users'][a]['is_vaccinated']))
            if ((dic[1]==nombre) & (dic[2]==apellido)):
                    string_final.append(dic)
    
	return string_final

#PRUEBAS

def then_prueba1(ctx):

	show("______________________________")
	show("TEST COMPROBACIÓN ELEMENTOS")
	show("______________________________")
	
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	show("""
		THEN aparece label principal ventana 1""")

	try:
		veo_objeto(ctx[1], "label", "CONSULTAR INFORMACIÓN PERSONAL EN EL SISTEMA")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	
	show("""
		THEN aparece label principal ventana 2""")

	try:
		veo_objeto(ctx[1], "label", "ACCESOS A INSTALACIONES")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
		THEN aparece label principal ventana 3""")

	try:
		veo_objeto(ctx[1], "label", "ALERTAS COVID")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparecen todos los botones buscar """)

	try:
		veo_objeto(ctx[1], 'push button', 'Buscar fechas')
		veo_objeto(ctx[1], 'push button', 'Busca Nombre')
		show_passed()
	except Exception as e:
		show_not_passed(e)


	show("""
	THEN aparece la barra de busqueda """)

	try:
		cuento_objetos(ctx[1], "text", "Search bar", 1)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	
	show("""
	THEN aparecen todos los botones de retroceso""")

	try:
		veo_objeto(ctx[1], "push button", "Volver1")
		cuento_objetos(ctx[1], "push button", "Volver", 2)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparecen todos los botones de rastrear""")

	try:
		cuento_objetos(ctx[1], "push button", "Rastrear", 1)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparecen todos los botones de 'antes' de la paginacion""")

	try:
		veo_objeto(ctx[1], 'push button', "Antes1")
		veo_objeto(ctx[1], 'push button', "Antes 2")
		veo_objeto(ctx[1], 'push button', "Antes 3")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparecen todos los botones de 'despues' de la paginacion""")

	try:
		veo_objeto(ctx[1], 'push button', "Despues1")
		veo_objeto(ctx[1], 'push button', "Despues 2")
		veo_objeto(ctx[1], 'push button', "Despues 3")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparece el label Start Date y su entrada""")

	try:
		veo_objeto(ctx[1], "label", "Start date:")
		cuento_objetos(ctx[1], "text", "Start date", 1)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparece el label End Date y su entrada""")

	try:
		veo_objeto(ctx[1], "label", "End date:")
		cuento_objetos(ctx[1], "text", "End date", 1)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	THEN aparecen los treeviews""")

	try:
		veo_objeto(ctx[1], "table", "string_treeview")
		veo_objeto(ctx[1], "table", "string_treeview3")
		show_passed()
	except Exception as e:
		show_not_passed(e)
	
	stop(ctx[0])

#FUNCIOMES VISTA 1

def aparecen_datos_en_la_tabla(app, datos, n, y, nombre, a):
	
	table = find_objeto(app, 'table', nombre)
		
	if (len(datos)-y*n<y):
		if(len(datos)-y*n<y):
			x=len(datos)-y*n
		else:
			x=0
	else:
		x=y

	for i in range (x):
		for j in range(a):
			assert datos[i+y*(n-1)][j] == table.get_accessible_at(i, j).get_text(0,-1)

def los_datos_de_la_tabla_son_correctos(app, datos, n, y, a):
	if (len(datos)-y*n<y):
		if(len(datos)-y*n<y):
			x=len(datos)-y*n
		else:
			x=0
	else:
		x=y
	
	for i in range (x):
		for w in range (a):
			nombre=datos[i+y*(n-1)][w]
			veo_objeto (app,'label', nombre)
	
def when_presiono_despues1(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', "Despues1")

def when_presiono_antes1(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', "Antes1")


def when_busco_un_nombre(app, nombre):
	entry = find_objeto(app, role='text', name="Search bar")
	assert entry is not None
	entry.set_text_contents(nombre)
	time.sleep(1.0)
	do(app, 'click', 'push button', 'Busca Nombre')
	busco=nombre.split()
	return busco

def when_presiono_volver(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Volver1')

def then_prueba2(ctx):
	numpag1 = 1
	show("______________________________")
	show("TEST COMPROBACIÓN VISTA 1")
	show("______________________________")

	show("""
		GIVEN he lanzado la aplicación""")
	
	ctx = lanzo_aplicacion(ctx[2])

	show("""
		THEN los datos de la primera tabla son correctos""")

	try:
		datos=obtengo_datos_iniciales()
		los_datos_de_la_tabla_son_correctos(ctx[1], datos, numpag1, 15, 6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
		WHEN presiono el boton Despues de la aplicación
		THEN muestra los siguientes elementos""")


	try:
		numpag1+=1
		when_presiono_despues1(ctx[1])
		datos=obtengo_datos_iniciales()
		los_datos_de_la_tabla_son_correctos(ctx[1], datos, numpag1, 15, 6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
		WHEN presiono el boton Antes de la aplicación
		THEN muestra los anteriores elementos""")

	try:
		numpag1-=1
		when_presiono_antes1(ctx[1])
		datos=obtengo_datos_iniciales()
		los_datos_de_la_tabla_son_correctos(ctx[1], datos, numpag1, 15, 6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
		WHEN busco el nombre 'Arturo Blanco'
		THEN solo muestra a 'Arturo Blanco'""")

	try:
		nombre = "Arturo Blanco"
		busco=when_busco_un_nombre(ctx[1], nombre)
		datos=obtengo_datos_iniciales_filtrados(busco[0],busco[1])
		los_datos_de_la_tabla_son_correctos(ctx[1], datos, numpag1, 15, 6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
		WHEN presiono el botón volver
		THEN vuelve a mostrar a todas las personas""")

	try:
		datos=obtengo_datos_iniciales()
		when_presiono_volver(ctx[1])
		los_datos_de_la_tabla_son_correctos(ctx[1], datos, numpag1, 15, 6)
		show_passed()
	except Exception as e:
		show_not_passed(e)
	
	stop(ctx[0])

#FUNCIONES VISTA 2


def when_presiono_el_boton_acceso(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Acceso1')

def when_presiono_el_boton_despues(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Despues 2')

def when_presiono_el_boton_antes(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Antes 2')

def then_prueba3(ctx):
	numpag=1
	show("______________________________")
	show("TEST COMPROBACIÓN VISTA 2")
	show("______________________________")
	
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	
	show("""
		WHEN peresiono el boton Acceso de la primera fila de la tabla
		THEN aparece los accesos de la persona seleccionada en la tabla""")
	
	

	try:
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		when_presiono_el_boton_acceso(ctx[1])
		datos=obtengo_datos_accesos(ctx[1], userId)
		
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 20, 'string_treeview',6)
		show_passed()
	except Exception as e:
		show_not_passed(e)
	
	show("""
	WHEN presiono el boton Despues de la paginacion
	THEN Muestra las siguientes personas""")
	try:
		numpag+=1
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		when_presiono_el_boton_despues(ctx[1])
		datos=obtengo_datos_accesos(ctx[1], userId)
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 20, 'string_treeview',6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	WHEN presiono el boton Antes de la paginacion
	THEN Muestra las anteriores personas""")	
	try:
		numpag-=1
		when_presiono_el_boton_antes(ctx[1])
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		datos=obtengo_datos_accesos(ctx[1], userId)
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 20, 'string_treeview',6)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	stop(ctx[0])

#FUNCIONES VISTA 3

def when_presiono_el_boton_rastreo(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Rastrear')

def when_presiono_despues(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Despues 3')
	

def when_presiono_antes(app):
	time.sleep(1.0)
	do(app, 'click',  'push button', 'Antes 3')

def when_filtro_por_fechas(app, fechainicio, fechafin):
	entry = find_objeto(app, role='text', name='Start date')
	assert entry is not None
	entry.set_text_contents(fechainicio)
	entry2 = find_objeto(app, role='text', name='End date')
	assert entry is not None
	entry2.set_text_contents(fechafin)

	time.sleep(1.0)
	do(app, 'click', 'push button', 'Buscar fechas')

def then_prueba4(ctx):
	numpag=1
	show("______________________________")
	show("TEST COMPROBACIÓN VISTA 3")
	show("______________________________")
	
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])

	show("""
	WHEN presiono el botón rastreo y filtro por fechas
	THEN Muestra los contactos ocurridos entre esas fechas""")	
	try:
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		numpag=1
		when_presiono_el_boton_acceso(ctx[1])
		when_presiono_el_boton_rastreo(ctx[1])
		fechainicio="01/01/2021"
		fechafin="12/31/2021"
		when_filtro_por_fechas(ctx[1], fechainicio, fechafin)
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		
		datos=obtengo_datos_rastreo_filtrado(userId, fechainicio, fechafin)
		
		
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 15, "string_treeview3", 3)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	WHEN presiono el boton Despues de la paginacion
	THEN Muestra las siguientes personas""")
	try:
		numpag+=1
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		when_presiono_despues(ctx[1])
		datos=obtengo_datos_rastreo_filtrado(userId, fechainicio, fechafin)
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 15, 'string_treeview3',3)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	show("""
	WHEN presiono el boton Antes de la paginacion
	THEN Muestra las anteriores personas""")	
	try:
		numpag-=1
		when_presiono_antes(ctx[1])
		userId="deca9539-3801-4df3-bdcc-d16c629c9f2d"
		datos=obtengo_datos_rastreo_filtrado(userId, fechainicio, fechafin)
		aparecen_datos_en_la_tabla(ctx[1], datos, numpag, 15, 'string_treeview3',3)
		show_passed()
	except Exception as e:
		show_not_passed(e)

	stop(ctx[0])

#FUNCIONES TEST DE ERRORES
def then_muestra_un_error(app, msg):
    dialog = e2e.find_obj(app, role='alert', name= 'Error')
    assert (dialog is not None) or (dialog.get_name()=='Error')
    find_objeto(app, 'label',msg)


def then_prueba5(ctx):
	show("______________________________")
	show("TEST COMPROBACIÓN ERROR BUSCAR NOMBRE NO EN BD")
	show("______________________________")
	
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	
	show("""
	WHEN introduzco un nombre que no está en la BD
	THEN Muestra un error""")
	try:
		
		nombre = "Daniel Iglesias"
		when_busco_un_nombre(ctx[1], nombre)
		then_muestra_un_error(ctx[1],"No se ha encontrado en la base de datos")
		time.sleep(1)
		show_passed()
	except Exception as e:
		show_not_passed(e)
	stop(ctx[0])

def then_prueba6(ctx):
	show("______________________________")
	show("TEST COMPROBACIÓN ERROR BUSCAR NOMBRE MAL")
	show("______________________________")
	
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
		
	show("""
	WHEN introduzco mal un nombre
	THEN Muestra un error""")	
	try:
		time.sleep(1)
		do(ctx[1], 'click',  'push button', 'Volver1')
		time.sleep(1)
		nombre = "Daniel Iglesias Moris"
		when_busco_un_nombre(ctx[1], nombre)
		then_muestra_un_error(ctx[1],"No se ha introducido de la manera correcta")
		
		show_passed()
	except Exception as e:
		show_not_passed(e)
	stop(ctx[0])
	
	
	
	
	
def then_prueba7(ctx):
	show("______________________________")
	show("TEST COMPROBACIÓN ERROR MAL FORMATO DE LA FECHA")
	show("______________________________")
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	show("""
	WHEN introduzco mal formato de la fecha
	THEN Muestra un error""")
	try:
		when_presiono_el_boton_acceso(ctx[1])
		when_presiono_el_boton_rastreo(ctx[1])
		fechainicio="01-01-2021"
		fechafin="12/31/2021"
		when_filtro_por_fechas(ctx[1], fechainicio, fechafin)
		then_muestra_un_error(ctx[1],"Fecha incorrecta")
		
		show_passed()
	except Exception as e:
		show_not_passed(e)
	stop(ctx[0])

def then_prueba8(ctx):
	show("______________________________")
	show("TEST COMPROBACIÓN ERROR MAL FECHA DE INICIO MENOR QUE LA DE FIN")
	show("______________________________")
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	show("""
	WHEN introduzco la fecha de fin menor que la de inicio
	THEN Muestra un error""")
	try:
		when_presiono_el_boton_acceso(ctx[1])
		when_presiono_el_boton_rastreo(ctx[1])
		fechainicio="12/31/2021"
		fechafin="01/01/2021"
		when_filtro_por_fechas(ctx[1], fechainicio, fechafin)
		then_muestra_un_error(ctx[1],"Fecha incorrecta")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	stop(ctx[0])

def then_prueba9(ctx):
	show("______________________________")
	show("TEST COMPROBACIÓN BASE DE DATOS DESCONECTADA")
	show("______________________________")
	show("""
		GIVEN he lanzado la aplicación""")
	ctx = lanzo_aplicacion(ctx[2])
	show("""
	WHEN la base de datos esta desconectada
	THEN Muestra un error""")
	try:
		nombre="Arturo Blanco"
		
		when_busco_un_nombre(ctx[1], nombre)
		os.system("systemctl stop docker.socket")
		os.system("systemctl stop docker.service")
		time.sleep(1)
		do(ctx[1], 'click',  'push button', "Volver1")
		time.sleep(3)
		then_muestra_un_error(ctx[1],"Error para comunicarse con la base de datos")
		show_passed()
	except Exception as e:
		show_not_passed(e)

	stop(ctx[0])

if __name__ == '__main__':
		path = sys.argv[1]
		initial_ctx = (None, None, path)

		then_prueba1(initial_ctx)  #Todos los elementos estan en las vistas
		then_prueba2(initial_ctx)  #La vista 1 funciona
		then_prueba3(initial_ctx)
		then_prueba4(initial_ctx) #La vista 3 funciona
		then_prueba5(initial_ctx)
		then_prueba6(initial_ctx)
		then_prueba7(initial_ctx)
		then_prueba8(initial_ctx)
		then_prueba9(initial_ctx)