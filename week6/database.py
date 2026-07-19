import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        user=os.environ.get("DB_USER", "root"),
        password=os.environ["DB_PASSWORD"],
        database=os.environ.get("DB_NAME", "website"),
        )

def get_member_by_email(email):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id FROM member WHERE email = %s", (email,))
            return cursor.fetchone()
    finally:
        conn.close()

def create_member(name, email, password):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO member (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password),
                )
        conn.commit()
    finally:
        conn.close()
        
def get_member_by_login(email, password):
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT id, name, email FROM member WHERE email = %s AND password = %s",
                (email, password),
                )
            return cursor.fetchone()
    finally:
        conn.close()

def create_message(member_id, content):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO message (member_id, content) VALUES (%s, %s)",
                (member_id, content),
                )
        conn.commit()
    finally:
        conn.close()


def get_all_messages():
    conn = get_connection()
    try:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT message.id, message.member_id, member.name, message.content "
                "FROM message JOIN member ON message.member_id = member.id "
                "ORDER BY message.id DESC"
                )
            return cursor.fetchall()
    finally:
        conn.close()


def delete_message(message_id, member_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM message WHERE id = %s AND member_id = %s",
                (message_id, member_id),
                )
            deleted = cursor.rowcount
        conn.commit()
        return deleted > 0
    finally:
        conn.close()