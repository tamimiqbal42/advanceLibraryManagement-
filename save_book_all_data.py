# save_book_all_data
import csv
import json

# def save_book_all_data(book_list):
#     with open ('book_store.csv', 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(['Title', 'Author', 'ISBN', 'Year', 'Price', 'Quantity'])
#         # (f'{Titel:<30} {Author:<30} {ISBN:<15} {Year:<10} {Price:<10} {Quantity:<15}')
#         for book in book_list:
#             writer.writerow([book['titel'], book['author'], book['isbn'], book['year'], book['price'], book['quantity']])

def save_book_all_data(book_list):
    with open("all_books.json", "w", newline='') as json_file:
        json.dump(book_list, json_file)


def load_books():
    book_list = []
    
    try:
        with open('book_store.csv', 'r', newline='') as read_book:
            reader = csv.reader(read_book)
            next(reader)
            for book in reader:
                book_list.append({
                    'titel': book[0],
                    'author': book[1],
                    'isbn': book[2],
                    'year': book[3],
                    'price': book[4],
                    'quantity': book[5]
                })
    except FileNotFoundError:
        pass
    

    return book_list


# def append_book_data(book_data):
#     import csv

#     # Open the file in append mode
#     with open('book_store.csv', 'a', newline='') as csv_file:
#         writer = csv.writer(csv_file)
        
#         # If the file is empty, write the header
#         if csv_file.tell() == 0:  # Check if file is empty
#             writer.writerow(['Title', 'Author', 'ISBN', 'Year', 'Price', 'Quantity'])
        
#         # Append the new book data
#         writer.writerow([
#             book_data['title'], 
#             book_data['author'], 
#             book_data['isbn'], 
#             book_data['year'], 
#             book_data['price'], 
#             book_data['quantity']
#         ])

