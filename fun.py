def main():
	sum_three(3, 4, 5)
	avg_three(3, 4, 5)

def sum_three(v1, v2, v3):
	""" do something
	"""
	p = v1 + v2 + v3
	return p

def avg_three(v1, v2, v3):
	""" do more
	"""
	sum = sum_three(v1, v2, v3)
	print(sum)
	p =  sum / 3.0
	print(p)


if __name__ == "__main__":
	main()