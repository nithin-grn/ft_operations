import streamlit as st
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import auxillaries as ax
import smtplib
import os

def send_email_report(act_df, sales_df):
  today = ax.today_date_string()
  
  multipart = MIMEMultipart()
  try:
    email = st.secrets['email']
    password = st.secrets['password']
  except KeyError:
    email = os.environ.get("email")
    password = os.environ.get("password")
      
  multipart["From"] = f"FT Operations <{email}>"
  multipart["To"] = email
  multipart["Subject"] = f'FT Daily Report - {today}'  

  act_today = act_df.loc[act_df['Date'] == today].to_html(index=False, escape=False, na_rep='Not updated', border = 0)
  sales_today = sales_df.loc[sales_df['Date'] == today].to_html(index=False, escape=False, na_rep='Not updated', border = 0)
  
  message = f"""\
  <p>Greetings,</p>
  <p>Here is today's operation report:</p><br>  
  <p><strong>Operations:</strong></p>
  {act_today}
  <br>
  <p><strong>Sales Report:</strong></p>
  {sales_today}
  <br>
  <p>Cheers.</p>
  """
  
  multipart.attach(MIMEText(message, "html"))
  
  server = smtplib.SMTP("smtp.gmail.com", 587)
  server.starttls()
  server.login(email, password)
  server.sendmail(email, email, multipart.as_string())
  server.quit()
