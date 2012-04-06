'''
Created on 05/04/2012

@author: heli
'''
from PyQt4.QtSql import QSqlQuery

class Jugador():
  def __init__(self, id=None):
    
    self.id = id
    self.nombre = ""
    self.nick = ""
    self.edad = 0
    self.rating = 0
    
    
  def obtener_datos(self):
    query = QSqlQuery()
    
    sql = """select * from jugadores where jugador_id=%d """%self.id
    
    g=lambda x: query.value(x).toString()
    if query.exec_(sql):
      query.next()
      
      self.nombre=g(1)
      self.nick=g(2)
      self.edad=int(g(3))
      self.rating=int(g(4))
      
      return True
    else:
      print "Error al obtener datos del Jugador."
      return False
