Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
% csrf_token %} digunakan untuk mencegah serangan Cross-site Request Forgery (CSRF) yang membuat penyerang mengirim permintaan palsu pada website yang sedang diakses sehingga penyerang dapat melakukan suautu tindakan yang tidak dikehendaki oleh pengguna aslinya.

Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, dengan menggunakan tag form yang diawali dengan <form> dan diakhiri </form> juga dengan menggunakan method yang menjelaskan isi data form, atribut method bisa menggunakan get atau post.
 
Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
dari HTML form, lalu data disimpan ke database dan akan muncul data yang telah disimpan di template HTML. Ketika user memberikan input data pada form HTML, data tersebut akan diterima oleh fungs-fungsi variabel. 
 
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
- Membuat aplikasi baru 'todolist'
-menambahkan path todolist agar bisa diakses http://localhost:8000/todolist
-membuat model task dengan atribut user, date, title, description
-membuat form dengan registrasi, login, dan logout
-Mmebuat routing pada urls.py
-melakukan deployment
-membuat dua akun dan 3 dummy data

 Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
<img width="960" alt="Untitled" src="https://user-images.githubusercontent.com/92297505/192968961-3c1160a9-a5f2-493a-90f9-441575463f16.png">
<img width="960" alt="ddf" src="https://user-images.githubusercontent.com/92297505/192969772-2d476335-7a48-4c08-a83a-8b02989c50a9.png">

