# add_book_infromations
from save_book_all_data import save_book_all_data
import random
from datetime import datetime


def add_book_infromations (book_list):
    titel = input('Enter Book Titel Name: ')
    author = input('Enter Book Author Name: ')
    # isbn = input('Enter Book ISBN Number: ')
    year = input('Enter Book Year: ')
    price = input('Enter Book Price:')
    quantity = input('Enter Book Quantity: ')
    
    isbn = random.randint(10000, 99999)
    bookAddedAt = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    book_all_data ={
        'titel': titel,
        'author': author,
        'isbn' : isbn,
        'year': year,
        'price': price,
        'quantity': quantity,
        'bookAddedAt': bookAddedAt,
    }

    book_list.append(book_all_data)
    save_book_all_data(book_list)

    print('Book All Data Added Successfully.')

    return book_list