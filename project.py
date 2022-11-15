

print ('Selamat Datang di Aplikasi "To Pofarm"!\n')
print ("""Di sini, kalian akan kami pandu untuk dapat mulai
bercocok tanam menggunakan metode hidroponik ^ ^""")


print ("""
Daftar jenis tanaman :
1. Tomat
2. Timun
3. Sawi""")
input_2 = int(input ("Tanaman yang Anda pilih : "))
if input_2 == 1 :
    print ("Baik, berikut penjelasannya : ")
    print ("\nAlat dan bahan yang harus anda siapkan meliputi : ")
    input_tomat = input ("Sudah siap untuk bercocok tanam? [y/t] : ")
    if input_tomat == "y" :
        file_tomat = open ("./project akhir huhu/tomat.txt", 'w')
        # "project akhir huhu" dapat diganti dengan tempat di mana folder file ini disimpan ^^
        print ("""
Baik, step yang bisa Anda lakukan adalah :\n
1. Siapkan bahan
2. Alat
               """)
        konten_tomat_1 = """
        Daily Tracker Day-1
        1. Menggunakan tanah pilihan
        2. Menyirami dengan sepenuh hati
        3. Direkam time-lapse
        """
        input_question_1 = input ("Apakah Anda sudah melakukannya sesuai instruksi? [y/t] : ")
        
        print (konten_tomat_1)
        file_tomat.write (konten_tomat_1)
        file_tomat.close () 
