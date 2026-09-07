def main():
	try:
		s = input()
	except EOFError:
		s = ""
	border = "*" * (len(s) + 4)
	middle = "* " + s + " *"
	print(border)
	print(middle)
	print(border)

if __name__ == '__main__':
	main()