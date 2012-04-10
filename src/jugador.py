'''
Created on 05/04/2012

@author: heli
'''
from PyQt4.QtSql import QSqlQuery
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import sqlite3
from baseDatos import base_datos

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
from ui.juegador import Ui_Form_altas
class ventana_jugador(QWidget,Ui_Form_altas):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self)
    self.pb_aceptar.clicked.connect(self.agregar_jugador)
    
  def agregar_jugador(self):
    connection = sqlite3.connect('pysuis.db')
    cursor= connection.cursor()
    datos=self.obtener_datos_de_formulario()
    cursor.execute('''insert into jugadores (Nombre,Nick,Edad,Rating) values (?,?,?,?)''',datos)
    cursor.commit()
  def obtener_datos_de_formulario(self):
    # Nombre, Nick, Edad, Rating
    datos=[]
    
    datos.append(self.le_nombre.text())
    datos.append(self.le_nick.text())
    datos.append(int(self.le_edad.text()))
    datos.append(self.le_rating.text())
    
    return datos

if __name__=="__main__":
  app=QApplication(sys.argv)
  d=base_datos()
  form=ventana_jugador()
  form.show()
  app.exec_()
  