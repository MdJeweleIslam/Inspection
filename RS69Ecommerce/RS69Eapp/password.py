import hashlib

def PassWord(rawdata):
	Spass = hashlib.sha256(str(rawdata).encode("utf-8")).hexdigest()
	Mpass = hashlib.md5(str(Spass).encode("utf-8")).hexdigest()
	return Mpass