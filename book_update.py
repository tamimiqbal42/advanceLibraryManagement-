# book_update
from save_book_all_data import save_book_all_data

def book_update (book_list):
    print(' 1. You can update book infromations one click :( ISBN Number)')
    print('or')
    print(' 2. You can update book infromations especific( ex: titel,author,price or quantity)')
    
    input_1_2 = input('Choice any number: ')

    if input_1_2 == '1':
        isbn = input('Book ISBN Number: ')
        for book in book_list:
            if book['isbn'] == isbn:
                print(f'Updating Book {book['titel']}')
                book['titel'] = input(f'Enter new book Titel name(current: Titel name- {book['titel']}:) ')
                book['author'] = input(f'Enter new book Author name(current:  Author name- {book['author']}:) ')
                book['year'] = input(f'Enter new book year(current: year- {book['year']}:) ')
                book['price'] = input(f'Enter new book Price(current: Price- {book['price']}:) ')
                book['quantity'] = input(f'Enter new book Quantity(current: book Quantity- {book['quantity']}:) ')

                save_book_all_data(book_list)
                print(f'Book name {book['titel']} and ISBN {book['isbn']} update successfully.')
                return
                break
        else:
            print(f'ISBN Number is not found.')

    elif input_1_2 == '2':

        isbn = input('Book ISBN Number:--- ')

        for book in book_list:
            if book['isbn'] == isbn:
                print(f'1. change book Titel name(current: Titel name- {book['titel']}:) ')
                print(f'2. change book Author name(current:  Author name- {book['author']}:) ')
                print(f'3. change book year(current: year- {book['year']}:) ')
                print(f'4. change book Price(current: Price- {book['price']}:) ')
                print(f'5. change book Quantity(current: book Quantity- {book['quantity']}:) ')

                all_number = input('choice any number: ')

                if all_number == '1':
                    print(f'Updating Book {book['titel']}')
                    book['titel'] = input(f'Enter new book Titel name(current: Titel name- {book['titel']}:) ')
                    save_book_all_data(book_list)
                    print(f'Book name {book['titel']} update successfully.')
                    return

                elif all_number == '2':
                    print(f'Updating Book {book['author']}')
                    book['author'] = input(f'Enter new book author name(current: author name- {book['author']}:) ')
                    save_book_all_data(book_list)
                    print(f'Book name {book['author']} update successfully.')
                    return

                elif all_number == '3':
                    print(f'Updating Book {book['year']}')
                    book['year'] = input(f'Enter new book year (current: year- {book['year']}:) ')
                    save_book_all_data(book_list)
                    print(f'Book name {book['year']} update successfully.')
                    return

                elif all_number == '4':
                    print(f'Updating Book {book['price']}')
                    book['price'] = input(f'Enter new book price (current: price- {book['price']}:) ')
                    save_book_all_data(book_list)
                    print(f'Book name {book['price']} update successfully.')
                    return

                elif all_number == '5':
                    print(f'Updating Book {book['quantity']}')
                    book['quantity'] = input(f'Enter new book quantity (current: quantity- {book['quantity']}:) ')
                    save_book_all_data(book_list)
                    print(f'Book name {book['quantity']} update successfully.')
                    return

                else:
                    print('Invalid Number Input.')

        else:
            print(f'ISBN Number is not found.')
    





