def binery_search(kumpulan, target) :
    kiri = 0
    kanan = len(kumpulan) - 1

    while kiri <= kanan :
        tengah = (kiri + kanan) // 2

        if kumpulan[tengah] == target :
            return tengah

        elif kumpulan[tengah] < target :
            kiri = tengah + 1

        else :
            kanan = tengah - 1

    return -1

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

"""
Untuk mencari berapa tabakan yang digunakan Binary Search, menggunakan Logaritma basis 2 (Log2(n))
misal :
    - apabila terdapat element array berjumlah 100 maka akan memilki maksimal 7 kali tebakan.
      perhitungannya log2(100) = 6.643856189774725 kita tambahkan 1 menjadi 7.643856189774725 sehingga kita bulatkan ke bawah menjadi 7
      selain itu 7 didapatkan dari log2(128) = 7, dimana 100 paling mendekati dengan 128.

    - apabila itu terdapat 1000 element maka perhitungan akan sama.
      log2(1000) = 9.965784284662087 kita tambahkan 1 menjadi 10.965784284662087 dibulatkan ke bawah menjadi 10.
      bisa didapat dari log2(1024) = 10, dimana 1000 paling mendekati 1024.
"""
