import gettext
import requests
from pathlib import Path
_ = gettext.gettext
N_ = gettext.ngettext

#Lista de usuarios (uuid, username, name, surname, email, phone, is_vaccinated)
class Model:
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def getData(self):
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
        
    
    def getData2(self):
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

    def getData3(self):
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
            r = requests.get( "http://localhost:8080/api/rest/facility_access_log/"+self.rep[b][0]+"/daterange?offset=0&limit=100", 
                 headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
                 json={"startdate": self.rep[b][2], "enddate": self.rep[b][3]})

            for c in range(len(r.json()['access_log'])): 
                if(self.userId!=r.json()['access_log'][c]['user']['uuid']):
                  l=0
                  
                  self.salida=[]
                  self.salida.append(str(r.json()['access_log'][c]['user']['uuid']))
                  self.salida.append(self.rep[c][0] + "(" +self.rep[c][1]+")")
                  self.salida.append(self.rep[c][2]+" - "+self.rep[c][3])

                

            if(self.salida!=[]):
                l=0     
                for i in range (len(self.salida_final)):
                  if self.salida_final[i][0] == self.salida[0]:
                    if self.salida_final[i][2] == self.salida[2]:
                        l+=1 
                if (l==0):
                  self.salida_final.append(self.salida)
        return self.salida_final

    def getData4(self):
        # self.finicio='2021-01-01T00:00:00.277923+00:00'
        # self.ffin='2021-12-31T23:59:59.277923+00:00'
        # self.ffin=None
        self.string_final=[]
        self.lug_final=[]
        
        r = requests.get( "http://localhost:8080/api/rest/user_access_log/"+self.userId+"/daterange", 
                 headers={"x-hasura-admin-secret":"myadminsecretkey"},
                 json={"startdate": self.finicio, "enddate": self.ffin})
        self.data = r.json()
        print(r)
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
        result=self.getData3(self)
        
        return result

    #Tabla de accesos a instalaciones segun usuario(temperature, timedate, type(IN/OUT)
    # facility_name, facility_address, facility_id)
    def getUserData(self):
        r = requests.get("http://localhost:8080/api/rest/user_access_log/"+self.userId, 
            headers={"x-hasura-admin-secret":"myadminsecretkey"})
        self.data = r.json()
        return self.data
    
    def getFilteredData2(self):
        r = requests.get( "http://localhost:8080/api/rest/user_access_log/"+self.userId+"/daterange", 
            headers={"x-hasura-admin-secret":"myadminsecretkey"}, 
            json={"startdate": +self.startDate, "enddate": +self.endDate})
        self.data = r.json()
        return self.data

    #Setters

    def setUserId(self, userId):
        self.userId = userId

    def setfinicio (self, fininicio):
        self.finicio = fininicio

    def setfin (self, ffin):
        self.ffin = ffin