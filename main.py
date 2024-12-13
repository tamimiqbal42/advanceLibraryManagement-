# Libaray Management System project:-
import add_book_infromations
import view_all_book_data
from save_book_all_data import load_books
import book_update
import remove_data
import restore_all_books


book_list = load_books()

while True:
    print( 'Welcome Advance Library Management System.')
    print( '0. Exit Program.')
    print( '1. Add Book.')
    print( '2. View Books.')
    print( '3. Update Book data.')
    print( '4. Delete or clear Book data.')
    
    book_list = restore_all_books.restore_all_books(book_list)

    enter_choice = input('Enter Your Choice:- ')

    if enter_choice == '0':
        print('Thanks Use Advance Library Management system.')
        break

    elif enter_choice == '1':
        add_book_infromations.add_book_infromations(book_list)

    elif enter_choice == '2':
        view_all_book_data.view_all_book_data(book_list)
        
    elif enter_choice == '3':
        book_update.book_update(book_list)

    elif enter_choice == '4':
        remove_data.remove_data(book_list)
    else:
        print('Invalid Choice.')

