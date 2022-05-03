wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for x in wardrobe:
	for y in wardrobe[x]:
		print("{} {}".format(y, x))