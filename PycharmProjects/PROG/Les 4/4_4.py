old_password = input('old password')
new_password = input('new password')

if old_password != new_password:
    print(len(new_password) >= 6)

