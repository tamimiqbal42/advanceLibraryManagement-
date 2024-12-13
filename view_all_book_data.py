# view_all_book_data

def view_all_book_data (book_list):
    if not book_list:
        print(f'Book Not Avilable.')

    else:
        print('_'*90)

        print(f'{'TITEL':<20} {'AUTHOR':<18} {'ISBN':<13} {'YEAR':<13} {'PRICE':<13} {'QUANTITY':<13}')
        print('_'*90)
        print('_'*90)

        for index, book in enumerate(book_list, start=1):
            # print(index)
            print(f'{index}. {book['titel']:<20}{book['author']:<20}{book['isbn']:<15}{book['year']:<15}{book['price']:<15}{book['quantity']:<15}')
            print('_'*90)
