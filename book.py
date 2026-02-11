class Book: # membuat blueprint
	def __init__(self, title, author, year):
		self.title = title
		self.author = author
		self.year = year
		self.is_available = True # Statis True = bisa dipinjam

	def __str__(self):
		"""Cara buku 'ditampilkan' saat di print"""
		status = "✓ Tersedia" if self.is_available else "✗ Dipinjam"
		return f"[{self.year}] {self.title} oleh {self.author} | {status}" 

	def borrow(self):
		"""Pinjam buku"""
		if self.is_available:
			self.is_available = False
			return True

	def return_book(self):
		self.is_available = True