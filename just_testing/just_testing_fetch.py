from Bio import Entrez
Entrez.email = 'traceylouisewright@hotmail.com'
from Bio import SeqIO
from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root",
                     passwd = "FurtherFlowersVenus", host = "localhost", db="bioseqdb")
db = server["just_testing"]
handle = Entrez.efetch(db="nuccore", id="6273291,6273290,6273289", rettype="gb", 
retmode="text")
count = db.load(SeqIO.parse(handle, "genbank"))
print("Loaded %i records" % count)
server.commit() #On Biopython 1.49 or older, server.adaptor.commit()
