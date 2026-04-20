
# validate user input exersise!

username= ('Enter username: ') #input

if len(username) > 12: #print all is missing
  ('your username cannot be more than 12 characters long :<')
elif len(username) < 4:
  ('username has to have a minimum of 3 characters')
elif not username.find(' ') == -1:
  ('username cannot contain spaces!')
elif not username.isalpha():
  ('username cannot contain numbers')
else:
  (f'Welcome {username} ! username looking good! ')
