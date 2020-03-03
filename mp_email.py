import imaplib
import base64
def auth_email():
    email_user = input('Email: ')
    email_pass = input('Password: ')

    M = imaplib.IMAP4_SSL('imap-mail.outlook.com', 993)
    M.login(email_user, email_pass)
    M.select()

    typ, message_numbers = M.search(None, 'ALL')  # change variable name, and use new name in for loop

    for num in message_numbers[0].split():
        typ, data = M.fetch(num, '(RFC822)')
        # num1 = base64.b64decode(num)          # unnecessary, I think
        print(data)   # check what you've actually got. That will help with the next line
        data1 = base64.b64decode(data[0][1])
        print('Message %s\n%s\n' % (num, data1))

    M.close()
    M.logout()
