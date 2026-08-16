# Project: Reading Tracker
# Author: Natasha Sophia Ndhlovu

books = []
months = ["January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"]

name = input("Hi! What is your name?: ")
year = input("What is your current reading year?: ")
print()

print(f"Hello {name}! Welcome to your Reading Tracker!")
print()

while True:

 print("--------------------------------")
 print("         READING TRACKER        ")
 print("--------------------------------")
  
 print("1. Add a book.")
 print("2. View your books.")
 print("3. Exit.")
 print()

 option = input("What would you like to do?: ")
 print()

 if option == "1":
  title = input("What is the title of the book?: ")
  author = input("Who wrote it?: ")
  print("When did you finish reading it?")
  while True:
   try:
    day = int(input("Day?: "))
   except ValueError:
    print("Input has to be a number.")
    continue
   if day < 1 or day > 31:
    print("Invalid day. Please try again.")
   else:
      break
  while True:
    month = input("Month?: ")
    month = month.capitalize()
    if month not in months:
     print("Month is invalid. Please try again.")
    else:
     break
  date_finished = (f"{day}, {month}, {year}.") 
  while True:
    try:
     rating = int(input("What would you rate this book out of five?: "))
    except ValueError:
     print("Input has to be a number.")
     continue
    if rating < 1 or rating > 5:
     print("Rating is invalid. Please try again.")
    else:
     break
  book = {"Title": title,
            "Author": author,
            "Date_finished": date_finished,
            "Rating": rating}
  books.append(book)
  print()
  print("You have successfully added: ")
  print(f"Title: {book['Title']}")
  print(f"Author: {book['Author']}")
  print(f"Date_finished: {book['Date_finished']}")
  print(f"Rating: {book['Rating']}")
  print()

  input("Press enter to return to the main menu")
         
 elif option == "2":
  if len(books) == 0:
   print("You have not added any books yet.")
  else: 
   print(f"In {year}, you have read the following books: ")
   print()
   number_of_books = 1
   for book in books:
    print(f"{number_of_books}.")
    print(f"Title: {book['Title']}")
    print(f"Author: {book['Author']}")
    print(f"Date_finished: {book['Date_finished']}")
    print(f"Rating: {book['Rating']}")
    print()
    number_of_books += 1

   input("Press enter to return to the main menu")
   print()

 elif option == "3":
  break
 else:
    print("Your option is invalid.")

