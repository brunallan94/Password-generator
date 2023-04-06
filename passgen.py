# A random password generator

import logging, random

logging.basicConfig(level = logging.DEBUG, filename = "passgen.log", filemode = "w"
    format = "%(asctime)s --> %(levelname)s --> %(message)s")

if __name__ == "__main__":
    uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase: str = uppercase.lower()
    numbers: int = 1234567890
    symbols: str = "!£$%^&*-+@#~<>?/.,"
    
    combine = uppercase + lowercase + str(numbers) + symbols
    length_of_string: int = 8
    
    password = "".join(random.sample(combine, length_of_string))
    logging.info(f'Your password is: {password}')
    
