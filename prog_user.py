import argparse
parser = argparse.ArgumentParser()
from dbcon import db_connect
from models import User
from psycopg2.extras import RealDictCursor


parser = argparse.ArgumentParser(description='process given commands')
parser.add_argument("-u", "--username", help="takes email")
parser.add_argument("-p", "--password", help="takes password")
parser.add_argument("-n", "--new-pass", help="new password")
parser.add_argument("-l", "--list", help="list all users")
parser.add_argument("-d", "--delete", help="takes email address of a person u want to delete")
parser.add_argument("-e", "--edit", help="takes email for user which You want to edit")

args = parser.parse_args()

if args.username != None and args.password != None and args.delete == None and args.edit == None:
    sql = f"""SELECT user_email FROM users WHERE user_email='{args.username}'"""
    c = db_connect().cursor(cursor_factory=RealDictCursor)
    c.execute(sql)
    data = c.fetchone()
    if data != None:
        raise NameError('User with that username already exist, think of another username')
    else:
        if len(args.password) >= 8:
            new_user = User()
            new_user.username = args.username
            new_user.user_email = args.username
            new_user.password = args.password
            new_user.save_to_db()
        else:
            print('password that u Gave is too short, password must be at least 8 characters')

if args.username != None and args.password != None and args.delete != None:
    sql = f"""SELECT user_id, user_name, user_email, password FROM users WHERE user_email='{args.username}'"""
    c = db_connect().cursor()
    c.execute(sql)
    data = c.fetchone()
    c.close()
    if data[3] == args.password:
        sql = f"""DELETE FROM Users WHERE user_id='{data[0]}'"""
        c = db_connect().cursor()
        c.execute(sql)
        c.close()
        print('user deleted')
    else:
        print('incorect password')









