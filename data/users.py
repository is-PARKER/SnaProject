from pickle import FALSE
import sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from data.modelbase import Base

class User(Base):
    __tablename__ = 'user'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    google_sub_id = sqlalchemy.Column(sqlalchemy.Text,unique=True, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime())
    last_login = sqlalchemy.Column(sqlalchemy.DateTime())
    private_models = sqlalchemy.Column(sqlalchemy.BINARY, default=FALSE)

    models = relationship('Models', backref='user')