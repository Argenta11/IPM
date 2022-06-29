from model import Model
import threading
import time

class Controller:

    def _init_(self):
        self.model = Model
        self.total2 = []
        self.total3 = []
        
        
    

    #CONTROLLER DE LA PRIMERA PANTALLA

    #Barra de busqueda
     
    def on_searchbar_click(self, nombre, apellido): #consigue los datos que le entran desde los labels de buscar
            self.model.setNombre(self.model,nombre)
            self.model.setApellido(self.model,apellido)
            self.result_bar=[]
            self.result_bar = self.model.getFilteredData(self.model)


    def on_searchdate_click(self,fechaini,fechafin, min):    #consigue los datos que le entran desde los labels de fecha
            self.model.setfinicio(self.model,fechaini)
            self.model.setfin(self.model,fechafin)
            self.result_date = []
            self.result_date = self.model.getData4(self.model, min)
            
            
        
        
        


    #Inicio
 
    def datos_inicio(self, min):                             #consigue los datos de la bd
            self.result=self.model.getData(self.model, min)     
            self.total=self.model.getAllData(self.model) 
    
    

    #CONTROLLER DE LA SEGUNDA PANTALLA

    #Inicio
    def datos_inicio2(self, uuid, min):                      #consigue los datos de la bd despues de haberlos buscado ya para la segunda pantalla
            self.model.setUserId(self.model,uuid)
            self.result2=self.model.getData2(self.model, min)
            self.total2=self.model.getAllData2(self.model)
            

            
    

    #Paginacion



    #CONTROLLER DE LA TERCERA PANTALLA
    #Inicio
    def datos_inicio3(self, uuid, min):                      #consigue los datos de la bd despues de haberlos buscado ya para la segunda pantalla
            self.model.setUserId(self.model,uuid)
            self.result3=self.model.getData3(self.model, min)
            self.total3=self.model.getAllData3(self.model)
            
