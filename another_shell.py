import Practice

while True:
	fn = input('> ')
	if fn.strip() == "": continue


	try:
		with open(fn, "r") as f:
			script = f.read()
	except Exception as e:
		print("failed to load goes brrr")

	result, error = Practice.run('<stdin>', script)

	# result = ''.join(str(i) for i in result)
	if error:
		print(error.as_string())
	elif result:
		print(f'{result}')
