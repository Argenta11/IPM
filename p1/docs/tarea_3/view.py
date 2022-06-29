import datetime
import gettext
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

_ = gettext.gettext

import qrcode
from controller import Controller

# TABLAS PARA PROBAR



class View:

    @classmethod
    def main(Cls):
        Gtk.main()

    @classmethod
    def main_quit(cls, w, e):
        Gtk.main_quit()


#FUNCIONES DE BOTONES

    def click_acceso(self):     #Funcion a la que se llama cuando se clica al boton de acceso

        v.uuid = v.listoflists[self.value][0]   #obtenemos el uuid de la persona accedida
        try:
            v.lista2=v.controller.datos_inicio2(v.controller, v.uuid)   #almacenamos los datos de donde estuvo
        except Exception as err:
                v.show_error("Error para comunicarse con la base de datos")    
                                                       #destruimos para que no se vayan duplicando
        v.hbox2_1.destroy()
        v.hbox2_3.destroy()
        v.hbox2_2.destroy()
        v.hbox2_3=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.START)      #se inicializan las 3 cajas despues de destruir las anteriores
        v.hbox2_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        v.hbox2_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        v.tabla2()                                                            #se crea otra vez la ventana
        v.hbox21()
        v.hbox22()


        v.second_screen.pack_start(v.hbox2_3, False, False, 0)                #se inician las cajas
        v.second_screen.pack_start(v.hbox2_1, False, False, 0)
        v.second_screen.pack_start(v.hbox2_2, False, False, 0)

        v._show_second_screen()

    def click_rastreo(self):                                                    #funcion que se llama al clicar al boton de rastreo
        v.pag=3
            
        
       
        v.hbox3_1.destroy()                                                     #destruimos para que no se vayan duplicando            
        v.hbox3_2.destroy()
        v.hbox3_3.destroy()
        v.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)        #se inician las cajas
        v.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        v.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        v.tabla3()                                                              #se crea otra vez la ventana
        v.hbox31()
        v.hbox32()
        

        v.third_screen.pack_start(v.hbox3_1, False, False, 0)                   #se inician las cajas
        v.third_screen.pack_start(v.hbox3_3, False, False, 0)
        v.third_screen.pack_start(v.hbox3_2, False, False, 0)
        
        
        v._show_third_screen()                                                  #se muestra la ventana
        
    def click_volver(self):                                                     #funcion que permite volver a la pagina inicial
        v.pag=1
        v._show_first_screen()
        
    def click_antes(self):                                                      #funcion que se ejecuta al clicar en antes(paginacion)
        if v.numpag != 1:                                                       #comprueba que no sea la primera pagina
           v.numpag -= 1
        v.listbox.destroy()                                                     #evitar duplicados
        v.hbox1_2.destroy()
        v.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)        #creamos la caja
        v.tabla()                                                               #llamamos a la funcion tabla
        v.pagyvolver()                                                          #y a la funcion que situa los botones de paginacion y volver
        v.fhbox12()                                                             
        v.first_screen.pack_start(v.listbox, False, False, 0)                   #metemos todo en la caja inicial
        v.first_screen.pack_start(v.hbox1_2, False, False, 0)
        v._show_first_screen()                                                  

    def click_despues(self):                                                    #funcion que se ejecuta al clicar a despues(paginacion)
        v.numpag += 1
        if v.numpag <= v.pagmax:                                                #comprueba que no se pase de max pag    
           v.listbox.destroy()
           v.hbox1_2.destroy()
           v.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.tabla()
           v.pagyvolver()
           v.fhbox12()
           v.first_screen.pack_start(v.listbox, False, False, 0)
           v.first_screen.pack_start(v.hbox1_2, False, False, 0)
           v._show_first_screen()
        else:v.numpag-=1


    def click_antes2(self):                                                     #mismo que click antes
        
        if v.numpag2 != 1:
           v.numpag2 -= 1
           v.hbox2_1.destroy()
           v.hbox2_3.destroy()
           v.hbox2_2.destroy()
           v.hbox2_3=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.hbox2_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.hbox2_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.tabla2()
           v.hbox21()
           v.hbox22()
           v.second_screen.pack_start(v.hbox2_3, False, False, 0)
           v.second_screen.pack_start(v.hbox2_1, False, False, 0)
           v.second_screen.pack_start(v.hbox2_2, False, False, 0)
           v._show_second_screen()
    
    def click_despues2(self):                                                   #mismo que click despues
        v.numpag2 += 1
        if v.numpag2 <= v.pagmax2:
           v.hbox2_1.destroy()
           v.hbox2_3.destroy()
           v.hbox2_2.destroy()
           v.hbox2_3=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.hbox2_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.hbox2_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           v.tabla2()
           v.hbox21()
           v.hbox22()
           v.second_screen.pack_start(v.hbox2_3, False, False, 0)
           v.second_screen.pack_start(v.hbox2_1, False, False, 0)
           v.second_screen.pack_start(v.hbox2_2, False, False, 0)
           v._show_second_screen()
        else:v.numpag2-=1

    def click_antes3(self):                                                     #mismo que click antes
        
        if v.numpag3 != 1:
            v.numpag3-=1
            v.hbox3_1.destroy()
            v.hbox3_2.destroy()
            v.hbox3_3.destroy()
            v.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.tabla3()
            v.hbox31()
            v.hbox32()

            v.third_screen.pack_start(v.hbox3_1, False, False, 0)
            v.third_screen.pack_start(v.hbox3_3, False, False, 0)
            v.third_screen.pack_start(v.hbox3_2, False, False, 0)
            v._show_third_screen()

    def click_despues3(self):                                                    #mismo que click despues
        v.numpag3 += 1
        if v.numpag3 <= v.pagmax3:
            v.hbox3_1.destroy()
            v.hbox3_2.destroy()
            v.hbox3_3.destroy()
            v.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.tabla3()
            v.hbox31()
            v.hbox32()

            v.third_screen.pack_start(v.hbox3_1, False, False, 0)
            v.third_screen.pack_start(v.hbox3_3, False, False, 0)
            v.third_screen.pack_start(v.hbox3_2, False, False, 0)
            v._show_third_screen()
        else: v.numpag3-=1
    
    
    
    
    
    def click_volver_persona(self):                                             #funcion que sirve para volver a la pagina de inicio despues de buscar a alguien
        try:
            v.lista=v.controller.datos_inicio(v.controller)
        except Exception as err:
                v.show_error("Error para comunicarse con la base de datos")   
        v.listbox.destroy()
        v.hbox1_2.destroy()
        v.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        v.tabla()
        v.pagyvolver()
        v.fhbox12()
        v.first_screen.pack_start(v.listbox, False, False, 0)
        v.first_screen.pack_start(v.hbox1_2, False, False, 0)
        v._show_first_screen()
    

           
    
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
           v.hbox1_2.destroy()                                                  
           v.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
           texto = v.busqueda.split()                                           #spliteamos el texto introducido
           if(len(texto)!=2):                                                   #comprobacion del formato
               v.show_error("No se ha introducido de la manera correcta")       #funcion de error
               v.pagyvolver()                                                   #se vuelve a mostrar todo
               v.fhbox12()
               v.first_screen.pack_start(v.hbox1_2, False, False, 0)
               v._show_first_screen()
           else:
            nombre = texto[0]                                           
            apellido = texto[1]
            result=[]
            try:
                result=v.controller.on_searchbar_click(v.controller, nombre, apellido)      #devuelve los resultados de buscar en la bd
            except Exception as err:
                v.show_error("Error para comunicarse con la base de datos")    
            if(result):                                                         #si la lista no esta vacia
                v.mostrardatos(result)
                v.pagyvolver()
                v.fhbox12()
                v.first_screen.pack_start(v.hbox1_2, False, False, 0)
                v._show_first_screen()
            else:                                                               #si esta vacia(no esta en la bd)
                v.show_error("No se ha encontrado en la base de datos")
                v.pagyvolver()
                v.fhbox12()
                v.first_screen.pack_start(v.hbox1_2, False, False, 0)
                v._show_first_screen()

    
    def buscafecha(self):                                                       #funcion de buscar fecha
        v.validate(v.fechaini)
        v.validate(v.fechafin)
        v.fechainit=v.fechaini.split('/')
        v.fechafint=v.fechafin.split('/')

        if(v.fechainit[2]> v.fechafint[2] or v.fechaini is None or v.fechafin is None):
           v.show_error("Fecha incorrecta") 
        else:
            if((v.fechainit[2]==v.fechainit[2]) & (v.fechainit[0]>v.fechafint[0])):
                v.show_error("Fecha incorrecta")
            else:
                if((v.fechainit[2]==v.fechainit[2]) & (v.fechainit[0]==v.fechafint[0]) & (v.fechainit[1]>v.fechafint[1])):
                    v.show_error("Fecha incorrecta")
        
        v.lista3=v.controller.on_searchdate_click(v.controller,v.fechaini,v.fechafin)
        if(v.lista3):
            v.hbox3_1.destroy()                                                     #destruimos para que no se vayan duplicando            
            v.hbox3_2.destroy()
            v.hbox3_3.destroy()
            v.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)        #se inician las cajas
            v.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
            v.tabla3()                                                              #se crea otra vez la ventana
            v.hbox31()
            v.hbox32()
            

            v.third_screen.pack_start(v.hbox3_1, False, False, 0)                   #se inician las cajas
            v.third_screen.pack_start(v.hbox3_3, False, False, 0)
            v.third_screen.pack_start(v.hbox3_2, False, False, 0)
            v._show_third_screen()                                                  #se muestra la ventana
        

    def validate(self,date_text):                                               #valida el formato de la fecha
        try:
            datetime.datetime.strptime(date_text, "%m/%d/%Y")
        except ValueError:
            v.show_error("Formato incorrecto")
        

    def mostrardatos(self,result):                                              
        self.lista=result
        self.listbox.destroy()
        self.tabla()
        self.first_screen.pack_start(self.listbox, False, False, 0)
        self._show_first_screen()

        



