Tautan Aplikasi Adaptable: https://tugas2-pbp-nazwa.adaptable.app

<PERTANYAAN dan JAWABAN>
...
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas    secara step-by-step (bukan hanya sekadar mengikuti tutorial).
=========
(JAWABAN)
- Membuat direktori baru yang bernama tugas2_pbp. setelah itu melakukan inisiasi direktorinya menjadi repository kosong. Lalu saya menghubungkan repository github dengan repository lokal yang ada di komputer saya.
- Untuk keperluan instalasi django, saya membuat repository baru pada github dengan nama pbp_nazwa. Setelahnya saya menyiapkan properti seperti mengaktifkan environment dan juga menyiapkan dependencies 
- Selanjutnya, saya melakukan konfigurasi pada settings.py untuk deployment di adaptable. 
- Pada repository tugas2_pbp, saya menambahkan file .gitignore dan saya melakukan commit serta push ke repository github, setelahnya saya melakukan deployment pada adaptable. 
- Pada repository tugas2_pbp, saya membuat aplikasi main, selanjutnya agar aplikasi dapat beroperasi, pada menu settings.py, saya mendaftarkan main ke ALLOWED HOST, setelah itu, pada main, saya menambahkan direktori baru 'templates' yang berisi file main.html, gunanya untuk menampilkan hasil eksekusi kode ke peramban. 
- Selanjutnya saya melakukan pembaruan pada file models.py untuk item yang akan dieksekusi dengan atribut nama, jumlah item, dan deskripsinya. untuk mengetahui bahwa terjadi modifikasi pada model, dilakukan migrasi model. 
- Selanjutnya, saya membuat fungsi di views.py dengan komponen nama aplikasi serta identitas diri saya. Setelah membuat fungsi, saya melakukan sedikit modifikasi pada main.html di direktori 'template' pada aplikasi main. Saya menghubungkan context yang ada pada views.py ke main.html
- Langkah finishing, saya melakukan unit testing dan juga routing. Routing ini semacam pemetaan pada direktori tugas2_pbp yang nantinya akan dieksekusi pada aplikasi main dan dicetak pada peramban. 
...

...
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
=========
(JAWABAN)
![BAGAN](bagan/File-Bagan-Request-Client-Nazwa.jpg)





...
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
=========
(JAWABAN)
Virtual environment digunakan karena berfungsi untuk mengisolasi package dan depedencies dari aplikasi sehingga tidak bertabrakan dengan versi lain yang ada pada komputer lokal kita. Kita tetap bisa membuat aplikasi web berbasis django tanpa menggunakan virtual environment, namun itu bukan best practice dan juga rentan terjadinya konflik package dan dependenciesnya. 
...

...
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
=========
(JAWABAN)
