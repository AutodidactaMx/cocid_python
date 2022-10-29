from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = "persona"
    curp = Column(String(30), primary_key=True)
    nombre = Column(String(30))
    edad = Column(String(30))
    correo = Column(String(30))
    telefono = Column(String)        
    def __repr__(self):
        return f"tb_persona(id={self.curp!r}, name={self.nombre!r}, fullname={self.correo!r}, fullname={self.telefono!r})" 

