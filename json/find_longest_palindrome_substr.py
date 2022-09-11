class Solution():
	def __init__(self, string: str):
		self.string, self.len = string, len(string)
		self.store = [[None for i in range(self.len)] for j in range(self.len)]
	def findLPS(self, i : int, j : int) -> list:
		if i >= j:
			return [i] if i == j else []
		if self.store[i][j]:
			return self.store[i][j]
		
		match = self.string.index(self.string[j], i, j+1)
		if match == j:
			return self.findLPS(i, j-1)
		give = self.findLPS(i, j-1)
		take = self.findLPS(match+1, j-1) + [match, j]
		self.store[i][j] = take if len(take) > len(give) else give
		return self.store[i][j]
	def printLPS(self) -> None:
		trace = self.findLPS(0, self.len - 1)
		print("".join(self.string[i] for i in sorted(trace)))

if __name__ == '__main__':
	string = "character"
	sol = Solution(string)
	Solution.printLPS(sol)

# result: "carac"