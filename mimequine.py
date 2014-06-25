#Author: Ernest Kirstein
import smtplib,getpass,base64
print "Your Gmail Address:",
f=raw_input()
p=getpass.getpass()
print "Who's getting it:",
t=raw_input()
m='MIME-Version: 1.0\nSubject: Email Quine\nFrom: %s\nTo: %s\nContent-Type: multipart/mixed; boundary=mm\n\n--mm\nContent-Type: text/plain; charset=UTF-8\n\nThis is a python quine (it produces its own source code). The output is through a Gmail attachment. I hope you enjoy it.\n--mm\nContent-Type: text/plain; charset=US-ASCII; name="mimequine.py"\nContent-Disposition: attachment; filename="mimequine.py"\nContent-Transfer-Encoding: base64\n\n%s\n--mm--'
c='#Author: Ernest Kirstein\nimport smtplib,getpass,base64\nprint "Your Gmail Address:",\nf=raw_input()\np=getpass.getpass()\nprint "Who\'s getting it:",\nt=raw_input()\nm=%r\nc=%r\ns=smtplib.SMTP("smtp.gmail.com:587")\ns.starttls()\ns.login(f,p)\ns.sendmail(f,t,m%%(f,t,base64.b64encode(c%%(m,c))))\ns.quit()\n'
s=smtplib.SMTP("smtp.gmail.com:587")
s.starttls()
s.login(f,p)
s.sendmail(f,t,m%(f,t,base64.b64encode(c%(m,c))))
s.quit()
