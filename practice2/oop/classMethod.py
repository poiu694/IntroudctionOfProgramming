class Info:
	length = 0
	message = ''

	def __init__(self, message = ''):
		self.message = message
		self.length = len(message)

	def __del__(self):
		print("#Info 인스턴스가 삭제되었습니다.")

	def __repr__(self):
		return f"#Info Message: {self.message}, length: {self.length}"

	def __add__(self, other):
		nextInfo = Info(self.message + other.message)
		return nextInfo

	def __lt__(self, other):
		return self.length < other.length

	def __eq__(self, other):
		return self.length == other.length

		
