from functions import notify_friends, send_email
from events_systems import *

# services
def create_user(username: str, password: str):
    print("User was saved ", username, password)
    dispatch("user_registered", username)
    #send_email(username)
    #notify_friends(username)




# main.py / bootstrap.py
register_event("user_registered", send_email)
register_event("user_registered", notify_friends)


create_user("Martin", "123abc")