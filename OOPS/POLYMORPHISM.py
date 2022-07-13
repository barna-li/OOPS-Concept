import logging
logging.basicConfig(filename="test6.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE
class one:
    def classtype(self):
        try:
            logging.info("FSDS NOV BATCH 2021")
        except Exception as e:
            logging.error(e)

    def studentsinnumbers(self):
        try:
            logging.info("300 Students")
        except Exception as e:
            logging.error(e)


class two:
    def classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def studentsinnumbers(self):
        try:
            logging.info("360 Students")
        except Exception as e:
            logging.error(e)

def external(a):   # its a bridge/connection between all the classes
    a.classtype()
    a.studentsinnumbers()

i = one()
j=  two()
external(i)
external(j)

#PRIVATE VARIABLE

class one:
    def __classtype(self):
        try:
            logging.info("FSDS NOV BATCH 2021")
        except Exception as e:
            logging.error(e)

    def __studentsinnumbers(self):
        try:
            logging.info("300 Students")
        except Exception as e:
            logging.error(e)


class two:
    def __classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def __studentsinnumbers(self):
        try:
            logging.info("360 Students")
        except Exception as e:
            logging.error(e)


def external(a,b):  # its a bridge/connection between all the classes
    a._one__classtype()
    a._one__studentsinnumbers()
    b._two__classtype()
    b._two__studentsinnumbers()


i = one()
j = two()
external(i,j)

