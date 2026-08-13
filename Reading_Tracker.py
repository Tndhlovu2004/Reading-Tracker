books = []
months = ["January, "
"Febuary, "
"March,"
" April, "
"May,"
" June,"
" July, "
"August, "
"September,"
" October,"
" November,"
" December"]

year = input("What is your current reading year?: ")
name = input("Hi! What is your name?: ")

print(f"Hello! {name} Welcome to your Reading Tracker!")

while True:

 print("--------------------------------")
 print("         READING TRACKER        ")
 print("--------------------------------")
  
 print("1. Add a book.")
 print("2. View your books.")
 print("3. Exit.")

 option = input("What would you like to do?: ")

 if option == "1":
  title = input("What is the title of the book?: ")
  author = input("Who wrote it?: ")
  print("When did you finish reading it?: ")
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
   ("You have successfully added: ")
   print(book)

 elif option == "2":
  if len(books) == 0:
   print("You have not added any books yet.")
  else: 
   print(f"In {year}, you have read the following books: ")
   number_of_books = 1
   for book in books:
    print(f"{number_of_books}.")
    print(book)
    number_of_books += 1

 elif option == "3":
  break
 else:
    print("Your option is invalid.")

