from instapy import InstaPy, smart_run

username = input('username: ')
password = input('password: ')

session = InstaPy(username=username, password=password, headless_browser=True)
tags = [
  'illustration',
  'drawing',
  'clipstudiopaint',
  'digitalart',
  'flamengo'
]

with smart_run(session):
  session.set_user_interact(amount=5, media='Photo')
  session.like_by_tags(tags,amount=3)