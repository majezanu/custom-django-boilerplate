from django_channels_notifications.core import Notification  
from django_channels_notifications.core.channels import MailChannel  
from django.core.mail import EmailMessage
from django.template import loader
from django.core.mail import EmailMultiAlternatives
 
      
class ResetPasswordNotification(Notification):

  def __init__(self,subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):
        self.subject_template_name = subject_template_name
        self.email_template_name = email_template_name
        self.context = context
        self.from_email = from_email
        self.to_email = to_email
        self.html_email_template_name = html_email_template_name

      # Get the notification's delivery channels.  
  def via(self, notifiable):  
        return [MailChannel]  
  
  # Get the dict representation of the notification.  
  def to_mail(self, notifiable):  
        subject = loader.render_to_string(self.subject_template_name, self.context)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(self.email_template_name, self.context)

        email_message = EmailMultiAlternatives(subject, body, self.from_email, [self.to_email])
        if self.html_email_template_name is not None:
            html_email = loader.render_to_string(self.html_email_template_name, self.context)
            email_message.attach_alternative(html_email, 'text/html')
        return email_message