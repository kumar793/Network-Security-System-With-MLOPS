import sys
from networksecurity.logging.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    logging.info("error message found")
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        logging.info("Exception occured")
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        logging.info("****Exception****")
        return self.error_message
    


        