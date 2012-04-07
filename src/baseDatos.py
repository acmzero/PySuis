'''
Created on 05/04/2012

@author: heli
'''

from PyQt4.QtSql import QSqlDatabase,QSqlQuery,QSqlError
from PyQt4.QtCore import QCoreApplication
import os
import sys
class base_datos(QSqlDatabase):
  def __init__(self):
    db=QSqlDatabase.addDatabase("QSQLITE")
    
    db.setHostName("localhost")
    a=QSqlError()
    if os.path.exists("pysuis.db"):
      db.setDatabaseName("pysuis.db")
      print self.db.open()
    else:
      w=open("pysuis.db","w")
      w.flush()
      w.close()
      db.setDatabaseName("pysuis.db")
      db.open()
      b=db.lastError()
      print b.text()
      #print self.db.open()
      c=crear_base()
      db.commit()


class crear_base():
  def __init__(self):
    self.comandos = []
    self.agregar_sentencias()
    if self.enviar_comandos():
      print self.comandos
      print "Tablas Creadas"
    
    
  def enviar_comandos(self):
    query=QSqlQuery()
    r=True
    for comando in self.comandos:
      if not query.exec_(comando):
        r=False
    
        
    return r
    
  def agregar_sentencias(self):
    g = lambda x: self.comandos.append(x)
    
    #Tabla de jugadores
    g("CREATE TABLE `jugadores` (`jugador_id` int  PRIMARY KEY, `Nombre` int, `Nick` int,  `Edad` int,  `Rating` int)")
    
    

