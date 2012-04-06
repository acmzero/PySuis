'''
Created on 05/04/2012

@author: heli
'''

from PyQt4.QtSql import QSqlDatabase
class base_datos(QSqlDatabase):
  def __init__(self):
    self.addDatabase("QMYSQL")
    self.setDatabaseName("PySuis")
    self.setUserName("root")
    self.setPassword("kaka")
    self.setHostName("localhost")







class crear_base():
  def __init__(self):
    self.comandos = []
    
  def agregar_sentencias(self):
    g = lambda x: self.comandos.append(x)
    
    #Tabla de jugadores
    g("CREATE TABLE `jugadores` (`jugador_id` int  PRIMARY KEY, `Nombre` int, `Nick` int,  `Edad` int,  `Rating` int)")
