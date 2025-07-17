import sys
import logging 

def error_message_detail(error: Exception, error_detail: sys):
    ''' 
    Extracts detailed error information including the file name, line number and the error message where the error occurred.
    :param error: The exception object containing the error details.
    :param error_detail: The sys module to access the traceback information.
    :return: A formatted string containing the file name, line number, and error message.
    '''
    # Extract traceback details (exception information)
    _, _, exec_tb = error_detail.exc_info()
    
    # Get the file name and line number where the error occurred
    file_name = exec_tb.tb_frame.f_code.co_filename
    
    # Create a formatted error message string with file name, line number, and error message
    error_message = f"Error occurred in script: [{file_name}] at line number: [{exec_tb.tb_lineno}] with error message: [{str(error)}]"
    
    # Log the error message
    logging.error(error_message)
    
    return error_message

class MyException(Exception):
    '''
    Custom exception class that inherits from the built-in Exception class.
    It is used to raise exceptions with detailed error messages.
    '''
    
    def __init__(self, error_message: str, error_detail: sys):
        '''
        Initializes the MyException class with an error message and error details.
        :param error_message: The error message to be displayed.
        :param error_detail: The sys module to access the traceback information.
        '''
        # Call the base class constructor with the error message
        super().__init__(error_message)
        
        # Format the error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)
    
    def __str__(self):
        '''
        Returns the string representation of the error message.
        '''
        return self.error_message