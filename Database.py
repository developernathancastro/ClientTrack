from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

database = "sqlite:///Clientes.db"
engine = create_engine(database, echo=True)  # O parâmetro 'echo=True' exibe as instruções SQL geradas (opcional)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Clientes(Base):
    __tablename__ = 'Clientes'  # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cnpj = Column(Integer, nullable=False, unique=True)
    data_cadastro = Column(DateTime, nullable=False, default=func.now())
    estado = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    tipo_de_cliente = Column(String, nullable=False)

Base.metadata.create_all(engine)