# FUNCIONES COMUNES PARA TODAS LAS VENTANAS

    def cajainicio(self):                                                       #crea la caja inicial
        self.win = Gtk.Window(title=_("Accesos COVID"))                         #atribuye titulo
        self.win.connect('delete-event',v.main_quit)                            #conectamos el boton de salir
        self.box = Gtk.Box(halign= Gtk.Align.CENTER)
        self.numpag=1
        self.numpag2=1
        self.numpag3=1
        #Definimos caja por ventana
        self.first_screen = Gtk.VBox(spacing=10, margin=15)
        self.second_screen = Gtk.VBox(spacing=10, margin=15)
        self.third_screen = Gtk.VBox(spacing=10, margin=15)
        self.fourth_screen = Gtk.VBox(spacing=10,margin=15)

#anadir uuid
    def click_qr(self):                                                         #genera el qr
        
        uuid = self.listoflists[self.j][0]                                      #separamos uuid, nombre y apellido
        nombre = self.listoflists[self.j][1]
        apellido = self.listoflists[self.j][2]
        
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
        
    def botonespaginacion(self):                                                #botones de paginacion
        if (v.pag==1):                                                          
            if(self.numpag*self.elempag>self.listmax):
                self.total=self.listmax
            else:
                self.total=self.numpag*self.elempag
                if(self.numpag*self.elempag-self.elempag<self.listmax):
                    self.text_num=f"Mostrando de {self.numpag*self.elempag-self.elempag} a {self.total} resultados de {self.listmax} entradas"
                else:self.text_num=f"No hay más entradas actualmente"
        
        self.num_label=Gtk.Label()
        self.num_label.set_text(self.text_num)
        self.before_button=Gtk.Button(label=_("Antes"))

        self.num=1
        self.text_pag=f"Página {self.numpag}"
        self.pag_label=Gtk.Label()
        self.pag_label.set_text(self.text_pag)
        self.after_button=Gtk.Button(label=_("Despues")) 
        
        
        

    def pagyvolver(self):                                                   #boton de volver + paginacion
        self.__class__.botonespaginacion(self)
        self.num_label.destroy()
        self.back_b2=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        self.back_b2.connect("clicked", self.__class__.click_volver)

    def titulo(self, tit):
        self.label_prin=Gtk.Label()
        self.label_prin.set_margin_top(10)
        self.tit = tit
        self.label_prin.set_markup("<big>" + tit + "</big>")

