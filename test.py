from models import User

x = User()
x.user_name = 'Jan'
x.user_email = 'swierad-5@gmail.com'
x.password = "pomidor"


#x.save_to_db()


User.load_all_users


