import logging
logging.basicConfig(filename="test2.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')

#PUBLIC VARIABLE

class Student:
    def __init__(self):
        self.courses = 30
        self.blogs = "Cloud computing"
        self.internships = "Machine Learning"
        self.job = "Python Developer"

    def stud(self):
        try:
            logging.info(self.courses)
            logging.info(self.blogs)
            logging.info(self.internships)
            logging.info(self.job)
        except Exception as e:
            logging.error(e)

i = Student()
i.stud()
i.courses =57
i.blogs ="Designing"
i.internships="Big Data"
i.job ="Data Analyst"
i.stud()              

#PRIVATE VARIABLE

class Student:
    def __init__(self):
        self.__courses = 30
        self.__blogs = "Cloud computing"
        self.__internships = "Machine Learning"
        self.__job = "Python Developer"

    def stud(self):
        try:
            logging.info(self.__courses)
            logging.info(self.__blogs)
            logging.info(self.__internships)
            logging.info(self.__job)
        except Exception as e:
            logging.critical("this is a situation for us")
            logging.error(e)

    def change(self,new_value1,new_value2,new_value3,new_value4):
        try:
            self.__courses = new_value1
            self.__blogs = new_value2
            self.__internships = new_value3
            self.__job = new_value4
        except Exception as e:
            logging.error(e)


j = Student()
j.stud()
j.change(57,"Designing","Big Data","Data Analyst")
j.stud()

