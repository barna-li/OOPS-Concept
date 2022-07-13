import logging
logging.basicConfig(filename="test4.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE
class first:
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



class second(first):
    def job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class third(second):
    pass

i = third()
i.job()
i.internships()
i.courses()
i.studentsinnumbers()
i.classtype()

#PRIVATE VARIABLE

class first:
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



class second(first):
    def __job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class third(second):
    pass

i = third()
i._second__job()
i._first__internships()
i._first__courses()
i._first__studentsinnumbers()
i._first__classtype()

