import cv2

def tampilkan_citra(''):
    # Baca citra dari file
    citra = cv2.imread('apel 2.jpeg')

    # Pastikan citra berhasil dibaca
    if citra is not None:
        # Tampilkan citra
        cv2.imshow('Citra', citra)

        # Tunggu sampai pengguna menekan tombol keyboard
        cv2.waitKey(0)

        # Tutup jendela tampilan
        cv2.destroyAllWindows()
    else:
        print(f"Gagal membaca citra dari file {'Disney Princess, lily Z.jpg'}")

if __name__ == "__main__":
    nama_file_citra = 'Disney Princess, lily Z.jpg'  
    tampilkan_citra(nama_file_citra)
