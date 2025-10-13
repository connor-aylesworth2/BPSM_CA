!#/bin/bash

#for animal in cat dog llama
#do 
#	echo ${animal}
#done



#for number in {1..4} ; do echo -e "${number}\t${animal}"; done



#for number in {0..20..5}
#do
#echo -e "${number}\t${animal}"
#done



#for ((i = 0 ; i <= 50 ; i+=5)); do
#echo -e "${i}\t${animal}"
#done



#for number in {1..4} ; 
#do
#for anumal in cat dog llama
#do
#echo -e "${number}\t${animal}"
#done
#done



#for number in {1..4} ; do for animal in cat dog llama; do echo -e "${number}\t${animal}";done;done

unset count
for number in {1..4} ;
do
	for animal in cat dog llama
	do
		count=$((count+1))
		echo -e "${count}\t${number}\t${animal}"
	done
done
