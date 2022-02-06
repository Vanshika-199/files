files=open("question3.txt","r")
open1=open("delhi.txt","w")
open2=open("shimla.txt","w")
open3=open("others.txt","w")
files2=files.read()
files3=files2.split("\n")
i=0
while i<len(files3):
    if "delhi" in files3[i]:
        open1.write(files3[i])
        open1.write("\n")
    elif "shimla" in files3[i]:
        open2.write(files3[i])
        open2.write("\n")
    else:
        open3.write(files3[i])
        open3.write("\n")
    i=i+1
files.close()