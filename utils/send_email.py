import yagmail
def send_mails(file):
    s=yagmail.SMTP(user="3421804764@qq.com",password="ubnavehqwgiddcbe",host="smtp.qq.com")
    s.send(to="3421804764@qq.com",subject="这是发送邮箱",contents="发送报告和日志",attachments=file)
    return s