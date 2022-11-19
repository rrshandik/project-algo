import os
import pandas as pd

def home () :
    os.system("cls")
    print ("""
================================================       
    Selamat Datang di Aplikasi 'To Pofarm'!
================================================ 
    """.center(50))
    input_awal = input ("Mulai belajar bertani? [y/t] : ")
    if input_awal == "y" :
        jenis_tanaman ()
    elif input_awal == "t" :
        print ("see you when i see you!")
        
    
def jenis_tanaman () : #inti alur kodingan
    os.system ('cls')
    print ("""
    Daftar jenis tanaman :
    1. Tomat
    2. Cabai
    """)
    input_2 = int(input ("Tanaman yang Anda pilih : "))
    if input_2 == 1 :
        tomat ()
        input_tomat = input ("Sudah siap untuk bercocok tanam? [y/t] : ")
        
        if input_tomat == "y" :
            tomat_day1 ()
            input_question_1 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
            
            if input_question_1 == "y" :
                tomat_progress1 ()
                input_question_2 = int(input ("\n1. Lanjut hari ke-2-4\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                
                if input_question_2 == 1 :
                    tomat_day2 ()
                    input_question_3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                    
                    if input_question_3 == "y" :
                        tomat_progress2 ()
                        input_question4 = int (input("\n1. Lanjut hari ke-5\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                        if input_question4 == 1 :
                            tomat_day5 ()
                            input_question5 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                            if input_question5 == "y" :
                                tomat_progress5 ()
                                input_question6 = int(input("\n1. Lanjut hari ke-10\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                                if input_question6 == 1 :
                                    tomat_day10 ()
                                    input_question7 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                    if input_question7 == "y" :
                                        tomat_progress10 () ; """sampe sini"""
                                elif input_question6 == 2:
                                    problem1 ()
                                    input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                                    
                                    if input_problem == 1 :
                                        print ("kosek rung tekan")
                                        
                                    elif input_problem == 2 :
                                        print ('ini juga belom')
                                        
                                    elif input_problem == 3 : 
                                        jenis_tanaman ()
                                elif input_question6 == 3 :
                                    hapus_progress (2)
                                    input_hapus = input ("Ulangi progress? [y/t] : ")
                                    if input_hapus == "y" :
                                        tomat_day5 ()
                                        input_question_3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                        if input_question_3 == "y" :
                                            tomat_progress5 ()
                                            input_question_4 = input ("lanjut? [y/t] : ")
                                            if input_question_4 == "y" :
                                                tomat_day10 ()

                            elif input_question5 == 't' :
                                problem1 ()
                                input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                                
                                if input_problem == 1 :
                                    print ("kosek rung tekan")
                                    
                                elif input_problem == 2 :
                                    print ('ini juga belom')
                                    
                                elif input_problem == 3 : 
                                    jenis_tanaman ()
                        elif input_question4 == 2 :
                            problem1 ()
                            input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                            
                            if input_problem == 1 :
                                print ("kosek rung tekan")
                                
                            elif input_problem == 2 :
                                print ('ini juga belom')
                                
                            elif input_problem == 3 : 
                                print ('nanti dulu ya teman')
                        elif input_question4 == 3 :
                            hapus_progress_tomat (1)
                            input_hapus = input ("Ulangi progress? [y/t] : ")
                            if input_hapus == "y" :
                                tomat_day2 ()
                                input_question_3 = input ("\nLanjut hari ke-5? [y/t] : ")
                                if input_question_3 == "y" :
                                    tomat_progress_hapus ()
                                    input_question4 = int (input("\n1. Lanjut hari ke-5\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                                    if input_question4 == 1 :
                                        tomat_day5 ()
                                        input_question5 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                        if input_question5 == "y" :
                                            tomat_progress5 ()
                                            input_question6 = int(input("\n1. Lanjut hari ke-10\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                                            if input_question6 == 1 :
                                                tomat_day10 ()
                                                input_question7 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                                if input_question7 == "y" :
                                                    tomat_progress10 () 
                                            elif input_question6 == 2:
                                                problem1 ()
                                                input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                                                
                                                if input_problem == 1 :
                                                    print ("kosek rung tekan")
                                                    
                                                elif input_problem == 2 :
                                                    print ('ini juga belom')
                                                    
                                                elif input_problem == 3 : 
                                                    jenis_tanaman ()
                                            elif input_question6 == 3 :
                                                hapus_progress (2)
                                                input_hapus = input ("Ulangi progress? [y/t] : ")
                                                if input_hapus == "y" :
                                                    tomat_day5 ()
                                                    input_question_3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                                    if input_question_3 == "y" :
                                                        tomat_progress5 ()
                                                        input_question_4 = input ("lanjut? [y/t] : ")
                                                        if input_question_4 == "y" :
                                                            tomat_day10 ()
                        
                    elif input_question_3 == 't' :
                        problem1 ()
                        input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                        
                        if input_problem == 1 :
                            print ("kosek rung tekan")
                            
                        elif input_problem == 2 :
                            print ('ini juga belom')
                            
                        elif input_problem == 3 : 
                            jenis_tanaman ()
                            
                elif input_question_2 == 2 :
                    problem1 ()
                    input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                    
                    if input_problem == 1 :
                        print ("kosek rung tekan")
                        
                    elif input_problem == 2 :
                        print ('ini juga belom')
                        
                    elif input_problem == 3 : 
                        print ('nanti dulu ya teman')
                        
                elif input_question_2 == 3 :
                    hapus_progress_tomat (0)
                    input_hapus = input ("Ulangi progress? [y/t] : ")
                    
                    if input_hapus == 'y' :
                        tomat_day1()
                        input_hapus1 = input ("Lanjut hari ke-2? [y/t] : ")
                        
                        if input_hapus1 == "y" :
                            tomat_progress1 ()
                            input_question_2 = int(input ("\n1. Lanjut hari ke-2-4\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))

                            if input_question_2 == 1 :
                                tomat_day2 ()
                                input_question_3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                
                                if input_question_3 == "y" :
                                    tomat_progress2 ()
                                    input_question4 = int (input("\n1. Lanjut hari ke-5\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                                    if input_question4 == 1 :
                                        tomat_day5 ()
                                        input_question5 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                        if input_question5 == "y" :
                                            tomat_progress5 ()
                                            input_question6 = int(input("\n1. Lanjut hari ke-10\n2. FAQ\n3. Hapus progress hari ini\n\nPilihanmu : "))
                                            if input_question6 == 1 :
                                                tomat_day10 ()
                                                input_question7 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                                if input_question7 == "y" :
                                                    tomat_progress10 () ; """sampe sini"""
                                            elif input_question6 == 2:
                                                problem1 ()
                                                input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                                                
                                                if input_problem == 1 :
                                                    print ("kosek rung tekan")
                                                    
                                                elif input_problem == 2 :
                                                    print ('ini juga belom')
                                                    
                                                elif input_problem == 3 : 
                                                    jenis_tanaman ()
                                            elif input_question6 == 3 :
                                                hapus_progress (2)
                                                input_hapus = input ("Ulangi progress? [y/t] : ")
                                                if input_hapus == "y" :
                                                    tomat_day5 ()
                                                    input_question_3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                                                    if input_question_3 == "y" :
                                                        tomat_progress5 ()
                                                        input_question_4 = input ("lanjut? [y/t] : ")
                                                        if input_question_4 == "y" :
                                                            tomat_day10 ()
                                    
                    elif input_hapus1 == "t" :
                        tomat_day1 ()
                    
            elif input_question_1 == "t" :
                problem1 ()
                input_problem = int(input ("Mana yang menjadi kesulitan Anda? : "))
                
                if input_problem == 1 :
                    print ("kosek rung tekan")
                    
                elif input_problem == 2 :
                    print ('ini juga belom')
                    
                elif input_problem == 3 : 
                    jenis_tanaman ()
                    
        elif input_tomat == "t" :
            print ("Baik. Sekian terima kasih!")
            
    elif input_2 == 2 :
        cabai ()
        input_cabai = input ("Sudah siap untuk bercocok tanam? [y/t] : ")
        
        if input_cabai == "y" :
            cabai_day1 ()
            input_question_cabe1 = input ("Apakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
            
            if input_question_cabe1 == "y" :
                cabai_progress1 ()
                input_question_cabe2 = input ("\nLanjut hari ke-2? [y/t] : ")
                
                if input_question_cabe2 == "y" :
                    cabai_day2 ()
                    input_question_cabe3 = input ("\nApakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
                    
                    if input_question_cabe3 == "y" :    
                        cabai_progress2 ()
            
                
def problem1 () :
    os.system ('cls')
    print ("Apa ada masalah?")
    print ('''
    Mungkin Frequently Asked Questions ini bisa membantumu ^^ :
    1. apa
    2. ya
    3. Home
           ''')

def problem2 () :
    os.system ("cls")
    print ("Apa ada masalah?")
    print ('''
    Mungkin Frequently Asked Questions ini bisa membantumu ^^ :
    1. siapa yang cape
    2. saya
    3. Home
           ''')
    
def tomat () :
    print ('Anda memilih TOMAT!')
    print ('\n====== Basic Knowledges! ======'.center(50))
    print ('''
    1. Memilih Bibit Dengan Tepat
    Langkah awal yang perlu kamu lakukan adalah dengan memilih bibit unggulan.
    Kamu bisa mendapatkannya di toko pertanian. Kamu juga bisa mengambil biji 
    tomat dari buahnya langsung.
    Cara mendapatkan biji tomat unggulan:
    •	Rendam benih/bibit tomat yang telah kering selama 15-20 menit
    •	Selanjutnya akan terlihat, bibit ada yang mengapung dan terendam. 
        Bibit yang baik adalah yang terendam.
        
    2. Siapkan Media Tanam
    •	Siapkan bibit tomat yang dibutuhkan untuk hidroponik
    •	Siapkan media tanam pengganti tanah seperti rockwool
    •	Siapkan rockwool dengan ukuran 2,5x2,5x2,5 cm
    •	Plastic hitam untuk menjaga cahaya agar tidak masuk saat penyemaian
    •	Siapkan bantalan rockwool seperti kerikil, arang atau lainnya.
    •	Siapkan air nutrisi berkisar pada angka 1300 ppm
    •	Siapkan semprotan fungisida untuk membasmi hama

    3. Proses Penyemaian
        Setelah Anda mendapatkan bibit unggulan pilihanmu, Anda jelas perlu 
        melakukan tahap selanjutnya, yaitu penyemaian!
        Berikut adalah cara penyemaian tanaman tomat pada rockwool :
    •	Siapkan rockwool, kemudian potong dengan ukuran 2,5 x 2,5 x 2,5 cm.
    •	Lubangi masing-masing rockwool untuk memasukkan bibit. Pada proses 
        ini pastikan rockwool tidak bolong
    •	Letakkan rockwool pada tray semai atau nampan
    •	Masukkan bibit pada lubang yang telah dibuat
    •	Siram rockwool dengan air hingga basah
    •	Tutup tray semai dengan plastic hitam agar cahaya tidak masuk dan 
        simpan di tempat yang gelap selama 2x24 jam
    •	Setelah 2 hari akan terlihat proses pertumbuhan kecambah. Pada proses 
        ini pindahkan tray semai ke tempat yang ada sinar matahari. Biasanya, 
        proses ini berlangsung 21-28 hari.
    •	Selama proses ini berlangsung, kamu harus sering memantau kondisi 
        tanaman tomatnya. Jika perlu tambahkan air agar kondisi rockwool lembap.

           ''')
    
def tomat_day1() :
    os.system ("cls")
    file_tomat = open ("./project akhir huhu/tomat.csv", 'w')
    # "project akhir huhu" dapat diganti dengan tempat di mana folder file ini disimpan ^^
        
    konten_tomat_1 = """
    Daily Tracker Day-1
    
    Yang perlu disiapkan adalah :
    1.	Siapkan bibit tomat
    2.	Air secukupnya
    3.	Polybag yang sudah diisi dengan media tanam tanah
    4.	Pupuk kandang
    
    Langkah-langkah :
    Rendam bibit (mempercepat pembelahan bijinya) di dalam 
    gelas lalu berikan air secukupnya dan tunggu 5 – 6 jam.
    """
    print (konten_tomat_1)    

def hapus_progress_tomat (hari) :
    os.system ('cls')
    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    df = df.drop (hari)
    print ("Progress terkini")
    print (df)
    
    
def tomat_progress1 () :
    os.system ("cls") 
    file_tomat = open ("./project akhir huhu/tomat.csv", 'a')
    konten_tomat_csv1 = "Hari Ke, status\n1, terlaksana"
    file_tomat.write (konten_tomat_csv1)
    file_tomat.close () 
        
    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    print ("\n\nProgress Anda sejauh ini")
    print (df)
            
def tomat_day2 () :
    os.system ("cls")
    print ("""
    Day 2 - 4:
    Bersiap untuk menanam
    
    Hal yang perlu Anda lakukan :
    1.	Siapkan polybag yang berisi media tanah 
    2.	Letakkan atau taburkan biji cabe yang telah di rendam 
        ke dalam polybag yang sudah berisi tanah
    3.	Kasih jarak antar bibit agar tidak menumpuk dan tidak 
        saling mendorong pada saat tumbuh.
    4.	Setelah bibit sudah di letakkan di tanah, taburkan pupuk 
        kandang secukupnya di atas biji yang sudah di tanam.
    5.	Berikutnya yang paling penting adalah siram bibit tersebut 
        dengan air secukupnya.
    6.	Setelah disiram sampai basah lalu polybag tersebut di tutup.
        Misal menggunakan kain selama 2 hari 2 malam (tempat gelap 
        bisa mempercepat pembelahan bijinya.) 

    """)
    
def tomat_progress2 () :
    os.system ("cls") 
    file_tomat = open ("./project akhir huhu/tomat.csv", 'a')
    konten_tomat_csv1 = "\n2-4, terlaksana"
    file_tomat.write (konten_tomat_csv1)
    file_tomat.close () 
        
    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    print ("\n\nProgress Anda sejauh ini")
    print (df)
    
def tomat_progress_hapus () :
    os.system ("cls")
    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    print ("\n\nProgress Anda sejauh ini")
    print (df)
    
def tomat_day5 () :
    os.system ("cls")
    print ("""
    Day 5-9

    Setelah di tutup selama 2 hari 2 malam, 
    di hari ke-5, biji sudah pecah. Dan di hari ke lima
    akan muncul batang tipis serta daun.

    """)
    
def tomat_progress5 () :
    os.system ("cls") 
    file_tomat = open ("./project akhir huhu/tomat.csv", 'a')
    konten_tomat_csv1 = "\n5-9, terlaksana"
    file_tomat.write (konten_tomat_csv1)
    file_tomat.close () 

    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    print ("\n\nProgress Anda sejauh ini")
    print (df)
    
def tomat_day10 () :
    os.system ("cls")
    print ("""
    Day-10
    
    Pada hari ke sepuluh, bibit sudah mulai pertumbuhan di tandai dengan muncul 4-5 daun.
    
    Lakukan :
    1.	Pisahkan dan sendirikan bibit-bibit ke dalam polybag baru agar pertumbuhan nya semakin cepat.
    2.	Setelah di tancapkan ke polybag yang baru, tusuk-tusuk tanah di sekeliling tanaman agar pada saat disiram, air-air nya akan meresap kedalam tanah.
    3.	Setelah semua sudah dipindahkan, siram tanaman dengan air secukupnya.
    4.	Apabila musim kemarau, siram tanaman dua kali sehari. Jika musim hujan jangan sering menyiram tanaman. Lakukan setiap hari.
    
    """)
    
def tomat_progress10 () :
    os.system ("cls") 
    file_tomat = open ("./project akhir huhu/tomat.csv", 'a')
    konten_tomat_csv1 = "\n10, terlaksana"
    file_tomat.write (konten_tomat_csv1)
    file_tomat.close () 
    
    file_csv_tomat = "./project akhir huhu/tomat.csv"
    df = pd.read_csv (file_csv_tomat)
    print ("\n\nProgress Anda sejauh ini")
    print (df)
    
def cabai () :
    print ('Anda memilih CABAI!')
    print ('\n====== Basic Knowledges! ======'.center(50))
    print ("""
    1. Penyemaian Benih
    Sejatinya, penyemaian benih membutuhkan waktu lama hingga 1 bulan. 
    Oleh karena itu,sebelum melakukan penanaman di polybag, Anda harus 
    melakukan penyemaian benih terlebih dahulu.
    
    Langkah-langkah penyemaian benih antara lain:
    •	Siapkan polybag atau pot kecil sebagai wadah penyemaian.
    •	Ayak tanah humus yang akan digunakan sebagai media tanam. 
        Setelah halus, masukkan tanah humus kedalam pot atau polybag.
    •	Pilih benih berkualitas. Anda bisa mendapatkannya di toko 
        pertanian ataupun mengambilnya 
        langsung dari buah cabe hasil panen.
    •	Rendam biji selama 24 jam kedalam air hangat terlebih dahulu.
    •	Pilih biji yang terendam lalu tebarkan di kain basah. Tunggu 
        hingga 3-4 hari hingga biji berkecambah.
    •	Pindahkan biji yang berkecambah kedalam pot atau polybag kemudian 
        tutupi benih dengan pasir halus.
    •	Paparkan benih cabe ke sinar matahari selama setengah hari hingga 
        pukul 2 siang lalu teduhkan hingga sore.

    2. Persiapan Media Tanam
    Teknik hidroponik tidak menggunakan tanah sebagai media. Sebagai gantinya, 
    Anda bisa menggunakan jenis-jenis media tanam lain seperti sekam, pasir, 
    kerikil, hingga air. Langkah persiapan yang harus dilakukan antara lain:
    •	Siapkan media tanam pengganti tanah seperti pasir, kerikil, sekam bakar, 
        dan serbuk gergaji halus.
    •	Siapkan pupuk kandang atau kompos serta pupuk NPK .
    •	Campurkan pupuk kandang dan NPK dengan perbandingan 
    •	Media yang telah dicampurkan kemudian dimasukkan kedalam polybag 
        setengah bagian. Setengah bagian 
        lagi diisi dengan campuran pupuk kandang dan NPK.
    •	Tutupi bagian atas polybag dengan menggunakan kerikil halus.

    3. Pemindahan Benih ke Media Hidroponik
    Ketika benih mencapai usia 1 bulan, maka Anda sudah bisa memindahkannya 
    ke media hidroponik polybag.
    •	Buat lubang tanam di bagian tengah polybag dengan kedalaman 5-8 cm.
    •	Pindahkan benih cabe kedalam lubang yang telah disiapkan.
    •	Setelah bibit dimasukkan, tutup tanah dan lakukan penyiraman secara 
        rutin agar benih tidak layu.
    •	Ketika melakukan proses pemindahan, Anda juga bisa langsung menancapkan 
        tongkat agar tanaman cabe 
        dapat berdiri kokoh. Namun,jangan tancapkan terlalu dekat dengan akar.
    •	Setelah semua benih dipindahkan, atur jarak antar polybag kurang 
        lebih 40-60 cm per polybag.

    4. Perawatan
    Perawatan cabe hidroponik sendiri terdiri dari penyiraman, pemupukan, 
    penyiangan gulma, dan pengendalian hama penyakit.
    •	Penyiraman
    Setiap hari pada pagi dan sore hari
    •	Pemupukan
    Pemupukan tanaman cabe hidroponik bisa menggunakan pupuk organik cair (POC)
    Proses pemupukan dilakukan setiap 4-5 hari sekali agar tanaman dapat 
    berkembang dengan baik.
    •	Pengendalian Hama Penyakit
    Untuk serangan hama serangga, maka gunakan insektisida. Fungisida 
    digunakan untuk mengatasi serangan jamur dan bakterisida digunakan untuk 
    mengatasi serangan bakteri.

    5. Pemanenan
    Cabe hidroponik bisa dipanen ketika memasuki usia 75 hari. Ciri-ciri cabe yang 
    bisa dipanen yaitu warna buahnya yang merah di seluruh bagian. 
    Puncak hasil panen biasanya didapat ketika memasuki masa panen ke-8 hingga ke-10.
    
    Agar hasil panen maksimal, maka Anda harus memperhatikan asupan nutrisi dan 
    unsur hara yang dibutuhkan oleh tanaman.
    
           """)
    
def cabai_day1 () :
    os.system ("cls")
    file_cabai = open ("./project akhir huhu/cabai.csv", 'w')
    # "project akhir huhu" dapat diganti dengan tempat di mana folder file ini disimpan ^^
    konten_cabai_1 = """
    Daily Tracker Day-1
    1. Menggunakan tanah pilihan
    2. Menyirami dengan sepenuh hati
    3. Direkam time-lapse
    """
    print (konten_cabai_1)
    
def cabai_progress1 () :
    os.system ("cls") 
    file_cabai = open ("./project akhir huhu/cabai.csv", 'a')
    konten_cabai_csv1 = "Hari Ke, status\n1, terlaksana"
    file_cabai.write (konten_cabai_csv1)
    file_cabai.close () 
        
    file_csv_cabai = "./project akhir huhu/cabai.csv"
    df = pd.read_csv (file_csv_cabai)
    print ("\n\nProgress Anda sejauh ini")
    print (df)

def cabai_day2 () :
    os.system ("cls")
    # "project akhir huhu" dapat diganti dengan tempat di mana folder file ini disimpan ^^
    konten_cabai_1 = """
    Daily Tracker Day-2
    1. Menggunakan tanah pilihan
    2. Menyirami dengan sepenuh hati
    3. Direkam time-lapse
    """
    print (konten_cabai_1)

def cabai_progress2 () :
    os.system ('cls')
    file_cabai = open ("./project akhir huhu/cabai.csv", 'a')
    konten_cabai_csv1 = "\n2, terlaksana"
    file_cabai.write (konten_cabai_csv1)
    file_cabai.close () 
        
    file_csv_cabai = "./project akhir huhu/cabai.csv"
    df = pd.read_csv (file_csv_cabai)
    print ("\nProgress Anda sejauh ini")
    print (df)

home ()
