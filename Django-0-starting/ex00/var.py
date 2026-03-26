def my_var():
	vars = [
		int(42),
		"42",
		"quarante-deux",
		float(42),
		True,
		[42],
		{42:42},
		(42,),
		set()
		]
	for var in vars:
		print(f"{var} has a type {type(var)}")

if __name__ == "__main__":
	my_var()
