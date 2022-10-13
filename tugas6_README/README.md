**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**
Synchronous programming merupakan jenis programming untuk  sistem atau aplikasi yang tidak bisa dilakukan proses lain selama programnya berjalan. 
sehingga metode pemanggilan function atau request yang hanya bisa dilakukan satu-satu (synchronous). 
Sedangkan asynchronous programming adalah suautu jenis program yang dapat berjalan sekaligus selama website tersebut loading sehingga sistem bisa melakukan 
multitasking atau melakukan banyak proses sekaligus.


**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming.
Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**
Event-driven programming adalah model program yang bergantung pada 'event' yang terjadi pada sistem.
Event yang dimaksudkan adalah button click, key press, dsb. 


**Jelaskan penerapan asynchronous programming pada AJAX.**
AJAX (Asynchronous JavaScript And XML) digunakan untuk mengubah tampilan html tanpa harus website atau aplikasi melakukan refresh. AJAX dapat membuat HTTP GET dan POST.
sehingga program tidak perlu melakukan refresh dalam menerapkan data.


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
- membuat path yang mengarah ke view yang me-return json tasks  user. 
- membuat path baru (/todolist/ajax) dalam  membuat ajax GET request. 
- Saya membuat file .js yang direfers oleh file todolist_ajax.html lalu mulai membuat function js yang bisa mengembalikan data dari json, 
- membuat POST request untuk mensubmit data di form modal. 


