#! /bin/bash 

#Variables
FASTA=raw.piwi.fas #only varibale to edit, just replace with main file
AA=piwi.aa.fas
ALN=piwi.aa.aln.fas
PHY=piwi.aa.aln.phy

#Alignment
translate.py $FASTA > $AA
linsi --thread 10 $AA > $ALN

## IQTREE STUFF ##

echo "starting iqtree..."
sleep 10

#If the directory iqtree doesn't exist, make it
if [ ! -d iqtree ]
  then mkdir iqtree
fi 

cp $ALN iqtree/
cd iqtree

#going to build 10 iqtrees simultaneously
seq 10 |parallel "iqtree2 -s piwi.aa.aln.fas -m JTT+R7 -T 6 -B 1000 -alrt 1000 --prefix tree{}"

cat *treefile > allTrees.nwk

#compare 10 trees, find the best of the 10
iqtree2 -s $ALN -z allTrees.nwk -m JTT+R7 --prefix bestTree -T 8

cd ../

echo "finished iqtree!"
sleep 5
echo "starting exaBayes..."
sleep 5

## ExaBayes stuff ##

#ExaBayes takes a long time, sometimes 12 hours

#If the directory exab doesn't exist, make it
if [ ! -d exab ]
 then mkdir exab
fi

#convert fasta to phylip
fas2phy.py $ALN > exab/$PHY

cd exab

#script must be in your BIOL435
makeConfig.py

#exabayes lines you haven't seen yet
mpirun -np 16 exabayes -m PROT -f $PHY -n myRun -s $RANDOM -c config.nex -R 4

consense -f ExaBayes_topologies.run-* -n myTree

echo "finshed exabayes!"
