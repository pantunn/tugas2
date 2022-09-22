**Jelaskan perbedaan antara JSON, XML, dan HTML!**

JSON (JavaScript Object Notation) merupakan format yang digunakan untuk menyimpan, membaca, dan menukar data agar bisa dibaca oleh user. Format dari file JSON adalah .json. JSON tidak mempunyai tag yang tidak terpakai sehingga, jika dibandingkan JSON lebih sederhana dan cepat dibandingkan dengan XML. 
XML (Extensive Markup Language) adalah suatu markup language yang dibuat untuk menyimpan dan mebawa serta mengantarkan data. Sebenarnya XML memiliki fungsi yang mirip akan tetapi JSON dan XML sangat berbeda. format file dari XML diakhiri dengan .xml. Perbedaan yang sangat jelas adalah XML lebih rumit karena memerlukan ukuran file yang besar. JSON biasanya digunakan untuk mengirim data dengan menguraikan data tersebut terlebih dahulu,  lalu kemudian dikirim ke internet. Sedangkan XML mempunyai data yang lebih terstruktur. HTML (Hypertext Markup Language) adalah suatu bahasa markup standar yang digunakan untuk membuat serta  menyusun halaman dan aplikasi web.

**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery digunakan untuk menghantarkan reqeust dari user yang nantinya digunakan sebagai untuk meminta data dari suatu database dan menghantarkan kembali kepada user dengan cepat dan aman.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas?**
1. Pertama-tama membuat aplikasi baru bernama mywatchlist, saya membuatnya melalui vscode
2. menambahkan path mywatchlist pada file urls.py
3. membuat model MyWatchList dengan mengisi file models.py dengan atribut watched, title, rating, release_date, dan review
4. menambah 10 data dengan membuat file initial_mywatchlist_data.json pada folder fixtures
5. membuat penyajian data dalam 3 format: HTML, XML, JSON
6. melakukan routing data sehingga ketiga format dapat diakses
7. melakukan git push ke github
8. melakukan deployment ke Heroku 

**Screenshot Postman**
XML

![image](https://user-images.githubusercontent.com/92297505/191659875-b7e8f74e-9c7f-4f93-84b7-349d338aa092.png)

JSON

![image](https://user-images.githubusercontent.com/92297505/191660006-c586c6da-464e-40ee-819b-09e615056730.png)

HTML

![image](https://user-images.githubusercontent.com/92297505/191660057-3a2b8b18-b0dd-4408-9765-d91502ba34cb.png)



