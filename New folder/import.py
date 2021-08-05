import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Book
import csv


engine= create_engine("postgresql://nvrcvodmyluvkf:dad009f026667d780a95bd8b05415254659b07dbdf8ad6da3544022788a034e8@ec2-3-230-38-145.compute-1.amazonaws.com:5432/d43vioe3vuckh1")
db_session = scoped_session(sessionmaker(bind=engine))
with open('books.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    for row in readCSV:
        new_book= Book(isbn=row[0],name=row[1],author=row[2], year=row[3])
        db_session.add(new_book)
db_session.commit()
db_session.close()
