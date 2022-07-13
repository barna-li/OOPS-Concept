import logging
logging.basicConfig(filename="test1.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE

class ineuron:
    noofstudents = 300
    classtype= "DATA SCIENCE-DATA ABSTRACTION CLASS"

    def students(self):
        try:
            logging.info(ineuron.noofstudents)
            logging.info(ineuron.classtype)
        except Exception as e:
            logging.critical("this is a situation for us")
            logging.error(e)


i = ineuron()
i.students()

#PRIVATE VARIABLE

class ineuron:
    __noofstudents= 300
    __classtype= "DATA SCIENCE-DATA ABSTRACTION CLASS"

    def students(self):
        try:
            logging.info(ineuron.__noofstudents)
            logging.info(ineuron.__classtype)
        except Exception as e:
            logging.critical("this is a situation for us")
            logging.error(e)


i = ineuron()
i.students()

