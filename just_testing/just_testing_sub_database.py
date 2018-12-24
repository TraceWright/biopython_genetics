from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root",
                     passwd = "FurtherFlowersVenus", host = "localhost", db="bioseqdb")
db = server.new_database("just_testing", description="Just for testing")
server.commit() #On Biopython 1.49 or older, server.adaptor.commit()
