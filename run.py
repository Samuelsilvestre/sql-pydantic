from src.config.db import Db
from src.schema.usuario import User



class Ex(Db):
    url = 'mysql+mysqldb://root:password@localhost/db'

    def objects(self):
        session =  super().objects()
        queryset = session.query(User).all()
        return self.select(queryset)

    def select(self, queryset):
        data = [ {
            'id': attr.id,
            'email': attr.email,
            'user_name': attr.user_name
        } for attr in queryset ]
        return data



        




