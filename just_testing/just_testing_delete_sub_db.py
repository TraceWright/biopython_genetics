from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root",
                     passwd = "FurtherFlowersVenus", host = "localhost", db="bioseqdb")
del server["just_testing"]
server.commit() #On Biopython 1.49 or older, server.adaptor.commit()
