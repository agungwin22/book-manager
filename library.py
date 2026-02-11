class Library:
	def __init__(self, name="Perpustakaanku"):
		self.name = name
		self.books = []	# List kosong untuk simpan object book

	def add_book(self, book):
		"""tambah buku ke rak"""
		self.books.append(book)
		print(f"✓ buku {book} ditambahkan")

	def list_book(self):
		"""Tampilkan semua buku"""
		if not self.books:
			print("Rak Kosong!")
			return 

		print(f"\n=== {self.name} ===")
		for idx, book in enumerate(self.books, 1):
			print(f"{idx}. {book}")

	def search_by_title(self, keyword):
		"""Cari buku berdasarkan judul"""
		results = [
			book for book in self.books
			if keyword.lower() in book.title.lower()
		]

	def borrow_book(self, index):
		"""Pinjam buku berdasarkan no urut"""
		try:
			book = self.books[index, 1]
			if book.borrow():
				print(f"✓ Berhasil meminjam '{book.title}'")
			else:
				print(f"✗ '{book.title}' sedang dipinjam")
		except IndexError:
			print("Nomor buku tidak valid!")