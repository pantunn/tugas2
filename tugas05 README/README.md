 **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
 1. inline
 kode Inline CSS  dimasukkan secara langsung pada setiap atribut HTML. 
 sehingga setiap atribut memiliki style CSS yang berbeda tergantung yang akan dibutuhkan.
  kelebihan: lebih mudah dalam perbaikan atribut HTML
             Membantu saat pengujian/testing.
             loading pada website lebih cepat dan HTTP request lebih kecil.
  kekurangan: Kurang efisien untuk penggunaan karena hanya bisa digunakan pada satu atribut saja.
              Kurang efisien untuk digunakanan dengan coding dengan baris yang banyak
 2. Internal
 kode CSS yang ditaruh dalam tag <style> dan sehingga lokasinya ada bagian header file HTML. 
 internal biasanya digunakan untuk membuat custom khusus pada satu halaman website agar halaman lain tidak terganggu/terpengaruh.
  kelebihan: lebih mudah untuk dilakukan editing tiap halaman website
             tidak perlu untuk mengupload file CSS karena sudah masuk dalam file HTML
             maintanance lebih mudah
  kekurangan: tidak efisien digunakan apabila digunakan untuk beberapa halaman website karena harus menuliskan ulang.
              Performa website menjadi lebih lambat karena adanya repetisi
              Ukuran file cenderung lebih besar
              
 3. Exernal
 kode CSS yang ditaruh pada file terpisah dengan file HTML. file CSS ditulis pada file dengan ekstensi .css. 
 Kelebihan: Ukuran file cenderung lebih kecil
            Penulisan kode HTML lebih rapi
            Loading  pada website lebih cepat
            bisa digunakan pada halaman website yang beda
 Kekurangan: kurang efisien pada website yang butuh halaman custom
             website bisa berantakan apabila CSS gagal load dengan sempurna

 **Jelaskan tag HTML5 yang kamu ketahui!**
 <style>	Tag yang digunakan membuat informasi style pada dokumen
 <div>	Tag yang digunakan membuat bagian dalam suatu dokumen
 <table>	Tag yang digunakan untuk membuat tabel
 <a>	Tag yang digunakan untuk membuat hyperlink
 <img>	Tag yang digunakan untuk membuat gambar
 
 Jelaskan tipe-tipe CSS selector yang kamu ketahui.
 1. Tag Selector
Tag ini menggunakan tag HTML untuk sebagai selectornya, misalnya jika ingin menggunakan tag HTML paragraf (<p>) pada HTML,
maka selectornya bisa ditulis dengan p
2. ID Selector
selector ini menggunakan atribut “id” pada element HTML sebagai selectornya. Apabila kita lihat penggunaan tag selector, 
maka tag yang dipilih semua tag dalam file HTML tersebut akan ikut berubah.
3. Class Selector
sistemnya hampir sama dengan ID selector, tetapi pada class selector  menggunakan atribut class.  
 
**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
-melakukan kustomisasi pada tugas 4 menggunakan CSS framework
-kustomisasi yang saya lakukan ada pada bagian login,register, todolist, dan my_todolist
-halaman website dibuat dengan responsive

