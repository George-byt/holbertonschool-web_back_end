#!/usr/bin/env python3
""" Python file about 0x05. Personal data project """
from typing import List
import re
import logging
import mysql.connector
from os import getenv

# Tuple PII_FIELDS that contains the fields
# from user_data.csv that are considered PII
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format method to class

        Arguments:
        => record: (logging.LogRecord)

        Returns:
        => str
        """
        msg = filter_datum(self.fields, self.REDACTION,
                           super().format(record), self.SEPARATOR)
        return msg


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    Arguments:
    => fields: A list of strings representing all fields to abfuscate
    => redaction: A string representing by what the field will be obfuscated
    => message: A string representing the log line
    => separator: A string representing by which character is separating all
    fields in the log line (message)
    """
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """
    get_logger implementation
    Return: logging.Logger
    """
    # crate logger with the name "user_data"
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # create console handler and set level to debug
    ch = logging.StreamHandler()

    # add formatter to ch
    ch.setFormatter(RedactingFormatter(PII_FIELDS))

    # add ch to logger
    logger.addHandler(ch)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    get_db() implementation
    Return: A connector to the database
    (mysql.connector.connection.MySQLConnection object)
    """
    db = mysql.connector.connection.MySQLConnection(
        host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=getenv('PERSONAL_DATA_DB_NAME'),
        user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=getenv('PERSONAL_DATA_DB_PASSWORD', '')
    )
    return db


def main():
    """
    main() implementation that returns nothing
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    result = cursor.fetchall()
    for data in result:
        message = f"name={data[0]}; " + \
                  f"email={data[1]}; " + \
                  f"phone={data[2]}; " + \
                  f"ssn={data[3]}; " + \
                  f"password={data[4]}; " + \
                  f"ip={data[5]}; " + \
                  f"last_login={data[6]}; " + \
                  f"user_agent={data[7]};"
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
