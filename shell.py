import CFPL

while True:
	fn = input('> ')
	if fn.strip() == "": continue
	try:
		with open(fn, "r") as f:
			script = f.read()
	except Exception as e:
		print("failed to load goes brrr")
	script = script.strip()
	result, error = CFPL.run('<stdin>', script)

	# result = ''.join(str(i) for i in result)
	if error:
		print(error.as_string())
	elif result:
		print(f'{result}')