# FUNCIONES PARA LA VENTANA 1

    def mostrarimagen (img, self):
        self.__class__.titulo(self, 'Codigo QR')
    
    def input1(self):
        self.hbox1_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox1_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)

    def fhbox11(self):                                                      #crea la primera caja con la barra de busqueda
        self.busqueda=""
        self.search_bar=Gtk.SearchEntry(text="")
        self.search_bar.set_placeholder_text(("Buscar por nombre y apellidos"))
        self.search_bar.connect('search-changed',self.__class__.bar_searching)  #conecta con la funcion bar_searching
        search_bar_accesible=self.search_bar.get_accessible()
        search_bar_accesible.set_name("Search bar")
        self.search_button=Gtk.Button(label=_("Buscar"))
        self.search_button.connect("clicked", self.__class__.busca)
        start_search_button=self.search_button.get_accessible()
        start_search_button.set_name("Busca Nombre")
        
        

        self.hbox1_1.pack_start(self.search_bar, False, False, 0)
        self.hbox1_1.pack_start(self.search_button, False, False, 0)

    def tabla(self):
        # Lista de personal
        
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

        self.listoflists = []
        self.list=[]
        self.elempag=15                                                     #numero maximo de elemntos por pagina
        self.elempag2=20
        self.elempag3=15
        self.j=(self.numpag-1)*self.elempag
        
        
        if len(self.lista)%self.elempag==0:
           self.pagmax = len(self.lista)/self.elempag
        else: self.pagmax = len(self.lista)/self.elempag+1

        print(self.pagmax)
        if(self.elempag>=len(self.lista)):
            self.elempag=len(self.lista)
        else:
            self.elempag=15

        
        for self.j in range (self.elempag2):                                 #recorremos los elementos de la tabla
          if self.j<self.elempag:  
            row = Gtk.ListBoxRow()
            hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
            row.add(hbox)
            self.list =[]
            self.listmax=len(self.lista)                                    #longitud maxima de la lista
            if(self.numpag-1)*self.elempag+self.j<len(self.lista): 
                for i in range(6):                                          #rellenamos con los datos de la bd
                   dato=self.lista[(self.numpag-1)*self.elempag+self.j][i]
                   labelfor = Gtk.Label(dato, xalign=0)
                   hbox.pack_start(labelfor, True, True, 0)
                   self.list.append(self.lista[(self.numpag-1)*self.elempag+self.j][i])
            
                self.listoflists.append(self.list)

                button = Gtk.Button(label="QR")                             #boton del qr
                button._value=self.j
                button.connect("clicked", self.__class__.click_cod)
                hbox.pack_start(button, False, True, 0)
                self.listbox.add(row)

                
                if (self.j==0):
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
                   self.list.append(" ")
            
                self.listoflists.append(self.list)
                
                self.listbox.add(row)



    def fhbox12(self):
        
        
        self.hbox1_2.pack_start(self.num_label, True, True, 0)
        
        self.before_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before_button.connect("clicked", self.__class__.click_antes)
        before_accessible = self.before_button.get_accessible()
        before_accessible.set_name("Antes1")
        self.hbox1_2.pack_start(self.before_button, False, False, 0)

        self.hbox1_2.pack_start(self.pag_label, True, True, 0)

        self.after_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after_button.connect("clicked", self.__class__.click_despues)
        after_accessible = self.after_button.get_accessible()
        after_accessible.set_name("Despues1")
        self.hbox1_2.pack_start(self.after_button, False, False, 0)

        self.backp=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        self.backp.connect("clicked", self.__class__.click_volver_persona)
        volver_accessible = self.backp.get_accessible()
        volver_accessible.set_name("Volver1")
        self.hbox1_2.pack_start(self.backp,False, False, 0)

    def anadirventana(self):
        self.first_screen.pack_start(self.label_prin, False, False, 0)
        self.first_screen.pack_start(self.hbox1_1, False, False, 0)
        self.first_screen.pack_start(self.listbox, False, False, 0)
        self.first_screen.pack_start(self.hbox1_2, False, False, 0)

    def primeraventana(self):                                               #inicializa la primera ventana
        tit='CONSULTAR INFORMACIÓN PERSONAL EN EL SISTEMA'
        self.__class__.cajainicio(self)
        self.__class__.titulo(self, tit)
        self.__class__.input1(self)
        self.__class__.fhbox11(self)
        self.__class__.tabla(self)
        self.__class__.botonespaginacion(self)
        self.__class__.pagyvolver(self)
        self.__class__.fhbox12(self)
        self.__class__.anadirventana(self)

