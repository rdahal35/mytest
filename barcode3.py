from pyzbar.pyzbar import decode
import PIL
from PIL import Image
import glob
import pandas as pd

barcode=[]

for filename in glob.glob("img/*.jpg"):
	y=decode(Image.open(filename))
	for x in y:
		z=(x[0])
		a=str(z)
		l=len(a)-1
		barcode.append(a[2:l])
barcode.sort()
print(barcode)
my_df=pd.DataFrame(barcode)
my_df.to_csv('barcode.csv',index=False, header='barcode')
