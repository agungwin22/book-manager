from book import Book
from library import Library
import os

def main():

	lib = Library("CLI Book Manager")

	while True:

		os.system('clear')

		print("\n=== Menu ===")
		print("1. Tambah Buku")
		print("2. Lihat Semua Buku")
		print("3. Cari Buku")
		print("4. Pinjam Buku")

		choice = input("Pilih (1-5): ")

		if choice == '1':
			title = input("Title: ")
			author = input("Author: ")
			year = input("Tahun: ")
			book = Book(title, author, year)
			lib.add_book(book)

		elif choice == '2':
			lib.list_book()
		elif choice == '3':
			keyword = input("Cari Judul: ")
			result = lib.search_by_title(keyword)
			if result:
				for book in result:
					print(f" • {book}")
			else:
				print("Tidak ditemukan")
		elif choice == '4':
			lib.list_book()
			if lib.list_book():
				idx = int(input("Nomor buku untuk dipinjam: "))
				lib.borrow_book(idx)
		else:
			print("Pilihan tidak valid")

		isdone = input("\nLanjut? (y/n): ")

		if isdone == 'n':
			print("Sampai Jumpa")
			break

if __name__ == '__main__':
	main()