# FUNCIONES PARA LA VENTANA 2

    def input2(self):
        self.hbox2_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox2_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.START)
        self.hbox2_3=Gtk.VBox(spacing=10, margin=0, halign=Gtk.Align.START)

    def tabla2(self):                                                       #crea la tabla de la segunda ventana mediante un treeview

        labelstore=Gtk.ListStore(str,str,str,str,str,str)                   #da formato a la tabla
                    
        if (len(self.lista2)%self.elempag2==0):
           self.pagmax2=len(self.lista2)/self.elempag2
        else:
            self.pagmax2=len(self.lista2)/self.elempag2+1
        
        
        for i in range(self.elempag2):                                      #rellenamos con los datos de la tabla
            if (i+(self.numpag2-1)*self.elempag2)<len(self.lista2):
               labelstore.append(self.lista2[i+(self.numpag2-1)*self.elempag2])
               

        v.treeview=Gtk.TreeView(model=labelstore)                           #creamos el treeview 

        for t, dato in enumerate(["Temperatura","Fecha y Hora","Tipo","Nombre Instalacion","Direccion","Id"]):  #ponemos columnas del treeview
            renderer_text=Gtk.CellRendererText()
            column_text=Gtk.TreeViewColumn(dato,renderer_text,text=t)
            self.treeview.append_column(column_text)
        
        self.hbox2_3.pack_start(v.treeview, False, False, 0)
        treeview_accessible = v.treeview.get_accessible()
        treeview_accessible.set_name("string_treeview")
        
    

    def hbox21(self):
        self.rastreo=Gtk.Button(label="Rastrear", halign=Gtk.Align.CENTER)
        self.rastreo.connect("clicked", self.__class__.click_rastreo)
        self.hbox2_1.pack_start(self.rastreo, False, False, 0)

    def hbox22(self):
        self.back_b2=Gtk.Button(label="Volver", halign=Gtk.Align.CENTER)
        self.back_b2.connect("clicked", self.__class__.click_volver)
        if(self.numpag*self.elempag>self.listmax):
           self.total=self.listmax
        else:
            self.total=self.numpag2*self.elempag
        if(self.numpag2*self.elempag-self.elempag<self.listmax):
            self.text_num=f"Mostrando de {self.numpag2*self.elempag-self.elempag} a {self.total} resultados de {self.listmax} entradas"
        else:self.text_num=f"No hay más entradas actualmente"
        self.before2_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before2_button.connect("clicked", self.__class__.click_antes2)
        before2_accessible = self.before2_button.get_accessible()
        before2_accessible.set_name("Antes 2")
        self.num_label2=Gtk.Label()
        self.num_label2.set_text(str(self.numpag2))
        self.after2_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after2_button.connect("clicked", self.__class__.click_despues2)
        after2_accessible = self.after2_button.get_accessible()
        after2_accessible.set_name("Despues 2")
        self.hbox2_2.pack_start(self.before2_button, False, False, 0)
        self.hbox2_2.pack_start(self.num_label2, True, True, 0)
        self.hbox2_2.pack_start(self.after2_button, False, False, 0)
        self.hbox2_2.pack_start(self.back_b2, False, False, 0)
        

    def anadirventana2(self):
        self.second_screen.pack_start(self.label_prin, False, False, 0)
              
        self.second_screen.pack_start(self.hbox2_3, False, False, 0)
        self.second_screen.pack_start(self.hbox2_1, False, False, 0)
        self.second_screen.pack_start(self.hbox2_2, False, False, 0)

    def segundaventana(self):
        tit='ACCESOS A INSTALACIONES'
        self.__class__.input2(self)
        self.__class__.pagyvolver(self)
        self.__class__.titulo(self, tit)
        self.__class__.tabla2(self)
        self.__class__.hbox21(self)
        self.__class__.hbox22(self)
        self.__class__.anadirventana2(self)

