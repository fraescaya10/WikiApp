from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )
from wikiapp.models.principal import Base

class Pagina(Base):
	__tablename__ = 'tpagina'
	uid = Column(Integer, primary_key=True)
	nombre = Column(Text, unique=True)
	detalle = Column(Text)