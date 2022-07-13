import logging
logging.basicConfig(filename="test3.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE
class INEURON:
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


    def courses(self):
        try:
            logging.info("57 Courses")
        except Exception as e:
            logging.error(e)

    def blogs(self):
        try:
            logging.info("Designing,Digital Marketing")
        except Exception as e:
            logging.error(e)

    def internships(self):
        try:
            logging.info("Web Development,Virtual Reality")
        except Exception as e:
            logging.error(e)

    def job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class sub(INEURON):
    def classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def studentsinnumbers(self):
        try:
            logging.info("428 Students")
        except Exception as e:
            logging.error(e)


i = sub()
i.classtype()
i.studentsinnumbers()


#PRIVATE VARIABLE
class INEURON:
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

    def __job(self):
        try:
            logging.info("Data Analyst,Business Analyst")
        except Exception as e:
            logging.error(e)

class sub(INEURON):
    def __classtype(self):
        try:
            logging.info("FSDS MAY BATCH 2022")
        except Exception as e:
            logging.error(e)

    def __studentsinnumbers(self):
        try:
            logging.info("428 Students")
        except Exception as e:
            logging.error(e)

j = sub()
j._sub__classtype()
j._sub__studentsinnumbers()


