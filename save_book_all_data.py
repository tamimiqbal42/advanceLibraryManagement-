# save_book_all_data
# import csv
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



    return book_list



