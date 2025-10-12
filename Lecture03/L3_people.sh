#!/bin/bash
#Exercises from L3

#1
#counts how many people are in the people tsv.

x1=$(grep -v "name" /localdisk/data/BPSM/Lecture03/example_people_data.tsv|
awk 'BEGIN{FS="\t";}
{
	if($1 != "")
	{print $1;}
}'|
wc -l)

echo -e "#1 There are " ${x1} "people in the example_people_data.tsv file."



#2
#checks if field 6 (DOB) is less than or equal to 1995 and counts them.

x2=$(
cat /localdisk/data/BPSM/Lecture03/example_people_data.tsv|
    awk 'BEGIN{FS="\t";}
	{
		if($6 <= 1995)
		{print $0;}
	}'|
      wc -l)

echo -e "#2 "${x2}" of them are 30 years old or older."



#3
#checks if the first field (name) of the people tsv is exactly "Jan", and counts how many people have that name.

x3=$(cat /localdisk/data/BPSM/Lecture03/example_people_data.tsv|
    awk 'BEGIN{FS="\t";}{
	    if($1=="Jan")
	    {print $0;}
    }
    END{}'|
wc -l)

echo -e "#3 Of the "${x1}" people in the example_people_data.tsv file, "${x3}" of them is named Jan."



#4
#gives number of people from each country in people data (Mozambique)

#cat /localdisk/data/BPSM/Lecture03/example_people_data.tsv|
#    awk 'BEGIN{FS="\t"}
#    {print $7}'|
#	   sort|
#	   uniq -c|
#	   sort -n 
    
#takes all people from mozambique and finds those of that list that are 50yo or older

x4=$(awk 'BEGIN{FS="\t"}{
if($7=="Mozambique" && $6 <= 1975)
	{print $0}}' /localdisk/data/BPSM/Lecture03/example_people_data.tsv|wc -l)

echo -e "#4 Of the "${x1}" people in the example_people_data.tsv file, the most common country of origin is Mozambique. Of those from Mozambique, "${x4}" of them is 50yo or older."



#5
#Get lines of people who's emails end in edu
#sort those lines based on field 7, their country of origin
#list said sorted lines in reverse order relative to field 1, their names
#
