__author__ = 'longtian'

import pandas

BAV_only = pandas.read_csv("BAV3810.csv")

transcript = pandas.read_csv("transcript.csv")

contig_transcript = [i.split(':')[0] for i in transcript['locus']] #Get the contig info from transcript form
start_transcript = [int(i.split(':')[1].split('-')[0]) for i in transcript['locus']] #Get start position
stop_transcript = [int(i.split(':')[1].split('-')[1]) for i in transcript['locus']] #And the end position

transcriptome = open('transcriptome_all.txt','w')
transcriptome.write('Contig_ID\tFunction\tStrand\tStart\tStop\tFPKM\n')
for i in range(len(BAV_only['contig_id'])):
    for j in range(len(contig_transcript)):
        if contig_transcript[j] == BAV_only['contig_id'][i]:
            if BAV_only['start'][i] >= start_transcript[j] and BAV_only['stop'][i] <= stop_transcript[j]:
                oneline='%s\t%s\t%s\t%s\t%s\t%s\n'%(BAV_only['contig_id'][i],BAV_only['function'][i],BAV_only['strand'][i],
                                                BAV_only['start'][i],BAV_only['stop'][i],transcript['FPKM'][j])
                transcriptome.write(oneline)
            else:
                continue
        else:
            continue

transcriptome.close()


