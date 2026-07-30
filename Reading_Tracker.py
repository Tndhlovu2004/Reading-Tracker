books = []

name = input("Hi! What is your name? ")

print(f"Hello! {name} Welcome to your Reading Tracker!")

while True:

 print("--------------------------------")
 print("         READING TRACKER        ")
 print("--------------------------------")
  
 print("1. Add a book")
 print("2. View your books")
 print("3. Exit")

 option = input("What would you like to do?: ")

 if option == "1":
  title = input("What is the title of the book?: ")
  author = input("Who wrote it?: ")
  date_finished = input("When did you finish reading it? (Day, Month, Year): ")
  rating = input("What do you rate this book out of five?: ")
  book = {"Title": title,
            "Author": author,
            "Date_finished": date_finished,
            "Rating": rating}
  books.append(book)
  print("You have successfully added: ")
  print(book)

 elif option == "2":
  if len(books) == 0:
   print("You have not added any books yet")
  else: 
   print("In 2026, you have read the following books: ")
   number_of_books = 1
   for book in books:
    print(f"{number_of_books}.")
    print(book)
    number_of_books += 1

 elif option == "3":
  break
 else:
    print("Your option is invalid.")

