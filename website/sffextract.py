from Bio import SeqIO

def sfftofasta(inputfl,outputfl):
    records = SeqIO.parse(inputfl, "sff")
    count = SeqIO.write(records, outputfl, "fasta")
    print("Converted %i records" % count)
    return