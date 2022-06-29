import datetime
import gettext
import os
import time
import threading
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GObject

_ = gettext.gettext

import qrcode
from controller import Controller

class View:

    @classmethod
    def main(Cls):
        Gtk.main()

    @classmethod
    def main_quit(cls, w, e):
        Gtk.main_quit()
    
    #Concurrencia
    def finaliza_con_error(self, msg):
        # Se debe detener al spinner.
       if(v.opcon==1):
        self.spinner.stop()
       else:
         self.spinner2.stop()  
        # Ejecutamos las acciones después de que se haya llevado a cabo
        # la tarea larga.
       print(msg)
       v.show_error("Error para comunicarse con la base de datos")
    
    
    def finalizado(self, msg, concu):
		# Se debe detener al spinner.
       if(v.opcon==1):
        self.spinner.stop()
       else:
         self.spinner2.stop()

       # Se espera a que el threa creado termine su ejecución.
       self.runner.join()
       
        # Ejecutamos las acciones después de que se haya llevado a cabo
        # la tarea larga.
       print(msg)
       v.lista2=v.controller.result2
       v.second_screen.destroy()
       v.second_screen = Gtk.VBox(spacing=10, margin=15)
       v.segundaventana()
       v._show_screen(2)
    
    def aux_concu(self):
        try:
            v.controller.datos_inicio2(v.controller, v.uuid, v.min2)
        except Exception as err:
            GLib.idle_add(self.finaliza_con_error, "Ha ocurrido un error")
        GLib.idle_add(self.finalizado, "El tiempo de espera ha finalizado",1)

    def finalizado2(self, msg, concu):
		# Se debe detener al spinner.
       self.spinner2.stop()

       # Se espera a que el threa creado termine su ejecución.
       self.runner.join()
       
        # Ejecutamos las acciones después de que se haya llevado a cabo
        # la tarea larga.
       print(msg)
       v.lista3=v.controller.result_date
       v.pagmax3=len(self.controller.result_date)/self.elempag3
       v.third_screen.destroy()
       v.third_screen = Gtk.VBox(spacing=10, margin=15)
       v.terceraventana()
       v._show_screen(3)
    
    def aux_concu2(self):
        try:
            v.controller.datos_inicio3(v.controller, v.uuid, v.min3)
        except Exception as err:
            GLib.idle_add(self.finaliza_con_error, "Ha ocurrido un error")
        
        GLib.idle_add(self.finalizado2, "El tiempo de espera ha finalizado",1)

    def concu(self):
        v.opcon=1
        v.runner = threading.Thread(target=v.aux_concu)
        v.spinner.start()
        v.runner.start()
    
    def concu2(self):
        v.opcon=2
        v.runner = threading.Thread(target=v.aux_concu)
        v.spinner2.start()
        v.runner.start()
    
    def aux_concu3(self):
        try:
            self.error=False
            if(v.filtro):
                v.controller.on_searchbar_click(v.controller, v.nombre,v.apellido)
            else:
                v.controller.datos_inicio(v.controller, v.min)
        except Exception as err:
            self.error=True
            GLib.idle_add(self.finaliza_con_error, "Ha ocurrido un error")
        GLib.idle_add(self.finalizado3, "El tiempo de espera ha finalizado",1)

   
    def finalizado3(self, msg, concu):
		# Se debe detener al spinner.
       self.spinner.stop()

       # Se espera a que el threa creado termine su ejecución.
       self.runner.join()
       
        # Ejecutamos las acciones después de que se haya llevado a cabo
        # la tarea larga.
       print(msg)
       if(self.error==False):
        if(v.filtro):
           v.lista=v.controller.result_bar
        else:
           v.lista=v.controller.result
        if(v.lista is None):
           v.show_error("No se ha encontrado el nombre en la BD")
        else:
           v.first_screen.destroy()
           v.first_screen = Gtk.VBox(spacing=10, margin=15)
           v.primeraventana()
           
       v._show_screen(1)
    
        
    def concu3(self):
        v.opcon=1
        v.runner = threading.Thread(target=v.aux_concu3)
        v.spinner.start()
        v.runner.start()
    
    def aux_concu4(self):
        try:
            v.controller.on_searchdate_click(v.controller,v.fechaini+"T00:00:00.277923+00:00",v.fechafin+"T23:59:59.277923+00:00",v.min3)
        except Exception as err:
            GLib.idle_add(self.finaliza_con_error, "Ha ocurrido un error")
        GLib.idle_add(self.finalizado2, "El tiempo de espera ha finalizado",1)

    
    def concu4(self):
        v.runner = threading.Thread(target=v.aux_concu4)
        v.spinner2.start()
        v.runner.start()

    def aux_concu5(self):
        try:
            v.controller.on_searchdate_click(v.controller,v.fechaini+"T00:00:00.277923+00:00",v.fechafin+"T23:59:59.277923+00:00",v.min3)
        except Exception as err:
            GLib.idle_add(self.finaliza_con_error, "Ha ocurrido un error")
        GLib.idle_add(self.finalizado2, "El tiempo de espera ha finalizado",1)
    
    def concu5(self):
        v.runner = threading.Thread(target=v.aux_concu5)
        v.spinner3.start()
        v.runner.start()


    # Funciones para los botones
    def click_acceso(self):     #Funcion a la que se llama cuando se clica al boton de acceso
        v.uuid = v.lista[self.value][0]
        v.concu()

    def click_rastreo(self):                                                    #funcion que se llama al clicar al boton de rastreo
        
        v.concu4()
        
    def click_volver(self):                                                     #funcion que permite volver a la pagina inicial
        v._show_screen(1)
    
    def termina_funcion(self):
       v.lista2= v.controller.result2  #almacenamos los datos de donde estuvo
       v.hbox2_1.destroy()
       v.hbox2_3.destroy()
       v.hbox2_2.destroy()
       v.segundaventana()
       v._show_screen(2)
    
    def click_antes(self):                                                      #funcion que se ejecuta al clicar en antes(paginacion)
        if v.numpag != 1:                                                       #comprueba que no sea la primera pagina
           v.numpag -= 1
           v.min=(v.numpag-1)*v.elempag
           v.concu3()                                                  

    def click_despues(self):                                                    #funcion que se ejecuta al clicar a despues(paginacion)
        if v.numpag < v.pagmax:                                                #comprueba que no se pase de max pag    
           v.numpag += 1
           v.min=(v.numpag-1)*v.elempag
           v.concu3()    
        
    def click_antes2(self):                                                     #mismo que click antes
        if v.numpag2 != 1:                                                       #comprueba que no sea la primera pagina
           v.numpag2 -= 1
           v.min2=(v.numpag2-1)*v.elempag2
           v.concu2()
    
    def click_despues2(self):                                                   #mismo que click despues
        if v.numpag2 < v.pagmax2:                                                #comprueba que no se pase de max pag    
           v.numpag2 += 1
           v.min2=(v.numpag2-1)*v.elempag2 
           v.concu2()

    def click_antes3(self):                                                     #mismo que click antes
        
        if v.numpag3 != 1:
           v.numpag3 -= 1
           v.min3=(v.numpag3-1)*v.elempag3
           v.concu5()

    def click_despues3(self):                                                    #mismo que click despues
        if v.numpag3 < v.pagmax3:                                                #comprueba que no se pase de max pag    
           v.numpag3 += 1
           v.min3=(v.numpag3-1)*v.elempag3
           v.concu5()
    
    def click_volver_persona(self):                                             #funcion que sirve para volver a la pagina de inicio despues de buscar a alguien
        v.filtro=False
        v.concu3()

    def click_cod(self):
        v.j = self._value
        v._show_fourth_screen()

    def bar_searching(widget):                                                  #atribuye el valor del texto introducido por la barra de busqueda
        v.busqueda = widget.get_text()

    def date_searching(widget):                                                 #atribuye el valor del texto introducido por la label de fecha inicio
        v.fechaini = widget.get_text()

    def date_searching2(widget):                                                #atribuye el valor del texto introducido por la label de fecha fin
        v.fechafin = widget.get_text()
    
    def busca(self):                                                            #funcion del boton buscar
                    
           texto = v.busqueda.split()                                           #spliteamos el texto introducido
           if(len(texto)!=2):                                                   #comprobacion del formato
               v.show_error("No se ha introducido de la manera correcta")       #funcion de error
               v._show_screen(1)
           else:
            v.nombre = texto[0]                                           
            v.apellido = texto[1]
            v.resultado=[]
            v.filtro=True
            v.concu3()

    def buscafecha(self):                                                       #funcion de buscar fecha
        v.valido=0
        v.validate(v.fechaini)
        v.validate(v.fechafin)
        v.fechainit=v.fechaini.split('-')
        v.fechafint=v.fechafin.split('-')

        if(v.valido==2):

            if(v.fechainit[0]> v.fechafint[0] or v.fechaini is None or v.fechafin is None):
                v.show_error("Fecha incorrecta") 
            else:
                if((v.fechainit[0]==v.fechainit[0]) & (v.fechainit[1]>v.fechafint[1])):
                    v.show_error("Fecha incorrecta")
                else:
                    if((v.fechainit[0]==v.fechainit[0]) & (v.fechainit[1]==v.fechafint[1]) & (v.fechainit[2]>v.fechafint[2])):
                        v.show_error("Fecha incorrecta")
                    else:
                        v.concu5()

    def validate(self,date_text):                                               #valida el formato de la fecha
        try:
            datetime.datetime.strptime(date_text, "%Y-%m-%d")
            v.valido+=1
        except ValueError:
            v.show_error("Formato incorrecto")

    
    
    def click_qr(self):                                                         #genera el qr
        
        uuid = self.lista[self.j][0]                                      #separamos uuid, nombre y apellido
        nombre = self.lista[self.j][1]
        apellido = self.lista[self.j][2]
        
        data=uuid + "," + nombre + "," + apellido
        

        qr = qrcode.QRCode(                                                     #funcion del qr
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
                                                                                #se añade el qr a la ventana
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(os.getcwd()+'/qrcode.png')
    
    
    # Widgets 1
    def searchbar(self, text):
        self.busqueda=""
        self.search_bar=Gtk.SearchEntry(text="")
        self.search_bar.set_placeholder_text((text))
        self.search_bar.connect('search-changed',self.__class__.bar_searching)  #conecta con la funcion bar_searching
        search_bar_accesible=self.search_bar.get_accessible()
        search_bar_accesible.set_name("Search bar")

    def searchbutton(self):
        self.search_button=Gtk.Button(label=_("Buscar"))
        self.search_button.connect("clicked", self.__class__.busca)
        start_search_button=self.search_button.get_accessible()
        start_search_button.set_name("Busca Nombre")
    
    def beforebutton(self):
        self.before_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before_button.connect("clicked", self.__class__.click_antes)
        before_accessible = self.before_button.get_accessible()
        before_accessible.set_name("Antes1")
        self.hbox1_2.pack_start(self.before_button, False, False, 0)
    
    def paglabel(self):
        self.text_pag=f"Página {self.numpag}"
        self.pag_label=Gtk.Label()
        self.pag_label.set_text(self.text_pag)
        self.hbox1_2.pack_start(self.pag_label, True, True, 0)
    
    def afterbutton(self):
        self.after_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after_button.connect("clicked", self.__class__.click_despues)
        after_accessible = self.after_button.get_accessible()
        after_accessible.set_name("Despues1")
        self.hbox1_2.pack_start(self.after_button, False, False, 0)
    
    def volverbutton(self):
        self.backp=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        self.backp.connect("clicked", self.__class__.click_volver_persona)
        volver_accessible = self.backp.get_accessible()
        volver_accessible.set_name("Volver1")
        self.hbox1_2.pack_start(self.backp,False, False, 0)
    
    def construirspinner(self):
        self.spinner = Gtk.Spinner()
        spinner_accessible = self.spinner.get_accessible()
        spinner_accessible.set_name("Spinner1")
        self.hbox1_2.pack_start(self.spinner, False, False, 0)
    
    #Primera ventana
    def input1(self):
        self.hbox1_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
    
    def titulo(self, tit):
        self.label_prin=Gtk.Label()
        self.label_prin.set_margin_top(10)
        self.tit = tit
        self.label_prin.set_markup("<big>" + tit + "</big>")

    def fhbox11(self):                                                      #crea la primera caja con la barra de busqueda
        self.searchbar("Buscar por nombre y apellidos")  
        self.searchbutton()      
        self.hbox1_1.pack_start(self.search_bar, False, False, 0)
        self.hbox1_1.pack_start(self.search_button, False, False, 0)
    
    def iniciar_variables_tabla(self):
        self.listoflists = []
        self.list=[]
        self.j=0
        self.pagmax=4
        self.min=(self.numpag-1)*self.elempag
        
    
    def crear_listbox(self):
        self.listbox = Gtk.ListBox()                                        #creamos una tabla con un listbox
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        row = Gtk.ListBoxRow()                                              #creamos las filas
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)  #lo metemos en una caja
        row.add(hbox)                                                       #lo añadimos a una fila

        label1 = Gtk.Label(label="uuid", xalign=0)                          #damos formato a la tabla
        labelvacio = Gtk.Label(label="                                                                    ", xalign=0)
        label2 = Gtk.Label(label="Nombre", xalign=0)
        label3 = Gtk.Label(label="Apellido", xalign=0)
        label7 = Gtk.Label(label="Email", xalign=0)
        labelvacio2 = Gtk.Label(label="                                    ", xalign=0)
        label6 = Gtk.Label(label="Telefono", xalign=0)
        
        label10 = Gtk.Label(label="Vacunado", xalign=0)
        label8 = Gtk.Label(label="                     ", xalign=0)
        label9 = Gtk.Label(label="                     ", xalign=0)
        

        hbox.pack_start(label1, True, True, 0)
        hbox.pack_start(labelvacio, True, True, 0)
        hbox.pack_start(label2, True, True, 0)
        hbox.pack_start(label3, True, True, 0)
        hbox.pack_start(label7, True, True, 0)
        hbox.pack_start(labelvacio2, True, True, 0)
        hbox.pack_start(label6, True, True, 0)
        hbox.pack_start(label10, True, True, 0)
        hbox.pack_start(label8, True, True, 0)
        hbox.pack_start(label9, True, True, 0)
        
        self.listbox.add(row)                                               #añadimos el formato a la listbox
        self.j=0

    def rellenamos_tabla(self):
        for self.j in range (len(self.lista)):                                 #recorremos los elementos de la tabla  
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            self.list =[]
            self.listatotal=self.controller.total
            self.listmax=len(self.listatotal)                                    #longitud maxima de la lista
            if(self.min+self.j<len(self.listatotal)): 
                for i in range(6):                                          #rellenamos con los datos de la bd
                   dato=self.lista[self.j][i]
                   labelfor = Gtk.Label(dato, xalign=0)
                   hbox.pack_start(labelfor, True, True, 0)

                button = Gtk.Button(label="QR")                             #boton del qr
                button._value=self.j
                button.connect("clicked", self.__class__.click_cod)
                hbox.pack_start(button, False, True, 0)
                self.listbox.add(row)

                
                if (self.j==0): #Para buscar el primer boton en los tests
                    button1 = Gtk.Button(label="Acceso ")                        #boton de acceso
                    button1.value=self.j
                    button1.connect("clicked", self.__class__.click_acceso)
                    hbox.pack_start(button1, False, True, 0)
                    acceso_accesible=button1.get_accessible()
                    acceso_accesible.set_name("Acceso1")
                else:
                    button = Gtk.Button(label="Acceso ")                        #boton de acceso
                    button.value=self.j
                    button.connect("clicked", self.__class__.click_acceso)
                    hbox.pack_start(button, False, True, 0)
                
                self.listbox.add(row)
            else:
                for i in range(8):                                          #rellenamos con los datos de la bd
                   dato=" "
                   labelfor = Gtk.Label(dato, xalign=0)
                   hbox.pack_start(labelfor, True, True, 0)
                
                self.listbox.add(row)
    
    
    def tabla(self):
        self.iniciar_variables_tabla()
        self.crear_listbox()
        self.rellenamos_tabla()
        
    def textopaginacion(self):                                                #botones de paginacion                                                          
        if(self.numpag*self.elempag>self.listmax):
                self.total=self.listmax
        else:
                self.total=self.numpag*self.elempag
                if(self.numpag*self.elempag-self.elempag<self.listmax):
                    self.text_num=f"Mostrando de {self.numpag*self.elempag-self.elempag} a {self.total} resultados de {self.listmax} entradas"
                else:self.text_num=f"No hay más entradas actualmente"
        
        self.num_label=Gtk.Label()
        self.num_label.set_text(self.text_num)
        self.hbox1_2.pack_start(self.num_label, True, True, 0)
        
        
    def fhbox12(self):    
        self.textopaginacion()
        self.beforebutton()
        self.paglabel()
        self.afterbutton()
        self.volverbutton()
        self.construirspinner()
    
    def anadirventana(self):
        self.first_screen.pack_start(self.label_prin, False, False, 0)
        self.first_screen.pack_start(self.hbox1_1, False, False, 0)
        self.first_screen.pack_start(self.listbox, False, False, 0)
        self.first_screen.pack_start(self.hbox1_2, False, False, 0)

    def primeraventana(self):                                               #inicializa la primera ventana
        tit='CONSULTAR INFORMACIÓN PERSONAL EN EL SISTEMA'
        self.__class__.titulo(self, tit)
        self.__class__.input1(self)
        self.__class__.fhbox11(self)
        self.__class__.tabla(self)
        self.__class__.fhbox12(self)
        self.__class__.anadirventana(self)
        self.box.pack_start(self.first_screen, False, False, 0)
    
    #Widgets 2
    
    def volverbutton2(self):
        self.back_b2=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        self.back_b2.connect("clicked", self.__class__.click_volver)

    def beforebutton2(self):
        self.before2_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before2_button.connect("clicked", self.__class__.click_antes2)
        before2_accessible = self.before2_button.get_accessible()
        before2_accessible.set_name("Antes 2")
    
    def numlabel2(self):
        self.num_label2=Gtk.Label()
        self.num_label2.set_text(str(self.numpag2))

    def afterbutton2(self):
        self.after2_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after2_button.connect("clicked", self.__class__.click_despues2)
        after2_accessible = self.after2_button.get_accessible()
        after2_accessible.set_name("Despues 2")
    
    def construirspinner2(self):
        self.spinner2 = Gtk.Spinner()
        spinner_accessible = self.spinner2.get_accessible()
        spinner_accessible.set_name("Spinner2")
        self.hbox2_2.pack_start(self.spinner2, False, False, 0)

    # Funciones para la ventana 2

    def input2(self):
        self.hbox2_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox2_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox2_3=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.START)

    def hbox21(self):
        self.rastreo=Gtk.Button(label="Rastrear", halign=Gtk.Align.CENTER)
        self.rastreo.connect("clicked", self.__class__.click_rastreo)
        self.hbox2_1.pack_start(self.rastreo, False, False, 0)

    def tabla2(self):                                                       #crea la tabla de la segunda ventana mediante un treeview

        labelstore=Gtk.ListStore(str,str,str,str,str,str)                   #da formato a la tabla
        self.min2=(self.numpag2-1)*self.elempag2         
        self.pagmax2=len(self.controller.total2)/self.elempag2
            
        

        for i in range(len(self.lista2)):                                      #rellenamos con los datos de la tabla
            #if (i+(self.numpag2-1)*self.elempag2)<len(self.lista2):
               labelstore.append(self.lista2[i])
               

        v.treeview=Gtk.TreeView(model=labelstore)                           #creamos el treeview 

        for t, dato in enumerate(["Temperatura","Fecha y Hora","Tipo","Nombre Instalacion","Direccion","Id"]):  #ponemos columnas del treeview
            renderer_text=Gtk.CellRendererText()
            column_text=Gtk.TreeViewColumn(dato,renderer_text,text=t)
            self.treeview.append_column(column_text)
        
        self.hbox2_3.pack_start(v.treeview, False, False, 0)
        treeview_accessible = v.treeview.get_accessible()
        treeview_accessible.set_name("string_treeview")      

    def hbox22(self):
        self.volverbutton2()
        self.beforebutton2()
        self.numlabel2()
        self.afterbutton2()
        self.volverbutton2()
        self.hbox2_2.pack_start(self.before2_button, False, False, 0)
        self.hbox2_2.pack_start(self.num_label2, True, True, 0)
        self.hbox2_2.pack_start(self.after2_button, False, False, 0)
        self.hbox2_2.pack_start(self.back_b2, False, False, 0)
        self.construirspinner2()
        
        
        

    def anadirventana2(self):
        self.second_screen.pack_start(self.label_prin, False, False, 0)     
        self.second_screen.pack_start(self.hbox2_3, False, False, 0)
        self.second_screen.pack_start(self.hbox2_1, False, False, 0)
        self.second_screen.pack_start(self.hbox2_2, False, False, 0)

    def segundaventana(self):
        tit='ACCESOS A INSTALACIONES'
        self.__class__.input2(self)
        self.__class__.titulo(self, tit)
        self.__class__.tabla2(self)
        self.__class__.hbox21(self)
        self.__class__.hbox22(self)
        self.__class__.anadirventana2(self)
        self.box.pack_start(self.second_screen, False, False, 0)
    
