# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declared_attr, declarative_base


# class PreBase:

#     @declared_attr
#     def __tablename__(cls):
#         return cls.__name__.lower()

#     id = Column(Integer, primary_key=True)


# Base = declarative_base(cls=PreBase)


# class Hero(Base):
#     name = Column(String(50), unique=True)
#     health = Column(Integer)
#     force = Column(Integer)
#     dexterity = Column(Integer)
#     magic = Column(Integer)
#     speed = Column(Integer)
#     protection = Column(Integer)
#     experience = Column(Integer)
#     nobility = Column(Integer)

# class Inventary(Base):


# if __name__ == '__main__':
#     engine = create_engine('sqlite:///sqlite.db', echo=True)
