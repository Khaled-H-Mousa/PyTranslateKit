
#FastaFile = "/home/khaled/Documents/Python_Tasks/sequence.fasta"
import os
import sys
import re


def read_fasta(FastaFile):
    seqs = {}
    with open(FastaFile) as MyFile:
        header = ""
        for line in MyFile:
            line = line.strip()
            #print(line)
            if line.startswith(">"):
                #print(line)
                header = line 
                header = header.replace(">","")
                header = " ".join(header.split(" ")[:3])
                seqs[header] = ""
            else:
                seqs[header] += line
    return seqs



def Transcription_DNA(seqs):
    DNA_Transcripte = {}
    for ID, seq in seqs.items():
        Seq_rna = seq.replace("T","U")
        DNA_Transcripte[ID] = Seq_rna
    return DNA_Transcripte



def Translation_DNA(DNA_Transcripte):
    DNA_Translate = {}
    # Define the codon to amino acid translation table
    table = {
              'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M', 
              'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 
              'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K', 
              'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
              'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 
              'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 
              'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q', 
              'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 
              'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 
              'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 
              'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E', 
              'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 
              'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 
              'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L', 
              'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_', 
              'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W'}

    for ID, seq in DNA_Transcripte.items():
        Protein = ""
        for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            Amino_Acid = table.get(codon, "")
            Protein += Amino_Acid
        DNA_Translate[ID] = Protein

    return DNA_Translate




