#>>>>>>>>>>>>>>>>>>>>>>  @vince frost <<<<<<<<<<<<<<<<<<<<<<<<
#>>>>>>>>>>>>>>>>>>>>>>  p.avince001@gmail.com  <<<<<<<<<<<<<<


alpha_set = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASFGHJKLZXCVBNM1234567890'
new_message = ''
message = input('Enter your message: ')
secret_key = int(input('Enter the secret_key (1-50):'))
for char in message:
  if char in alpha_set:
    position = alpha_set.find(char)
    new_position = (position + secret_key) % 61
    new_char = alpha_set[new_position]
    new_message = new_message + new_char
  else:
    new_message = new_message + char
print('Your encrypted:', new_message)
