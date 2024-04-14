'''
    This file is for implementing database functions and commands
'''

import psycopg2
import hashlib
import streamlit as st
   
def fetch_single_data(query: str)->tuple:
    """This method fetch the data from database\n
    Args:
        query: Sql query\n
    Returns:
        It returns the data from database in form of tuple
    """
    try:
        #establishing connection to the database
        connection = psycopg2.connect(
            dbname="try",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        
        #creating a cursor to execute SQL queries
        cursor = connection.cursor()
        
        #fetching scores from the database
        cursor.execute(query)
        result = cursor.fetchone()
        return result
    except (Exception,psycopg2.DatabaseError) as error:
        # Error occurred while connecting or querying the database
        msg=f'Database error: {error}'
        return msg
    finally:
        if connection is not None:
            cursor.close()
            connection.close()

def hash_password(password: str):
    """This method is used to generate hashed password\n
    Args:
        password: User's password\n
    Returns:
        Hashed password
    """
    hashed_password=hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def store_username_password(username:str, password:str, fullname:str)-> None:
    """This function stores the username and password in the database\n
    Args:
        username: User's username
        password: User's password
        fullname: User's fullname\n
    Returns:
        None
    """
    try:
        connection = psycopg2.connect(
            dbname="try",
            user="postgres",
            password="admin",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(f"insert into users(username,password,fullname) values('{username}','{password}','{fullname}')")
    except (Exception,psycopg2.DatabaseError) as error:
        msg=f'Database error: {error}'
        return msg
    finally:
        if connection is not None:
            connection.commit()
            cursor.close()
            connection.close()

def check_pw(username:str, password:str)-> bool:
    """This function checks the correction of password\n
    Args:
        plain_password: User entered password
        hashed_password: Password stored in database\n
    Returns:
        True if password matches otherwise False
    """
    result= fetch_single_data(f"select password from users where username='{username}'")
    result=result[0]
    hashed_pw=hash_password(password)
    if result == hashed_pw:
        return True
    else:
        return False

def check_user_existence(username:str)-> bool:
    """This function checks whether username exist in database or not\n
    Args:  
        username: User's username\n
    Returns:
        True if user exist otherwise False
    """
    result=fetch_single_data(f"select * from users where username={username}")
    if result:
        return True
    else:
        return False

if __name__=="__main__":
    pass