# Widgets 3
    def startenddate(self):
        self.fechaini="2001-01-01"
        self.fechafin="2021-12-31"
        self.label_start_date=Gtk.Label(label=_("Start date:"), xalign=0)
        self.start_date=Gtk.Entry(text="")
        self.start_date.set_placeholder_text(_("Ex. 2021-01-01"))
        self.start_date.connect('changed',self.__class__.date_searching)
        start_date_accesible=self.start_date.get_accessible()
        start_date_accesible.set_name("Start date")


        self.label_end_date=Gtk.Label(label=_("End date:"), xalign=0)
        self.end_date=Gtk.Entry(text="")
        self.end_date.set_placeholder_text(_("Ex. 2021-12-31"))
        self.end_date.connect('changed',self.__class__.date_searching2)
        end_date_accesible=self.end_date.get_accessible()
        end_date_accesible.set_name("End date")

    def searchdatebutton(self):
        self.date_button=Gtk.Button(label=_("Buscar"))
        self.date_button.connect("clicked", self.__class__.buscafecha)
        start_date_button=self.date_button.get_accessible()
        start_date_button.set_name("Buscar fechas")

    def construirspinner3(self):
        self.spinner3=Gtk.Spinner()
        spinner3_accessible = self.spinner3.get_accessible()
        spinner3_accessible.set_name("Spinner 3")

    def beforebutton3(self):
        self.before3_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before3_button.connect("clicked", self.__class__.click_antes3)
        before3_accessible = self.before3_button.get_accessible()
        before3_accessible.set_name("Antes 3")

    def afterbutton3(self):
        self.after3_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after3_button.connect("clicked", self.__class__.click_despues3)
        after3_accessible = self.after3_button.get_accessible()
        after3_accessible.set_name("Despues 3")

    def paglabel3(self):
        self.text_pag=f"Página {self.numpag3}"
        self.pag_label3=Gtk.Label()
        self.pag_label3.set_text(self.text_pag)

