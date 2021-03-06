import smtplib
import datetime
from email.mime.text import MIMEText

fromaddr = 'cpeng@augustatek.com'
toaddrs  = 'jiajia@augustatek.com.cn,cpeng@augustatek.com'
#toaddrs  = 'cpeng@augustatek.com'
ccaddrs = 'cpeng@augustatek.com'

team = ''
weekly = False

def set_team(t):
    global team
    team = t

def gen_subject():
    dt = datetime.datetime.now()
    subj = "EVA project issues "
    if weekly:
        subj += "weekly update - "
    else:
        subj += "daily update - "
    
    subj += "%s team " % team     
    subj += "%s/%s %s:%02d"%(dt.month, dt.day, dt.hour, dt.minute) + "\r\n"
    return  subj

def send_text(text):
    msg = MIMEText(text,'plain','utf-8')
    send(msg)
    
def send_html(html):
    msg = MIMEText(html, 'html', 'utf-8')
    send(msg)
    
def send(msg):
    msg['Subject']= gen_subject()
    msg['From'] = fromaddr
    msg['To'] = toaddrs
    #msg['Cc'] = ccaddrs

    with open(".passwd") as f:
        user,passwd = eval(f.readline())
    
    server = smtplib.SMTP_SSL('mailbj.augustatek.com.cn')
    server.set_debuglevel(1)
    server.login(user, passwd)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    msg = "hello"
    r = send_text(msg)
