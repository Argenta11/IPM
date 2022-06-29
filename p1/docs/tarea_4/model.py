import gettext
from datetime import datetime
import requests
from pathlib import Path
_ = gettext.gettext
N_ = gettext.ngettext

#Lista de usuarios (uuid, username, name, surname, email, phone, is_vaccinated)
class Model:
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def getData(self, min):
        self.string_final=[]
        r = requests.get("http://localhost:8080/api/rest/users?offset="+str(min)+"&limit=15", 
            headers={"x-hasura-admin-secret":"myadminsecretkey"})
        self.data = r.json()
        
        for a in range(len(r.json()['users'])):
                dic=[]
                dic.append(str(r.json()['users'][a]['uuid']))         
                dic.append(str(r.json()['users'][a]['name']))
                dic.append(str(r.json()['users'][a]['surname']))
                dic.append(str(r.json()['users'][a]['email']))
                dic.append(str(r.json()['users'][a]['phone']))
                dic.append(str(r.json()['users'][a]['is_vaccinated']))
                self.string_final.append(dic)  
       
        return self.string_final

    def getAllData(self):
        self.string_final=[]
        r = requests.get("http://localhost:8080/api/rest/users", 
            headers={"x-hasura-admin-secret":"myadminsecretkey"})
        self.data = r.json()
        
        for a in range(len(r.json()['users'])):
                dic=[]
                dic.append(str(r.json()['users'][a]['uuid']))         
                dic.append(str(r.json()['users'][a]['name']))
                dic.append(str(r.json()['users'][a]['surname']))
                dic.append(str(r.json()['users'][a]['email']))
                dic.append(str(r.json()['users'][a]['phone']))
                dic.append(str(r.json()['users'][a]['is_vaccinated']))
                self.string_final.append(dic)
            
  
        return self.string_final
    
    #Tabla filtrada por nombre o nombre y apellido
    def getFilteredData(self):
        string_final=[]
        if self.nombre is not None:
            if self.apellido is not None:
                r = requests.get("http://localhost:8080/api/rest/user?name="+self.nombre+"&surname="+self.apellido, 
                    headers={"x-hasura-admin-secret":"myadminsecretkey"})
            else:
                r = requests.get("http://localhost:8080/api/rest/user?name="+self.nombre, 
                    headers={"x-hasura-admin-secret":"myadminsecretkey"})

            self.data = r.json()

        for a in range(len(r.json()['users'])):
            dic=[]
            dic.append(str(r.json()['users'][a]['uuid']))         
            dic.append(str(r.json()['users'][a]['name']))
            dic.append(str(r.json()['users'][a]['surname']))
            dic.append(str(r.json()['users'][a]['email']))
            dic.append(str(r.json()['users'][a]['phone']))
            dic.append(str(r.json()['users'][a]['is_vaccinated']))
            if ((dic[1]==self.nombre) & (dic[2]==self.apellido)):
                    string_final.append(dic)

            return string_final
    
    #Setters

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido

