from datetime import datetime

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from BioSQL import BioSeqDatabase

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Just_Testing(tornado.web.RequestHandler):
    def initialize(self, server):
        self.server = server

    def get(self):
        db = self.server["just_testing"]  
        self.write("This database contains %i records" % len(db))
        for key, record in db.items():
            self.write("Key %r maps to a sequence record with id %s" % (key, record.id))      


class Application(tornado.web.Application):
    def __init__(self):

        server = BioSeqDatabase.open_database(driver="MySQLdb", user="root",
            passwd = "FurtherFlowersVenus", host = "localhost", db="bioseqdb")

        handlers = [
            (r"/", MainHandler),
            (r"/just_testing", Just_Testing, {'server': server })
        ]

        settings = dict(
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
