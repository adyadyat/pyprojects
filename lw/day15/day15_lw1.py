def reva(text):
	r=""
	d=len(text)
	if d==1:
		return text
	else:
		t=text[d-1:d]
		r2=t+reva(text[0:d-1])
		return r2
print(reva("askar"))