# Funciones para la ventana 3

    def input3(self):
        self.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)
        self.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)
        self.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)


    def hbox31(self):
        self.startenddate()
        self.searchdatebutton()
        self.labelpositivo=Gtk.Label(label=_("Id positivo: "+str(self.uuid)), xalign=0)
        self.hbox3_1.pack_start(self.label_start_date, False, False, 0)
        self.hbox3_1.pack_start(self.start_date, False, False, 0)
        self.hbox3_1.pack_start(self.label_end_date, False, False, 0)
        self.hbox3_1.pack_start(self.end_date, False, False, 0)
        self.hbox3_1.pack_start(self.date_button, False, False, 0)
        self.hbox3_1.pack_start(self.labelpositivo, False, False, 0)

    def hbox32(self):
        self.beforebutton3()
        self.paglabel3()
        self.afterbutton3()
        self.volverbutton2()
        self.construirspinner3()

        self.hbox3_2.pack_start(self.before3_button, False, False, 0)
        self.hbox3_2.pack_start(self.pag_label3, True, True, 0)
        self.hbox3_2.pack_start(self.after3_button, False, False, 0)
        self.hbox3_2.pack_start(self.back_b2, False, False, 0)
        self.hbox3_2.pack_start(self.spinner3, False, False, 0)
        

    def tabla3(self):                                                                  #sigue la misma funcionalidad que la tabla 2, pero con los datos de la bd oportunos

        labelstore=Gtk.ListStore(str,str,str)
        
        v.min3=(v.numpag3-1)*v.elempag3            
        
        
        for i in range(self.elempag3):
            if (i+(self.numpag3-1)*self.elempag3)<len(self.lista3):
                labelstore.append(self.lista3[i+(self.numpag3-1)*self.elempag3])     

        v.treeview3=Gtk.TreeView(model=labelstore)    
        
        for t, dato in enumerate(["Contacto","Instalacion","Fecha y hora"]):
            renderer_text=Gtk.CellRendererText()
            column_text=Gtk.TreeViewColumn(dato,renderer_text,text=t)
            v.treeview3.append_column(column_text)
        self.hbox3_3.pack_start(v.treeview3, False, False, 0)
        treeview3_accessible = v.treeview3.get_accessible()
        treeview3_accessible.set_name("string_treeview3")
        self.lista3=[]
        

    def anadirventana3(self):
        self.third_screen.pack_start(self.label_prin, False, False, 0)
        self.third_screen.pack_start(self.hbox3_1, False, False, 0)
        self.third_screen.pack_start(self.hbox3_3, False, False, 0)
        self.third_screen.pack_start(self.hbox3_2, False, False, 0)

    def terceraventana(self):
        tit='ALERTAS COVID'
        self.__class__.titulo(self, tit)
        self.__class__.input3(self)
        self.__class__.hbox31(self)
        self.__class__.tabla3(self)
        self.__class__.hbox32(self)
        self.__class__.anadirventana3(self)  
        self.box.pack_start(self.third_screen, False, False, 0)  

    #Ventana 4
    def input4(self):                                                                   #la ventana del qr
        self.hbox4_1=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.END)

    def hbox41(self):
        
        self.labelqr = Gtk.Image()
        self.labelqr.set_from_file("qrcode.png")
        self.hbox4_1.pack_start(self.labelqr, False, False, 0)
        button=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        button.connect("clicked", self.__class__.click_volver)
        self.hbox4_1.pack_start(button, False, False, 0)
        

    def anadirventana4(self):
        self.fourth_screen.pack_start(self.hbox4_1, False, False, 0)

    def cuartaventana(self):
        self.__class__.click_qr(self)
        self.__class__.input4(self)
        self.__class__.hbox41(self)
        self.__class__.anadirventana4(self)


    
    
    #Funciones comunes

    def show_error(self,text):
        dialog= Gtk.MessageDialog(parent=self.win,
                                message_type=Gtk.MessageType.ERROR,
                                buttons=Gtk.ButtonsType.CLOSE,
                                text=text)
        dialog.run()
        dialog_accesible=dialog.get_accessible()
        dialog_accesible.set_name("Error")
        dialog.destroy()
    
    
    
    
    
    #Funciones de inicio
    def _init_definitions(self):
        self.controller=Controller
        self.controller._init_(self.controller)
        self.a=self.o=0
        self.op=True
        self.numpag=self.numpag2=self.numpag3=1
        self.uuid=''
        self.lista2=self.lista3=[]
        self.elempag=self.elempag3=15                                                     
        self.elempag2=20
        self.fechaini='2021-01-01T00:00:00.277923+00:00'
        self.fechafin='2021-12-31T23:59:59.277923+00:00'
        self.min=(self.numpag-1)*self.elempag
        self.pagmax3=0
        self.filtro=False
        try:
            self.controller.datos_inicio(self.controller, self.min)
            self.lista=self.controller.result
        except Exception as err:
            v.show_error("Error para comunicarse con la base de datos")
        

    def cajainicio(self):                                                       #crea la caja inicial
        self.win = Gtk.Window(title=_("Accesos COVID"))                         #atribuye titulo
        self.win.connect('delete-event',v.main_quit)                            #conectamos el boton de salir
        self.box = Gtk.Box(halign= Gtk.Align.CENTER)
        
        #Definimos caja por ventana
        self.first_screen = Gtk.VBox(spacing=10, margin=15)
        self.second_screen = Gtk.VBox(spacing=10, margin=15)
        self.third_screen = Gtk.VBox(spacing=10, margin=15)
        self.fourth_screen = Gtk.VBox(spacing=10,margin=15)
    
    def anadirpantalla(self):
        self.win.add(self.box)
        self.win.set_default_size(480, 450)
    
    def build_view(self):
        self.__class__.cajainicio(self)
        self.__class__._init_definitions(self)
        self.__class__.primeraventana(self)
        self.__class__.segundaventana(self)
        self.__class__.terceraventana(self)
        self.__class__.anadirpantalla(self)
    
    #Mostrar pantalla
    
    def _show_screen(self, i):
        if(i!=1):
            self.first_screen.hide()
        else:
            self.first_screen.show_all()
        if(i!=2):
            self.second_screen.hide()
        else:
            self.second_screen.show_all()
        if(i!=3):
            self.third_screen.hide()
        else:
            self.third_screen.show_all()
        if(i!=4):
            self.fourth_screen.hide()
        else:
            self.fourth_screen.show_all()
        

    def _show_fourth_screen(self): #En esta ventana la volvemos a crear ya  que le qr se genera en base a los datos anteriores
        if self.a!=0:
            self.hbox4_1.destroy()
        self.a+=1
        v.first_screen.hide()
        v.second_screen.hide()
        v.third_screen.hide()
        v.cuartaventana()
        if self.a==1:
            v.box.pack_start(self.fourth_screen, False, False, 0)
        v.fourth_screen.show_all()
    
    # MOSTRAR VIEW
    # Muestra view (1º pantalla)
    def show(self):
        self.win.show()
        self.box.show()

    def show_all(self):
        self.win.show_all()
    
    def exit(self):
        v.win.destroy()
    
    def comenzar(self):
        v.build_view()
        v.show()
        v._show_screen(1)

v=View()
v.comenzar()