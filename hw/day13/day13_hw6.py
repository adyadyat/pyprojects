def converter():
	lght=int(input())
	cha=input()
	ch=["m","mm","ft","in","km","mi","nm"]
	m=[1,1000,3.28,39.37,0.001,0.000621,0.000540]
	mm=[0.001,1,0.0033,0.039370,0.000001,0.000000621,0.000000540]
	ft=[0.3048,305,1,12,0.000305,0.000189394,0.000164579]
	inch=[0.0254,25.4,0.0833,1,0.000025,0.000015783,0.000013715]
	km=[1000,1000000,3281,39370,1,0.621,0.540]
	mi=[1609,1609344,5280,63360,1.609,1,0.869]
	nm=[1852,1851999,6076,72913,1.852,1.151,1]
	lght1=["metr","millimetr","fut","inch","kilometr","mile","sea mile"]
	res=0
	if cha in ch:
		if cha=="m":
			for i in m:
				res=lght*i
				print(res)
				#print(" - ",end="")
		if cha=="mm":
			for i in mm:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		if cha=="ft":
			for i in ft:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		if cha=="in":
			for i in inch:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		if cha=="km":
			for i in km:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		if cha=="mi":
			for i in mi:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		if cha=="nm":
			for i in nm:
				res=lght*i
				print(res,end="")
				print(" - ",end="")
		print()
converter()