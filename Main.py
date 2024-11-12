
from Module.PyTrana import read_fasta, Transcription_DNA, Translation_DNA


FastaFile = "sequence.fasta"

myseqs = read_fasta(FastaFile)
dnaTranscripte = Transcription_DNA(myseqs)
dnatranslate = Translation_DNA(dnaTranscripte)
print(dnatranslate)


