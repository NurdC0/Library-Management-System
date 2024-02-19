

class Library:

    def __init__(self):
        self.file = open("books.txt", "a+")   # a: yazmak için dosyayı açar ve sonuna append eder. +:update etmek(yazma,okuma) için disk dosyasını açar.

    def __del__(self):
        self.file.close()    #dosyayı kapatır.

    def list_books(self):

        self.file.seek(0)  #dosyanın içinde başına git.
        split = self.file.read().splitlines()   #dosyayı oku ve satırlara böl. Örneğin split[0]=Momo,Michael Ende,1973,304

        for i in split:                   # Dosya içinde Satırlar haline gelmiş split listesini virgüle göre split et. 1. element: book name,  2. element: book author. sonra yazdır.
            book1 = i.split(",")             #Split dizisini ilk elementi yukarıdaki string. Bunu virgüle göre split ediyoruz. Yeni bir list var elimizde.
            book_names = book1[0].strip()         # Bu listenin ilk element kitap ismi 2. elementi de yazar ismi
            book_author = book1[1].strip()
            print(f"Book: {book_names}, Author: {book_author}")     #yazdırarak listeliyoruz.

    def add_books(self):
        book_title = input("Please enter the book title: ")
        book_author = input("Please enter the book author: ")
        release_year = input("Please enter release year of the book: ")
        total_pages = input("Please enter the total number of pages of book: ")

        book_data = f"{book_title}, {book_author}, {release_year}, {total_pages}\n"

        self.file.write(book_data)                #kullanıcıdan kitap datalarını iste. book_data isminde bir string oluştur. bunu dosyaya yazdır.
        print("Book added successfully")
        self.file.seek(0, 2)                      #her yazdıktan sonra dosyanın içinde sona git.

    def remove_books(self):

        removed_book = input("Please enter the title of book to be removed: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()   #her girilen kitabı lines isminde ve satır satır olacak şekilde tutan değişken
        books_list = [line for line in lines]   #üstte oluşturulmuş lines string ini kopyala ve books_list isminde br değişkende tut.

        removed_index = None
        for index, book_data in enumerate(books_list):      #enumerate fonksiyonu bir dizi içinde hem index hem de o indexe karşılık gelen value elde etmek için.
            if removed_book in book_data:                   #burada index: index,  book_data: value
                removed_index = index                     #kullanıcı kitabın ismini girer. for döngüsü kopyalanmış books_list'e bakar ve kitap ismi value değerleri içinde..
                break                                # varsa onun indexini bulur.

        if removed_index is not None:                 # isim ve listedeki valuelardan biri eşleşirse. O index yani element silinir. Kitap silindi.
            del books_list[removed_index]

            self.file.seek(0)                  #dosyanın başına git.
            self.file.truncate()               # truncate orjinal(self) dosyanın içindeki bütün verileri siler.

            for book_info in books_list:               #daha önce book_list kopyalanıp içindeki eşleşen index silinmişti.Bu yeni stringleri tekrar dosyaya yazdırıyoruz.
                self.file.write(book_info + '\n')

            print("Book removed successfully")

    def edit_book_info(self):

        edit_part = input("Enter the title of book you want to edit: ")     #kullanıcıya editlemek istediğimiz kitabın adını soruyoruz.

        self.file.seek(0)                            #dosyanın başına gidip, okuyoruz,satırlara bölüyoruz ve yeniden books_list isminde kopyalıyoruz.
        lines = self.file.read().splitlines()
        books_list = [line for line in lines]

        edited_index = None                            #editlemek istediğimiz kitabı adını buluyoruz for döngüsüyle. Remove'daki for ile aynı mantık.
        for i, book_data in enumerate(books_list):
            if edit_part in book_data:
                edited_index = i
                break

        if edited_index is not None:            #eşleşme olursa kullanıcıya kitabın hangi ismini editlemek istediğini soruyoruz.

            part_to_edit = input("Which part of book info you want to edit(title - author - year - pages):")

            new_info = input(f"Enter the new info for {part_to_edit}: ")       # part bilgisi geldikten sonra yeni bilgiyi soruyoruz.

            book_info_new = books_list[edited_index].split(",")   #kitap ismiyle bulduğumuz indexi biliyoruz artık.bu indexi kullanarak booka_list içindeki string i virgülle split.
            if part_to_edit.lower() == "title":                   #örneğin books_list[3]=Simyacı,Paula Coelho,1988,310 olsun. 3 indexini simyacı'yı books listten bakarak bulduk.
                book_info_new[0] = new_info.strip()               # şimdi bu texti (Simyacı,Paula Coelho,1988,310) virgülle ayırıyoruz.
            elif part_to_edit.lower() == "author":                #kullanıcıda gelen part bilgisi if-elif statementlarıyla eşleşirse book_info_new adıyla oluşturduğumuz string değişkeni
                book_info_new[1] = new_info.strip()               #ve ilgili indexe karşılık gelen yere göre assign ediyoruz. yeni stringi editlemek istediğimiz stringle değiştiriyoruz.
            elif part_to_edit.lower() == "year":
                book_info_new[2] = new_info.strip()
            elif part_to_edit.lower() == "pages":
                book_info_new[3] = new_info.strip()

            updated_book_info = ", ".join(book_info_new)         #daha önce parça pinçik olan küçük stringçiklerimizi aralarına virgül konulacak şekilde birleştiriyoruz.

            books_list[edited_index] = updated_book_info         #Editlemek istediğimiz part bilgisinin ait olduğu kitap info stringinin indexini bulmuştuk.
                                                                 #Join methoduyla birleştirdiğimiz yeni editlenmiş stringimizi eski stringin yerine koyuyoruz.

            self.file.seek(0)                           #orjinal dosyanın en başına gidip, içindeki bütün bilgileri siliyoruz.
            self.file.truncate()

            for book_info in books_list:                 #yeni editlenmiş books_listimizi dosyaya yazdırıyoruz. Her yazımdan sonra alt satıra geçiyoruz.
                self.file.write(book_info + '\n')

            print("Book information edited successfully")


lib = Library()


while True:                             #Durdurulmazsa sonsuza kadar giden bir whlie loop'u. Q tuşuyla sonlandıracağız.
    print("\n*** MENU ***")
    print("1) List Book")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Edit Book Info")
    print("5) Q to quit")

    choice = input("Please enter your choice: ")       #kullanıcıya hangi işlemi yapmak istediğini soruyoruz.

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()                       #çağırılan işleme karşılık gelen methodları işletiyoruz.
    elif choice == "3":
        lib.remove_books()
    elif choice == "4":
        lib.edit_book_info()
    elif choice.lower() == "q":
        break
    else:
        print("Please enter the valid choice.")