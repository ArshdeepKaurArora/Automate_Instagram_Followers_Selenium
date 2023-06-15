from insta_follower import InstaFollower

# login credentials
email_id = 'YOUR EMAIL'
password = 'YOUR PASSWORD'
user_name = 'YOUR USERNAME'

# object from related class
insta_account = InstaFollower()

# login to insta
insta_account.login(user_name,password)

# To scroll down the follower list
insta_account.find_followers()

# to follow the followers present in the scrolled list
insta_account.follow()