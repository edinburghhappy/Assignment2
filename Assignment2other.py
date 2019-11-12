#!/usr/bin/python3
fr=open('seq2.fasta','r')
fw=open('seq3.fasta','w')
seq={}
for line in fr:
	if line.startswith('>'):
		name=line.split()[0]
		seq[name]=''
	else:
		seq[name]+=line.replace('<n','')
fr.close()

for i in seq.keys():
	fw.write(i)
	fw.write('\n')
	fw.write(seq[i])
	fw.write('\n')
fr.close()

#some idea
'''
seq_contents=open("seq1.fasta").read().rstrip("\n")
seq_number=seq_contents.count('>')
print("We have obtained",seq_number,"sequences as required. Do you want to continue to analyze these sequences?")
user_choose1=input("Yes or No: ")
if user_choose1,upper()[0]=="Y" :
  if seq_number>250:
    clustalo -i seq1.fasta -o seq2.fasta --output-order tree-order  --maxnumseq 10000 --force -v
    
    
fr=open('test2.fasta', 'r')
fw=open('out.fasta', 'w')
seq={}
for line in fr:
    if line.startswith('>'):    #????????‘>??’
        name=line.split()[0]    #???????,?????0???
        seq[name]=''
    else:
        seq[name]+=line.replace('\n', '')
fr.close()                           

for i in seq.keys():
    fw.write(i)
    fw.write('\n')
    fw.write(seq[i])
    fw.write('\n')
fr.close()
##???????????????????seq?
#????????ID??,

for i in seq.keys():
    if i.startswith('>chr1|hos107.1'): #???????,??????ID????
        fw.write(i)
        fw.write('\n')
        fw.write(seq[i])
        fw.write('\n')
fr.close()
      
cons -sequence seq1.fasta -outseq cons.fasta
makeblastdb -in seq1.fasta -dbtype prot -out seq1
blastp -db seq1 -query cons.fasta -outfmt 7 > blastout1.out
grep -v "#" blastout1.out|\
sort -k3,3nr |\
grep -m10 "EM"|\
cut -f 2 > sort.out
plo_seq_Acc=open("sort.out").read().rstrip("\n")
plo_seq_Acc_list=plo_seq_Acc.split("\n")

for i in plo_seq_Acc_list:
  plo=open("plo.sh","w")
  plo.write("esearch -db protein -query "+"'"+i+"'| efetch -db protein -format fasta >> plo.fasta")
  plo.close()
  subprocess.call("chmod 700 plo.sh",shell=True)
  subprocess.call("./plo.sh",shell=True)
subprocess.call("plotcon -sequences plo.fasta -winsize 10 -graph svg",shell=True)
subprocess.call("display plotcon.svg")

subprocess.call("patmatmotifs -full -sequence seq1.fasta -outfile prosite.fasta -rstrandshow2",shell=True)


" seq_numbers "
subprocess.call("grep -c ">" seq1.fasta > seq_number.txt")
'''