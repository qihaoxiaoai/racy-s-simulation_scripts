#!/bin/sh
#for vasp qihaoxiaoai@gmail.com
awk '{if (NR<8)  print $0;
       else if (NR==8) {print "Selective Dynamics";print $0;}
       else if (NR>8) {if($3<0.2) printf("%.7f %.7f %.7f %s %s %s\n",$1,$2,$3,"F","F","F");
       else printf("%.7f %.7f %.7f %s %s %s\n",$1,$2,$3,"T","T","T");}}' POSCAR > POSCAR_new
