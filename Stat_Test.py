import re
import glob 
#Use to get file names

#Read Key Files
with open("Red.txt", encoding="utf-8") as x:
    red= x.read().split('\n')
with open("Pink.txt", encoding="utf-8") as x:
    pink= x.read().split('\n')
with open("Blue.txt", encoding="utf-8") as x:
    blue= x.read().split('\n')
with open("Green.txt", encoding="utf-8") as x:
    green= x.read().split('\n')
with open("Yellow.txt", encoding="utf-8") as x:
    yellow= x.read().split('\n')

#Get File Names
files=[x for x in glob.glob("Tests/*.txt")]
res=[]
print(files)
for f in files:
    with open(f, encoding="utf-8") as x:
        print(f)
        text=x.read()
        text= re.sub("/", " ", text)
        text= re.sub("  ", " ", text)
        print(text)
        r=0
        p=0
        b=0
        g=0
        y=0
        for i in red:
            if i in text:
                r+=1
        print(str(r))
        for i in pink:
            if i in text:
                p+=1
        print(str(p))
        for i in blue:
            if i in text:
                b+=1
        print(str(b))
        for i in green:
            if i in text:
                g+=1
        print(str(g))
        for i in yellow:
            if i in text:
                y+=1
        print(str(y))
        data= "File: " + f + " Red: " + str(r)+" Pink: " + str(p) + " Blue: " + str(b) + " Green: " + str(g) + " Yellow: " + str(y) + " บังคับ: " + str(r+p) + " ไม่บังคับ: " + str(b+g+y)
        res.append(data)
print(res)

with open("result.txt","w", encoding="utf-8") as result:
    for x in res:
        result.write(x)
        result.write("\n")