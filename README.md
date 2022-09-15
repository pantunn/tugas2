
:grinning::grinning:

**LINK HEROKU APP**
https://pantun-katalog.herokuapp.com/katalog/



**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**
![Blank diagram](https://user-images.githubusercontent.com/92297505/190316319-0ce4c199-28f3-4e6d-b5c4-fc287afe25db.png)

urls.py digunakan untuk mengarahkan request dari HTTP ke views.py yang sesuai berdasarkan request URL. 
Pemeta URL juga dapat mencocokkan pola string atau angka tertentu yang muncul di URL dan meneruskannya 
ke fungsi tampilan sebagai data.

views.py berfungsi untuk mengendalikan request, yang menerima request dari HTTP dan mengembalikan respons ke HTTP. 
views.py mengakses data yang diperlukan untuk memenuhi permintaan melalui models.py, 
lalu diserahkan template.

models.py adalah objek Python yang menjelaskan struktur data aplikasi, 
serta menyediakan mekanisme untuk mengelola data dengan memodifikasinya dalam database.

berkas html adalah file teks yang menjelaskan struktur dari file (seperti halaman HTML), yang digunakan untuk mewakili isi konten yang aslinya. 
berkas html dapat dengan dinamis membuat halaman HTML menggunakan template HTML, dengan mengisinya dengan data dari model.py 

**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Virtual environment digunakan untuk mempersiapkan di mana enviroment untuk mengembangkan aplikasi dalam kasus ini adalah aplikasi web
Virtual environment  yang tidak memengaruhi libraries yang  dijalankan di mesin.  
kita dapat menggunakan pip untuk menginstali file requirements.txt. 
