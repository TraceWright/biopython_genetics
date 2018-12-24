from BioSQL import BioSeqDatabase
server = BioSeqDatabase.open_database(driver="MySQLdb", user="root",
                     passwd = "FurtherFlowersVenus", host = "localhost", db="bioseqdb")
db = server["just_testing"]
print("This database contains %i records" % len(db))
for key, record in db.items():
    print("Key %r maps to a sequence record with id %s" % (key, record.id))
