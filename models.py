from database import Base
from sqlalchemy import Column, Integer, String,ForeignKey,Boolean,Text,Float
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class BooksCategory(Base):
    __tablename__ = 'books_category'
    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)

    def __repr__(self):
        return f'BooksCategory {self.id}: {self.name}'

class Books(Base):
    BOOK_JANRE =(
        ('Novel', 'novel'),
        ('Poetry','poetry'),
        ('NON_FICTION','non_fiction'),
        ('SCIENCE_FICTION','Science_fiction')
    )
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    author=Column(String, nullable=False)
    genre=Column(ChoiceType(BOOK_JANRE), default='ficton')
    publication_year=Column(Integer, nullable=False)
    price=Column(Float, nullable=False)
    description=Column(Text, nullable=False)
    is_available=Column(Boolean, default=True)
    book_category=Column("BooksCategory",back_populates='books')

    def __repr__(self):
        return f'Book {self.id}: {self.name}'
    


    
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name=Column(String, nullable=False)
    nationality=Column(String, nullable=False)
    birth_date=Column(String, nullable=False)
    death_date=Column(String, nullable=True)

    def __repr__(self):
        return f'Author {self.id}: {self.name}'
    
class Book_Author(Base):
    __tablename__ = 'book_author'
    book = Column("Books", back_populates='book_author')
    author = Column("Author", back_populates='book_author')

    def __repr__(self):
        return f'Book_Author {self.book.id} - {self.author.id}'
    
class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    comment=Column(Text, nullable=False)
    rating=Column(Integer, nullable=False)
    book=Column("Books",back_populates='review')
    user=Column("User", back_populates='review')
    
    def __repr__(self):
        return f'Review {self.id}: {self.comment}'
    