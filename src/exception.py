import os, sys

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)

        self.error_message = error_message

        _,_,exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self) -> str:
        return (
            f"Error occured in python script"
            f"[{self.file_name}]"
            f"at line [{self.line_number}]"
            f"error message [{self.error_message}]"
        )