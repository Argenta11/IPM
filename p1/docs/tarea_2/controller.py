
from model import Model


class Controller:

    def _init_(self):
        self.model = Model
        
    

    #CONTROLLER DE LA PRIMERA PANTALLA

    #Barra de busqueda
     
    def on_searchbar_click(self, nombre, apellido): #consigue los datos que le entran desde los labels de buscar
            self.model.setNombre(self.model,nombre)
            self.model.setApellido(self.model,apellido)
            result=[]
            result = self.model.getFilteredData(self.model)
            return result


    def on_searchdate_click(self,fechaini,fechafin):    #consigue los datos que le entran desde los labels de fecha
            self.model.setfinicio(self.model,fechaini)
            self.model.setfin(self.model,fechafin)
            result = []
            result = self.model.getData4(self.model)
            return result
        
        
        


    #Inicio
    def datos_inicio(self):                             #consigue los datos de la bd
            result=self.model.getData(self.model)
            return result
    

    #CONTROLLER DE LA SEGUNDA PANTALLA

    #Inicio
    def datos_inicio2(self, uuid):                      #consigue los datos de la bd despues de haberlos buscado ya para la segunda pantalla
            self.model.setUserId(self.model,uuid)
            result=self.model.getData2(self.model)
            return result
    
    #Rastrear

    #Paginacion



    #CONTROLLER DE LA TERCERA PANTALLA
    #Inicio
    def datos_inicio3(self, uuid):                      #consigue los datos de la bd despues de haberlos buscado ya para la segunda pantalla
            self.model.setUserId(self.model,uuid)
            result=self.model.getData3(self.model)
            return result
