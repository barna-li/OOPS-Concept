import logging
logging.basicConfig(filename="test5.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE
class one:
    def classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def studentsinnumbers(self):
        try:
            logging.info("300 Students")
        except Exception as e:
            logging.error(e)


class two:
    def courses(self):
        try:
            logging.info("57 Courses")
        except Exception as e:
            logging.error(e)

    def internships(self):
        try:
            logging.info("Web Development,Virtual Reality")
        except Exception as e:
            logging.error(e)


class three:
    def job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class four(one,two,three):
    pass

i = four()
i.job()
i.internships()
i.courses()
i.studentsinnumbers()
i.classtype()



#PRIVATE VARIABLE
class one:
    def __classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def __studentsinnumbers(self):
        try:
            logging.info("300 Students")
        except Exception as e:
            logging.error(e)


class two:
    def __courses(self):
        try:
            logging.info("57 Courses")
        except Exception as e:
            logging.error(e)

    def __internships(self):
        try:
            logging.info("Web Development,Virtual Reality")
        except Exception as e:
            logging.error(e)


class three:
    def __job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class four(one,two,three):
    pass

i = four()
i._three__job()
i._two__internships()
i._two__courses()
i._one__studentsinnumbers()
i._one__classtype()

