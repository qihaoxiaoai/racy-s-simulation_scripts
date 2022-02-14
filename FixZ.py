#utf-8
#qihaoxiaoai@gmail.com
#z direction

fo = open("POSCAR_Fix",'w')
fC = open("POSCAR")
line_total = 0
j=0
k=0
for i in range (1,10):
	linefc = fC.readline()
	fo.write( linefc )

minimum = float(input("minimum input:"))
maximum = float(input("maximum input:"))

line = fC.readline()
fC.seek(0)
while line: 
	line_total+=1
	line = fC.readline()

fC.seek(0) 
line2 = fC.readline()
fix  = " F F F \n"
move = " T T T \n"

while line2:
	if j>8: 	
		if float(line2.split()[2])<minimum or float(line2.split()[2])>maximum: 
			line2=line2.replace("T","")
			line2=line2.strip('\n')		
			line2+=fix
			fo.write( line2 )
			print (line2)
		else:
			line2=line2.replace("T","")
			line2=line2.strip('\n')		
			line2+=move
			fo.write( line2 )
			print (line2)
	j+=1
	line2 = fC.readline()

fC.close()

with open('POSCAR_NEW', 'r+') as fd:
    contents = fd.readlines()
    contents.insert(7, 'Selective Dynamics \n')  
    fd.seek(0)  
    fd.writelines(contents)
