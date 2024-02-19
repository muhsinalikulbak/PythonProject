import string


class Library:
    def __init__(self):
        self.library = open("books.txt", "w")

    def BookAdd(self, bookName, author, date, pages):
        if bookName==""or bookName==" "or bookName == "  ":
            return string.whitespace
        with open("books.txt",
                  "r") as file:  # With keywordü dosyayı açar ve metotdan çıktığında otomatik olarak kapatır.
            books = file.read().splitlines()
            lowBookName=bookName.lower()
        with open("books.txt", "a+") as file:
            for book in books:
                if book.lower().startswith(lowBookName):
                    return False
            file.write(f"{bookName},{author},{date},{pages}\n")
            return True

            # Burada textin listesini metodu çağırırken parametreye books adıyla gönderiyorum ardından texti silip silinecek kitap hariç
            # tüm kitapları books üzerinden tekrar texte yazıyorum.
            # eğer silinecek kitapa denk gelmediyse böyle bir kitap yoktur ve sonuç olarak false döndürerek hata verecektir.

    def BookRemove(self, removeName):
        with open("books.txt", "r") as file:
            books = file.read().splitlines()
            if len(books) == 0:
                return string.whitespace
            elif removeName=="":
                return False

        with open("books.txt", "w") as file:
            control = False
            for book in books:
                if not book.lower().startswith(removeName):
                    file.write(book)
                else:
                    control = True
            return control


    def BookList(self):
        with open("books.txt", "r") as file:
            list = file.read().splitlines()  ## list = file.readlines()
        print("\n")
        for i in list:
            print("Book : " + i) # Book classı oluştursaydık satır satır kitap ismi yazarını yazdırabilirdik. Yine yapabiliriz ama book classı
                                 # ile yapmak daha iyi ve temiz olacağı için burada bunu yapmak istemedim :D


def main():
    lib = Library()
    while True:
        choice = input("""
        ******Hoş geldiniz******
    
        Kitap ekleme --> 1
        Kitap silme --> 2
        Kitap listeleme --> 3
        Çıkış yapma --> Q
        
        Seçim --> """)
        if choice == "1":
            while True:
                name = input("Kitap ismi : ")
                author = input("Kitabın yazarı : ")
                date = input("Kitabın yayımlanma tarihi : ")
                pages = input("Sayfa sayısı : ")
                result =lib.BookAdd(name, author, date, pages)
                if result ==string.whitespace:
                    print("\n!Geçersiz giriş\n")
                elif result:
                    print("\nKitabı rafımıza ekledik\n")
                    break
                else:
                    print("\nBu kitabı  zaten eklemişsin\n")

        elif choice == "2":

            while True:
                with open("books.txt", "r") as file:
                    name = input("Silmek istediğiniz kitabın ismi : ").lower()
                    result = lib.BookRemove(name)
                    if result == string.whitespace:
                        print("\n!Listede silinecek kitap yok\n")
                        break
                    elif result:
                        print("\nKitabı raftan süpürdük\n")
                        break
                    else:
                     cont =False
                     print("\nBöyle bir kitabı aradık ardık bulamadık\n")
                     while True:
                            choice=input("\n\nMenü için --> 1\nTekrar denemek için --> 2 \nSeçim : ")
                            if choice =="1":
                                cont=True
                                break
                            elif choice=="2":
                                break
                            else:
                                print("\n!Geçersiz seçim")
                    if cont:
                     break





        elif choice == "3":
            lib.BookList()
        elif choice.lower() == "q":
            print("\n--Uygulama başarıyla sonlandı--")
            return  # return ile metodu sonlandırabilir ya da değer döndürerek de sonlandırabilirim :D
        #             Aslında break ile while'ı kırsam metodun başka yapacağı iş olmadığı için yine metotdan çıkar
        else:
            print("\nGeçersiz seçim tekrar deneyiniz.")

main()
