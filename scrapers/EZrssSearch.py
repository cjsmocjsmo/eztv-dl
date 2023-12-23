import sqlite3




















if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="A simple CLI program")
	parser.add_argument("--catagory", "-c", help="TV or Movie")
	parser.add_argument("--term", "-t", help="Text to search for")
	parser.add_argument("--season", "-s", help="Season to search for")
	parser.add_argument("--default", "-d", help="Scan default list yes or no")
	args = parser.parse_args()

	main(args)