# FUNCIONES PARA VENTANA 3

    def input3(self):
        self.hbox3_1=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)
        self.hbox3_2=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)
        self.hbox3_3=Gtk.HBox(spacing=10, margin=0, halign=Gtk.Align.END)


    def hbox31(self):
        self.fechaini=""
        self.fechafin=""
        self.label_start_date=Gtk.Label(label=_("Start date:"), xalign=0)
        self.start_date=Gtk.Entry(text="")
        self.start_date.set_placeholder_text(_("Ex. 12/31/2021"))
        self.start_date.connect('changed',self.__class__.date_searching)
        start_date_accesible=self.start_date.get_accessible()
        start_date_accesible.set_name("Start date")


        self.label_end_date=Gtk.Label(label=_("End date:"), xalign=0)
        self.end_date=Gtk.Entry(text="")
        self.end_date.set_placeholder_text(_("Ex. 12/31/2021"))
        self.end_date.connect('changed',self.__class__.date_searching2)
        end_date_accesible=self.end_date.get_accessible()
        end_date_accesible.set_name("End date")


        self.date_button=Gtk.Button(label=_("Buscar"))
        self.date_button.connect("clicked", self.__class__.buscafecha)
        start_date_button=self.date_button.get_accessible()
        start_date_button.set_name("Buscar fechas")
        self.labelpositivo=Gtk.Label(label=_("Id positivo: "+str(self.uuid)), xalign=0)
        self.hbox3_1.pack_start(self.label_start_date, False, False, 0)
        self.hbox3_1.pack_start(self.start_date, False, False, 0)
        self.hbox3_1.pack_start(self.label_end_date, False, False, 0)
        self.hbox3_1.pack_start(self.end_date, False, False, 0)
        self.hbox3_1.pack_start(self.date_button, False, False, 0)
        self.hbox3_1.pack_start(self.labelpositivo, False, False, 0)

    def hbox32(self):
        self.__class__.pagyvolver(self)
        self.before3_button = Gtk.Button(label="Antes", halign=Gtk.Align.CENTER)
        self.before3_button.connect("clicked", self.__class__.click_antes3)
        before3_accessible = self.before3_button.get_accessible()
        before3_accessible.set_name("Antes 3")
        self.after3_button = Gtk.Button(label="Despues", halign=Gtk.Align.CENTER)
        self.after3_button.connect("clicked", self.__class__.click_despues3)
        after3_accessible = self.after3_button.get_accessible()
        after3_accessible.set_name("Despues 3")
        self.text_pag=f"Página {self.numpag3}"
        self.pag_label3=Gtk.Label()
        self.pag_label3.set_text(self.text_pag)
        self.hbox3_2.pack_start(self.before3_button, False, False, 0)
        self.hbox3_2.pack_start(self.pag_label3, True, True, 0)
        self.hbox3_2.pack_start(self.after3_button, False, False, 0)
        self.hbox3_2.pack_start(self.back_b2, False, False, 0)

    def tabla3(self):                                                                  #sigue la misma funcionalidad que la tabla 2, pero con los datos de la bd oportunos

        labelstore=Gtk.ListStore(str,str,str)
        
                    
        if (len(self.lista3)%self.elempag3==0):
           self.pagmax3=len(self.lista3)/self.elempag3
        else:
            self.pagmax3=len(self.lista3)/self.elempag3+1
        
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
        self.__class__.pagyvolver(self)
        self.__class__.titulo(self, tit)
        self.__class__.input3(self)
        self.__class__.hbox31(self)
        self.__class__.tabla3(self)
        self.__class__.hbox32(self)
        self.__class__.anadirventana3(self)

