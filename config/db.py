from .base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker    
from typing import Type    
class Db:
    url = ''


    def __connection(self):
        engine = create_engine(self.url, echo = True)
        return engine
    
    def aplay(self):
        Base.metadata.create_all(self.__connection())

    def __session(self):
        session_maker = sessionmaker(bind=self.__connection())
        session = session_maker()
        return session
    
    def add(self, table: Type[Base]):
        '''inseri informações na tabela'''

        _add = self.__session()
        _add.add(table)
        _add.commit()
        _add.close()

    def objects(self):
        ''''
        operações de INSERT DELETE UPDATE SELECT
        '''

        session = self.__session()
        return session    
                                     
    