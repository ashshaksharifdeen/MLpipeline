import sys
#sys.path.insert(0, 'D:/Ashshak/ML practice/MLpipeline/src')
import logging
def error_mesage_detail(error,error_detail:sys):
   #this function will give all the information about which line, while the execption has occured
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name[{0}] line number [{1}] error message[{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message

class CustomException(Exception):
      def __init__(self, error_message,error_detail:sys):
           super().__init__(error_message)
           self.error_message = error_mesage_detail(error_message,error_detail=error_detail)

      def __str__(self):
           #this will print the error message
           return self.error_message
      
    