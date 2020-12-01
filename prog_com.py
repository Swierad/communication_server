import argparse
parser = argparse.ArgumentParser()
from dbcon import db_connect
from models import Message

parser = argparse.ArgumentParser(description='process given commands')

parser.add_argument("-u", "--username", help="takes username")
parser.add_argument("-p", "--password", help="takes password")
parser.add_argument("-l", "--list", help="list all massages")
parser.add_argument("-t", "--to", help="takes email address of a person u want to contact")
parser.add_argument("-s", "--send", help="text")

args = parser.parse_args()


if args.list != None:
    if args.username  == None or args.password == None:
        print("to list messages You need to type username and password")
    else:
        sql = f"""SELECT user_id, user_email, password FROM users WHERE user_email='{args.username}'"""
        c = db_connect().cursor()
        c.execute(sql)
        data = c.fetchone()
        sql = f"""SELECT text, creation_date FROM message Where to_id = '{data[0]}'"""
        ret = []
        c.execute(sql)
        data = c.fetchall()
        c.close()
        for row in data:
            print(f"""wiadomość: {row[0]} data:{row[1]}""")



if args.send != None:
    sql = f"""SELECT user_id, user_name, user_email, password FROM users WHERE user_email='{args.username}'"""
    c = db_connect().cursor()
    c.execute(sql)
    from_user = c.fetchone()
    c.close()
    sql = f"""SELECT user_id, user_email FROM users WHERE user_email='{args.to}'"""
    c = db_connect().cursor()
    c.execute(sql)
    to_user = c.fetchone()
    c.close()
    if len(args.send) > 256:
        print("message is too long, it cannot contain more than 256 characters")
    else:
        if args.username != from_user[2]:
            print(f"""there is no such user as {args.username}""")
        elif args.to != to_user[1]:
            print(f"""there is no such user as {args.to}""")
        elif args.password != from_user[3]:
            print(f"""wrong password: {args.to}""")
        else:
            new_massage = Message()
            new_massage.from_id = from_user[0]
            new_massage.to_id = to_user[0]
            new_massage.text = args.send
            new_massage.save_to_db_msg()
            






