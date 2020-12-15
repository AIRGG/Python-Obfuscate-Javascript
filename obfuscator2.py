import subprocess, re, os, time, sys
from bs4 import BeautifulSoup
from datetime import datetime

mode = 0
# 1 = Lanjut
# 0 = Replace Ulang

def main():
	for y in os.listdir("convert"):
		dirfile = f"convert\\{y}"
		diroutfile = f"convert\\output\\{y}"
		if os.path.isdir(dirfile): continue
		if mode == 1:
				if y in os.listdir("convert\\output\\"): continue
		with open(dirfile) as fl:
			txt = re.sub(r"\{\#.*\#\}", "", fl.read())
			with open("tmphtml", "w") as fw: fw.write(txt)
			html = BeautifulSoup(txt, "html.parser")
			script = html.find_all("script")
			# script = [script[1]]
			no = 0
			for x in script:
				if x.has_attr('src'): continue
				no += 1
				with open(f"tmpfile", "w") as fwtmp: fwtmp.write(x.text)
				output = subprocess.check_output(['node', 'obfuscatenya.js'])
				tmptxt = ""
				with open(f"tmphtml") as fwtmp: tmptxt = fwtmp.read()
				with open(f"tmphtml", "w") as fwtmp: fwtmp.write(tmptxt.replace(x.text, output.decode('utf-8')))
				tmptxt = ""
			with open(diroutfile, "w") as fwtmp:
				with open(f"tmphtml") as fread:
					fwtmp.write(fread.read())
			print(f"[DONE]: {y}")		


awal = time.time()
print(f"--- Start at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
try:	
	if __name__ == "__main__":
		main()
except Exception as ex:
	print(f"Something WRONG: {ex}")
finally:
	try:
		os.remove("tmphtml")
		os.remove("tmpfile")
	except Exception as e:
		print("Lewat")
	akhir = time.time() - awal
	print("\n--- Complete in %s seconds ---" % (time.time() - awal))