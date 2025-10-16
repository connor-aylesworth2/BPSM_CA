#!/usr/bin/bash

rm -f *.exercise.out
goodlines=$(grep -v "#" ${BLASToutput} | wc -l | cut -d ' ' -f1)
unset IFS
unset dataline
#shortHSP=0;
#hspcounter=0;
echo -e "We have ${goodlines} data lines for processing... \n"

#dupS_acc=()

#group1cut=100
#group2cut=200
#group3cut=300
#outfile1="HSPscore.${group1cut}.exercise.out"
#outfile2="HSPscore.${group2cut}.exercise.out"
#outfile3="HSPscore.${group3cut}.exercise.out"
#outfile4="HSPscore.morethan.${group3cut}.exercise.out"

#rm -f ${outfile1} ${outfile2} ${outfile3} ${outfile4}

while read wholeline
do
        #echo "Line: ${wholeline}"
        if test "${wholeline:0:1}" != "#"
                then
                dataline=$((dataline+1))
                #echo "Line ${dataline} starts with ${wholeline:0:1}"
                read Q_acc S_acc pc_identity alignment_length mismatches gap_opens Qstart Q_end S_start S_end evalue bitscore <<< ${wholeline}
		bitscore=$(printf "%.0f\n" ${bitscore})


#1) list the subject accession for all HSPs
                echo -e "${dataline}\t${Q_acc}\t${S_acc}" >> Subject_accessions.exercise.out

#2) list the alignment length and percent IDs for all HSPs
		echo -e "${dataline}\t${alignment_length}\t${pc_identity}" >> alignments.exercise.out

#3) show the HSPs with more than 20 mismatches
		if test "${mismatches}" -ge 20
		then
			echo -e "${wholeline}" >> 20plus_mismatches.exercise.out
		fi

#4) show the HSPs shorter than 100 amino acids and with more than 20 mismatches
		if test "${mismatches}" -ge 20 && test "${alignment_length}" -lt 100
		then
			echo -e "${wholeline}" >> not100_aa.exercise.out
		fi

#if test ${dataline} -eq ${goodlines}
#then
#        echo -e "\n\nENDBLOCK\n\nThere were ${shortHSP} HSPs shorter than 100 amino acids"
#        echo -e "There were ${#dupS_acc[@]} Subjects with multiple HSPs"
#fi
	fi
done < ${BLASToutput}
