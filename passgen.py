# A random password generator

import logging, random

logging.basicConfig(level = logging.DEBUG, filename = "passgen.log", filemode = "w",
    format = "%(asctime)s --> %(levelname)s --> %(message)s")

uppercase: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase: str = uppercase.lower()
numbers: int = 1234567890
symbols: str = "!£$%^&*-+@#~<>?/.,"
    
combine = uppercase + lowercase + str(numbers) + symbols
length_of_string: str = input("Write your recommended length of password: ")

if __name__ == "__main__":
    password = "".join(random.sample(combine, int(length_of_string)))
    logging.info(f'Your password is: {password}')
    
