files=open("people1-exercise.txt","r")
i=0
for line in files:
    if line!="\n":
        i=i+1
files.close()
print(i,"is the total count")