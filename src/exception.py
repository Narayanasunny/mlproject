import sys  # Importing sys module to get system-related exception information
import logging

# Function to create a detailed error message
def error_message_detail(error, error_detail: sys):
    # exc_info() returns (type, value, traceback). We only need traceback here.
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Format the error message with filename, line number, and actual error message
    error_message = "Error occurred in script [{0}] at line number [{1}] with message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    # Return the formatted error message
    return error_message
    

# Custom Exception class that gives more detailed error messages
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Call the parent Exception class constructor to store the basic error message
        super().__init__(error_message)

        # Call the function to generate detailed error info and store it
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
        
    # This function returns the detailed error message when the exception is printed
    def __str__(self):
        return self.error_message

