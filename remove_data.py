# remove_data
from save_book_all_data import save_book_all_data


def remove_data (book_list):
    print(' 1. You can delet/remove/clear book infromations one click :( ISBN Number)')
    
    input_1_2 = input('Choice any number: ')
    
    if input_1_2 == '1':
        isbn = input('Book ISBN Number: ')
        
        for i, book in enumerate(book_list):
            
            if book['isbn'] == isbn:
                book_list.pop(i)
                save_book_all_data(book_list)
                print(f'Your Book Data successfully Deleted.')
                return
        print('isbn number is not found')
        
    else:
        print(f'ISBN Number is not found.')
