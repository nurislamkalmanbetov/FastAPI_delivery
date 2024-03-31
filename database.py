from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine('postgresql://postgres:qwerty123@localhost/pizza', echo=True)

Base=declarative_base() # helping by update, delete db

Session=sessionmaker()