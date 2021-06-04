#! /usr/bin/env python

#parameters for ExaBayes
out = open('config.nex', 'w')

out.write('#NEXUS\n\n\
begin params;\n\
 stateFreq = (0)\n\
end;\n\n\
begin run;\n\
 numruns 4\n\
 numGen 1000000\n\
 samplingFreq 500\n\
 checkPointInterval 1000\n\
 sdsfConvergence 0.01\n\
 burninProportion 0.25\n\
 parsimonyStart  true\n\
 printFreq 100\n\
end;\n\n\
begin priors;\n\
 aaPr disc(JTT=1)\n\
end;\n')
out.close()

