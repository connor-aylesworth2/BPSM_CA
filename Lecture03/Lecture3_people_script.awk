#Exercises from L3

#1
x=$(
grep -v "name" /localdisk/data/BPSM/Lecture03/example_people_data.tsv|
awk 'BEGIN{FS="\t"}
{
	if($1 != $x)
	{print $1;}
}'|
wc -l)

echo -e "There are" ${x} "people in the example_people_data.tsv file."

