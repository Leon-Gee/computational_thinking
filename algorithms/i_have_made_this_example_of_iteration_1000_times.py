count = 0

while count < 10:
	print(count)
	count += 1

external_count = 0
internal_count = 0

while external_count < 5:
	while internal_count < 6:
		print(external_count)
		print(internal_count)
		internal_count += 1

		if internal_count >= 3:
			break

	external_count += 1
	internal_count = 0
