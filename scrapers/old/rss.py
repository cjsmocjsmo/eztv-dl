#!/usr/bin/python3
import os
import re
import time
import logging
import feedparser
import smtplib 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

class YTSFeedChecker:
    def __init__(self):
        self.oldytsList = ''
        self.oldyts_date = ''
        self.ytsFoundList = []
        try:
            os.stat('/home/charliepi/ScraperLogs/rss.log')
        except FileNotFoundError:
            with open('/home/charliepi/ScraperLogs/rss.log', 'w') as newfile:
                newfile.write("Log created")
        logging.basicConfig(
            filename ='/home/charliepi/ScraperLogs/rss.log',
            level = logging.DEBUG,
            format = '%(levelname)s:%(asctime)s:%(message)s',
        )

    def email_list(self, provider, emailList):
        email = "porthose.cjsmo.cjsmo@gmail.com"
        pas = "!!Porthose19600"
        # pas = "zhbaijvcuwgpsseq"
        sms_gateway = '9038201482@mymetropcs.com'
        smtp = "smtp.gmail.com" 
        port = 587
        server = smtplib.SMTP(smtp, port)
        server.starttls()
        server.login(email, pas)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = smtp
        prov = provider + '\n'
        msg['Subject'] = prov
        new_string = ''
        for em in emailList:
            new_email = em + "\n\n"
            new_string = new_string + new_email
        body = new_string
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(email,sms_gateway,sms)
        server.quit()
        logging.debug("Email Sent")

    def yts_rss(self):
        logging.debug("Starting yts_rss")
        Feed = feedparser.parse('https://yts.pm/rss')
        pointer = Feed.entries
        print("\n\nYTS Movies rss feed\n")
        logging.debug("YTS Movies rss feed")
        ytsList = []
        for p in pointer:
            ytsList.append(p.title)
            print(p.title)
            # logging.debug("this is p.title: \n %s", p.title)
        ytsList.sort()
        if len(self.oldytsList) == 0:
            self.oldytsList = ytsList
            # self.email_list("yts", ytsList)
            logging.debug("this is ytslist: \n %s", ytsList)
        elif self.oldytsList != ytsList:
            # self.email_list("yts", ytsList)
            logging.debug("this is ytslist: \n %s", ytsList)
        else:
            print("No new Movies")
            logging.debug("No new Movies")
        logging.debug("\n yts_rss is complete \n")

    def main(self):
        self.yts_rss()

if __name__ == "__main__":
    bar = YTSFeedChecker()
    bar.main()
