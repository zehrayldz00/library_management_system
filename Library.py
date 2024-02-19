class Library:
    def __init__(self): # dosya oluşturma fonksiyonu
        self.database = open("books.txt", "a+") # self.database değişken ismi ile books.txt adlı txt dosyasını a+ yani hem yazma hem okuma modunda oluşturduk. 

    def __del__(self): # dosya kapatma fonksiyonu
        if hasattr(self, 'self.database') and self.database is not None: # Bu bölümde gbtden yardım aldık. q harfine bastığımız zaman dosyayı kapatmak için bu fonksiyon çalışacak.
            self.database.close() 

    def list(self): # listeleme fonksiyonu
        self.database.seek(0)  # bu dosya içinde okumadan önce başa dönmeyi sağlıyor
        lines = self.database.read().splitlines() # satırları listeye atadık

        if not lines: # eğer satır yoksa
            print("No books found.") # kitap yok yazdır
            return

        for line in lines: # lines listesi içindeki her bir line elemanı için yani her bir satır için
            book_info = line.split(",") # satırı virgül gelen yerlerden parçala
            print(f"Title: {book_info[0]}, Author: {book_info[1]}") # ve sadece yazar adı ve kitap adı yazdırmamız lazım olduğu için book info listesinin 0. ve 1. indeksindeki elemanları getir

    def add(self): # Kitap ekleme fonksiyonu
        book_name = input("Write the book's name: ") # Kitap ismini istedik
        authors_name = input("Write the author's name: ") # Yazar ismini istedik
        release_year = input("Write the first release year: ") # Yayın yılını istedik
        page_count = input("Write the count of pages: ") # Sayfa sayısını istedik

        book_info = f"{book_name},{authors_name},{release_year},{page_count}\n" # Tüm bu bilgileri "book_info" isminde bir listeye atadık
        self.database.write(book_info) # Bu listeyi self.database e yani books.txt dosyasına yazdırdık.

    def remove(self): # silme fonksiyonu # buradaki fonksiyonlar için gbtden yardım aldık.
        
        book_to_remove = input("Write the name of the book : ") # silinecek kitabın adını istedik
        self.database.seek(0)  # bu dosya içinde okumadan önce başa dönmeyi sağlıyor
        lines = self.database.read().splitlines() # satırları listeye atadık

        updated_lines = [line for line in lines if not line.startswith(book_to_remove + ",")] # silinecek kitabın adıyla başlayan satırları filtreleyerek güncellenmiş satırları elde ettik

        self.database.seek(0)  # bu dosya içinde okumadan önce başa dönmeyi sağlıyor
        self.database.truncate()  # liste içeriğini düzenledik silinen öge gittikten sonra
        self.database.writelines("\n".join(updated_lines))  # yeni satırları dosyaya yazdık



lib = Library() # library classından lib isimli nesne oluşturduk

lib.__init__()


while True: # döngü içine aldık ki çıkış yapana kadar sürekli bu menü açılsın
    print("\n*** MENU ***\n1) List Books\n2) Add Book\n3) Remove Book") # kullanıcıya sunulan menü
    
    choice = input("Enter your choice : ") # kullanıcının seçim yapmasını istedik ve bunu choise değişkenine atadık.

    if choice == "1": # 1 e basılırsa
        lib.list() # listeleme fonksiyonu çalışsın
    elif choice == "2": # 2 ye basılırsa
        lib.add() # ekleme fonksiyonu çalışsın
    elif choice == "3": # 3 e basılırsa
        lib.remove() # silme fonksiyonu çalışsın
    elif choice.lower() == "q": # q harfine basılırsa
        break # programdan çıksın ve dosya kapansın
    else: # bunlar dısında herhangi bir tuşa basılırsa 
        print("Invalid choice. Please enter a valid option.") # uyarı versin ve geçerli bir seçenek istesin.
