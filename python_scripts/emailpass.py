import smtplib
  
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
  
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()

f = open("usersregionais.txt", 'r').read()

import re

pattern = re.compile(r'(.*?),(.*?),(.*?),(.*?),\n', re.UNICODE | re.DOTALL)

for match in pattern.finditer(f):
	print "%s %s %s %s" % (match.group(1),match.group(2),match.group(3),match.group(4))
	msg = "Se vc esta recebendo este email, é pq deu certo meu script... aqui estão seu user e senha para os treinos do boca sobre a s provas regionais passadas..  user: %s  senha: %s" % (match.group(3),match.group(4)) 
	sendemail(from_addr    = 'fuiripecn@gmail.com', 
          to_addr_list = [str(match.group(1))],
          cc_addr_list = [], 
          subject      = 'User e senha maratona', 
          message      = msg
          login        = 'fuiripecn', 
          password     = 'password')