#Ventana QR
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

#AÑADIR A LA PANTALLA PRINCIPAL

    def anadirpantalla(self):
        
        self.box.pack_start(self.first_screen, False, False, 0)
        self.box.pack_start(self.second_screen, False, False, 0)
        self.box.pack_start(self.third_screen, False, False, 0)
        self.win.add(self.box)

        self.win.set_default_size(480, 450)

# CONSTRUIR PANTALLAS
    def build_view(self):
        self.controller=Controller
        self.controller._init_(self.controller)
        self.a=0
        self.o=0
        self.pag=1
        self.uuid=''
        self.lista2=[]
        self.lista3=[]
        try:
            self.lista=self.controller.datos_inicio(self.controller)
        except Exception as err:
                v.show_error("Error para comunicarse con la base de datos") 
        self.__class__.primeraventana(self)
        self.__class__.segundaventana(self)
        self.__class__.terceraventana(self)
        self.__class__.anadirpantalla(self)

# DEFINICIONES DE MOSTRAR PANTALLAS
    def _show_first_screen(self):
        self.second_screen.hide()
        self.third_screen.hide()
        self.fourth_screen.hide()
        self.first_screen.show_all()

    def _show_second_screen(self):
        self.first_screen.hide()
        self.third_screen.hide()
        self.fourth_screen.hide()
        self.second_screen.show_all()

    def _show_third_screen(self):
        self.first_screen.hide()
        self.second_screen.hide()
        self.fourth_screen.hide()
        self.third_screen.show_all()

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

#DIALOGOS DE ERROR

    def show_error(self,text):
        dialog= Gtk.MessageDialog(parent=self.win,
                                message_type=Gtk.MessageType.ERROR,
                                buttons=Gtk.ButtonsType.CLOSE,
                                text=text)
        dialog.run()
        dialog_accesible=dialog.get_accessible()
        dialog_accesible.set_name("Error")
        dialog.destroy()

# MOSTRAR VIEW
    # Muestra view (1º pantalla)
    def show(self):
        self.win.show()
        self.box.show()

    def show_all(self):
        self.win.show_all()
    
    def exit(self):
        v.win.destroy()


v=View()
v.build_view()
v.show()
v._show_first_screen()