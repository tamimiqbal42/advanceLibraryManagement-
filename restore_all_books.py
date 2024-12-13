import json

def restore_all_books(book_list):
    with open("all_books.json", "r") as fp:
        book_list = json.load(fp)
    
    return book_list