class Notifier:
  def send_notification(self,method,email=None,subject=None,phone=None,message=""):
    if method=="email":
      if email and subject:
        return f"email is: {email} with Subject of: {subject}"
      else:
        return "email and subject is needed for sending mail"
    elif method=="sms":
      if phone and message:
        return f"Phone number is: {phone} and message is: {message}"
    else:
      return "Invalid notification method"
    


notifier= Notifier()

print(notifier.send_notification(method="email",email="sample@gmail.com",subject="this is a email"))
print(notifier.send_notification(method="sms",phone="8892440666",message="this is a message"))
