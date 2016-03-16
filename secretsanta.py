from random import shuffle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

attendees_test = [	{"name": "Glenn", "email": ""}]

attendees = [
	{"name": "Balram", "email": ""}]

me = "glenn@glennji.com"
# you = "Glenn Mason <glenn@glennji.com>"

shuffle(attendees)

# Send the message via local SMTP server.
username = os.environ["GMAIL_USERNAME"]
password = os.environ["GMAIL_PASSWORD"]
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

for (i, a) in enumerate(attendees):
	buyer = attendees[i]
	receipient = attendees[i -1]
	#print("{0} ({1}) buys for ???".format(buyer["name"], buyer["email"]))
	you = buyer["email"]
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "For Action: Secret Santa (Take #2) - and your gift goes to ..."
	msg['From'] = me
	msg['To'] = you

	# Create the body of the message (a plain-text and an HTML version).
	#text = "Hi {1}! A very Christmassy draw has been made (Python code available upon request) and you've been selected to buy a gift for {0}!".format(buyer["name"], receipient["name"])
	html = """\
	<html>
	  <head></head>
	  <body>
	    <p>Merry Christmas {0}!<p>
	    <p>So, the Secret Santa draw has been made (NEWLY PATCHED Python code available upon request) and you've been selected to buy a gift for <b>{1}</b>!</p>
	    <p>IGNORE ANY EARLIER EMAIL! Each time the script runs, it randomly pairs up gifters and giftees. There's a chance you've been asked to buy a gift for the same
	     person as last time, but it's just a coincidence, I promise. In the meantime, let's all talk about our QA processes ...</p>
	    <p>Remember, the Rules Of Secret Santa are:
	    <ol>
					<li>Don't talk about fight-club.
					<li>You buy an anonymous present for your GIFTEE (up to $20 maximum) &amp; label it with their name.
					<li>Someone else buys YOU an anonymous present.
					<li>...
					<li>PRESENTS!!
				</ol>
    	</p>
    	<p>We'll get all the gifts to the Christmas party and hand 'em out, so please give them to Alex for safe-keeping ahead of the party.</p>
    	<p>Look forward to MY CODE WORKING, and seeing the looks of joy and happiness on everyones faces!</p>
	  </body>
	</html>
	""".format(buyer["name"], receipient["name"])

	# Record the MIME types of both parts - text/plain and text/html.
	#part1 = MIMEText(text, 'plain')
	part2 = MIMEText(html, 'html')

	# Attach parts into message container.
	# According to RFC 2046, the last part of a multipart message, in this case
	# the HTML message, is best and preferred.
	#msg.attach(part1)
	msg.attach(part2)

	# sendmail function takes 3 arguments: sender's address, recipient's address
	# and message to send - here it is sent as one string.
	server.sendmail(me, you, msg.as_string())

# All done
server.quit()