#Tabla de accesos a instalaciones (user_name, user_surname, user_uuid, user_is_vaccinated, user_phone
# user_email, temperature, timedate, type(IN/OUT), facility_id)

    def __init__2(self):
        self.userId = 0
        
    
    def getData2(self, min):
        self.finicio='2021-01-01T00:00:00.277923+00:00'
        self.ffin='2021-12-31T23:59:59.277923+00:00'
        self.ffin=None
        self.string_final=[]
        self.lug_final=[]
        r = requests.get("http://localhost:8080/api/rest/user_access_log/"+self.userId+"?offset="+str(min)+"&limit=20", 
            headers={"x-hasura-admin-secret":"myadminsecretkey"})
        self.data = r.json()
        
        for a in range(len(r.json()['access_log'])):
            #if(a>min & a<max):
                dic=[]
                dic.append(str(r.json()['access_log'][a]['temperature']))   
                dic.append(str(r.json()['access_log'][a]['timestamp'])) 
                dic.append(str(r.json()['access_log'][a]['type']))    
                dic.append(str(r.json()['access_log'][a]['facility']['name']))
                dic.append(str(r.json()['access_log'][a]['facility']['address']))
                dic.append(str(r.json()['access_log'][a]['facility']['id'])) 
                self.string_final.append(dic)
                self.lug_final.append((str(r.json()['access_log'][a]['facility']['id'])))
        return self.string_final
        
    def getAllData2(self):
        self.finicio='2021-01-01T00:00:00.277923+00:00'
        self.ffin='2021-12-31T23:59:59.277923+00:00'
        self.ffin=None
        self.string_final=[]
        self.lug_final=[]
        r = requests.get("http://localhost:8080/api/rest/user_access_log/"+self.userId, 
            headers={"x-hasura-admin-secret":"myadminsecretkey"})
        self.data = r.json()
        
        for a in range(len(r.json()['access_log'])):
                dic=[]
                dic.append(str(r.json()['access_log'][a]['temperature']))   
                dic.append(str(r.json()['access_log'][a]['timestamp'])) 
                dic.append(str(r.json()['access_log'][a]['type']))    
                dic.append(str(r.json()['access_log'][a]['facility']['name']))
                dic.append(str(r.json()['access_log'][a]['facility']['address']))
                dic.append(str(r.json()['access_log'][a]['facility']['id'])) 
                self.string_final.append(dic)
                self.lug_final.append((str(r.json()['access_log'][a]['facility']['id'])))
        return self.string_final

    
        
    def getAllData3(self):
        self.string_final2=[]
        self.rep=[]
        self.salida=[]
        self.salida_final=[]
        
        for a in range(len(self.string_final)):
            if(a%2==0):
                self.string_final2=[]
                self.string_final2.append(self.string_final[a][5])
                self.string_final2.append(self.string_final[a][3])
                self.string_final2.append(self.string_final[a][1])
                self.string_final2.append(self.string_final[a+1][1])
                self.rep.append(self.string_final2)
        
        for b in range(len(self.rep)):
            r = requests.get( "http://localhost:8080/api/rest/facility_access_log/"+self.rep[b][0]+"/daterange", 
                 headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
                 json={"startdate": self.rep[b][2], "enddate": self.rep[b][3]})

            for c in range(len(r.json()['access_log'])):

                if(self.userId!=r.json()['access_log'][c]['user']['uuid']):
                  
                    self.salida=[]
                    self.salida.append(str(r.json()['access_log'][c]['user']['uuid']))
                    self.salida.append(self.rep[c][0] + "(" +self.rep[c][1]+")")
                    self.salida.append(self.rep[c][2]+" - "+self.rep[c][3])
                    self.salida_final.append(self.salida)
                
        
        return self.salida_final

    def getData3(self,min):
        self.string_final2=[]
        self.rep=[]
        self.salida=[]
        self.salida_final=[]
        self.lista2entera=[]
        self.listanueva=[]

        for a in range(len(self.string_final)):
            if(a%2==0):
                self.string_final2=[]
                self.string_final2.append(self.string_final[a][1])
                self.string_final2.append(self.string_final[a][2])
                self.string_final2.append(self.string_final[a][0])
                self.string_final2.append(self.string_final[a+1][0])
                self.rep.append(self.string_final2)
        
        
        for b in range(len(self.rep)):
                       
            r = requests.get( "http://localhost:8080/api/rest/facility_access_log/"+self.rep[b][1], 
                 headers={"x-hasura-admin-secret":"myadminsecretkey"})

            self.lista2entera=[]
            self.listanueva=[]
            for c in range(len(r.json()['access_log'])): 
                if(self.userId!=r.json()['access_log'][c]['user']['uuid']):
                    self.lista2=[]
                    self.lista2.append(str(r.json()['access_log'][c]['user']['uuid']))
                    self.lista2.append(str(r.json()['access_log'][c]['timestamp']))
                    self.lista2.append(str(r.json()['access_log'][c]['type']))
                    self.lista2.append(self.rep[b][1])
                    self.lista2entera.append(self.lista2)

            for e in range(len(self.lista2entera)):
                if(self.lista2entera[e][2]=='IN'):
                    i=0
                    for f in range(len(self.lista2entera)):
                        if((self.lista2entera[e][0]==self.lista2entera[f][0]) & (i==0)):
                            self.listanue=[]
                            self.listanue.append(self.lista2entera[e][0])
                            self.listanue.append(self.lista2entera[e][1])
                            self.listanue.append(self.lista2entera[f][1])
                            self.listanue.append(self.lista2entera[e][3])
                            i+=1
                            self.listanueva.append(self.listanue)
            
            
            for d in range(len(self.listanueva)):
                self.fecha1=self.fechaparacomparar(self,self.listanueva[d][1])
                self.formateada1=datetime.strptime(self.fecha1,"%Y-%m-%d %H:%M:%S")
                self.fecha2=self.fechaparacomparar(self,self.rep[b][2])
                self.formateada2=datetime.strptime(self.fecha2,"%Y-%m-%d %H:%M:%S")
                self.fecha3=self.fechaparacomparar(self,self.listanueva[d][2])
                self.formateada3=datetime.strptime(self.fecha3,"%Y-%m-%d %H:%M:%S")
                self.fecha4=self.fechaparacomparar(self,self.rep[b][3])
                self.formateada4=datetime.strptime(self.fecha4,"%Y-%m-%d %H:%M:%S")
                
                if(self.formateada1<self.formateada2):
                    if(self.formateada3>self.formateada2):
                        self.guardamos=[]
                        self.guardamos.append(self.listanueva[d][0])
                        self.guardamos.append(self.listanueva[d][3])
                        self.guardamos.append(self.listanueva[d][1]+" - "+self.listanueva[d][2])
                        self.salida_final.append(self.guardamos)
                else:
                    if(self.formateada1<self.formateada4):
                        self.guardamos=[]
                        self.guardamos.append(self.listanueva[d][0])
                        self.guardamos.append(self.listanueva[d][3])
                        self.guardamos.append(self.listanueva[d][1]+" - "+self.listanueva[d][2])
                        self.salida_final.append(self.guardamos)
        
        return self.salida_final

    
    def fechaparacomparar(self, a):
        sep=a.split('T')
        
        hora=sep[1].split('.')
        devolver=sep[0]+' '+hora[0]
        return devolver
    
    
    def getData4(self, min):
        self.string_final=[]
        self.lug_final=[]
        r = requests.get( "http://localhost:8080/api/rest/user_access_log/"+self.userId+"/daterange", 
                 headers={"x-hasura-admin-secret":"myadminsecretkey"},
                 json={"startdate": self.finicio, "enddate": self.ffin})
        self.data = r.json()
        
        for a in range(len(r.json()['access_log'])):
            dic=[]  
            dic.append(str(r.json()['access_log'][a]['timestamp'])) 
            dic.append(str(r.json()['access_log'][a]['facility']['name']))
            dic.append(str(r.json()['access_log'][a]['facility']['id'])) 
            self.string_final.append(dic)
        
        result=self.getData3(self, min)
        
        return result

    #Setters

    def setUserId(self, userId):
        self.userId = userId

    def setfinicio (self, fininicio):
        self.finicio = fininicio

    def setfin (self, ffin):
        self.ffin = ffin

