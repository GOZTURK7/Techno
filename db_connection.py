# STUDENT FEEST - TECHNO
# Auteur: Gökhan Öztürk


import mysql.connector
import config

def get_connection():
    return mysql.connector.connect(
    host = config.HOST,
    user = config.USER,
    port = config.PORT,
    password = config.PASSWORD,
    database = config.DATABASE
)
