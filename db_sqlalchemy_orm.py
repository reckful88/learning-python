#-*- coding: utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
db = create_engine("mysql://root:chrisk9999@localhost")
db.execute("use conference")
Base = declarative_base()
class User(Base):
	__tablename__ = 'users'
	
	user_id = Column(Integer, primary_key=True)
	name = Column(String(49))
	fullname = Column(String(40))
	password = Column(String(40))
	def __repr__(self):
		return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(db)
user = User(name='lfc', fullname='Li Fangcheng', password='iampassword')
print user.name
Session = sessionmaker(bind=db)
session = Session()
session.add(user)
session.commit()
user = session.query(User).filter(User.user_id==1).one()
print user.name
print user


'''
依旧别忘记DROP，mysql> drop tables users;
'''
