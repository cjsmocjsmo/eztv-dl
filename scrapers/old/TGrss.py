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


s1 = re.compile(r"Star Wars Visions")
s2 = re.compile(r"star wars visions")
# s3 = re.compile(r"Strange.New.Worlds")
# s4 = re.compile(r"Star.Trek.Strange.New.Worlds")
s5 = re.compile(r"Baymax")
s6 = re.compile(r"Star.Wars.Lando")
s7 = re.compile(r'Ironheart')
s8 = re.compile(r'IronHeart')
# s9 = re.compile(r"Moonknight")
# s10 = re.compile(r"MoonKnight")
# s11 = re.compile(r"SheHulk")
s12 = re.compile(r"Lando")
s13 = re.compile(r"Star Wars Lando")
s14 = re.compile(r"Rangers Of The New Republic")
s15 = re.compile(r"Rangers.Of.The.New.Republic")
s16 = re.compile(r'Star Wars The High Republic')
s17 = re.compile(r'Star.Wars.The.High.Republic')


s18 = re.compile(r'National Geographic')
# s19 = re.compile(r"Lost In Space")

# s20 = re.compile(r"Mobius")
# s21 = re.compile(r"Morbius")


# s22 = re.compile(r'Moon Knight')
# s23 = re.compile(r'Moon.Knight')
s24 = re.compile(r'She Hulk')
s25 = re.compile(r'She.Hulk')
s26 = re.compile(r'Secret Invasion')
s27 = re.compile(r'Secret.Invasion')
s28 = re.compile(r'Armor Wars')

s30 = re.compile(r"Ahsoka")
s31 = re.compile(r"Star Wars Ahsoka")
s32 = re.compile(r'Star.Wars.Ahsoka')
# s38 = re.compile(r"Marvel Eternals")
# s39 = re.compile(r"Eternals")

s40 = re.compile(r'Acolyte')
s41 = re.compile(r"The Acolyte")
s42 = re.compile(r"Star Wars Acolyte")
s43 = re.compile(r"Star Wars The Acolyte")
s44 = re.compile(r"The.Acolyte")
s45 = re.compile(r"Star.Wars.Acolyte")
s46 = re.compile(r"Star.Wars.The.Acolyte")
s47 = re.compile(r"Andor")
s48 = re.compile(r"Star Wars Andor")
s49 = re.compile(r"Star.Wars.Andor")

s50 = re.compile(r"Lord Of The Rings")
s51 = re.compile(r"lord of the rings")
s52 = re.compile(r"Lord.Of.The.Rings")
s53 = re.compile(r"lord.of.the.rings")
# s54 = re.compile(r"Obi-Wan Kenobi")
# s55 = re.compile(r"Obi Wan Kenobi")
# s56 = re.compile(r"Star Wars Obi Wan Kenobi")
# s57 = re.compile(r"Obi.Wan.Kenobi")
# s58 = re.compile(r"Star.Wars.Obi.Wan.Kenobi")
s59 = re.compile(r"Droid Story")

s60 = re.compile(r"A Droid Story")
s61 = re.compile(r"Star Wars Droid Story")
s62 = re.compile(r'Star Wars A Droid Story')
s63 = re.compile(r"Droid.Story")
s64 = re.compile(r"A.Droid.Story")
s65 = re.compile(r"Star.Wars.Droid.Story")
s66 = re.compile(r'Star.Wars.A.Droid.Story')
s67 = re.compile(r'Groot')
s68 = re.compile(r"I Am Groot")
s69 = re.compile(r"I.Am.Groot")

s75 = re.compile(r'Wakanda')
s76 = re.compile(r'Marvel Wakanda')
s77 = re.compile(r'Marvel.Wakanda')
# s78 = re.compile(r'Halo')
# s79 = re.compile(r'Marvel Hawkeye')

# s80 = re.compile(r'Marvel.Hawkeye')
# s84 = re.compile(r'Spiderman.No.Way.Home')
# s85 = re.compile(r'Spiderman No Way Home')
# s86 = re.compile(r'Spider-Man No Way Home')
# s87 = re.compile(r'Thor Love And Thunder')
# s88 = re.compile(r'Thor.Love.And.Thunder')

s89 = re.compile(r"Andor")

s92 = re.compile(r"Star.Trek.4")
s93 = re.compile(r"Star Trek 4")

# s94 = re.compile(r"Lightyear")
# s95 = re.compile(r"LightYear")


class FeedChecker:

    def __init__(self):
        try:
            os.stat('/home/charliepi/ScraperLogs/TGtv.log')
        except FileNotFoundError:
            with open('/home/charliepi/ScraperLogs/TGtv.log', 'w') as newfile:
                newfile.write("Log created")

        logging.basicConfig(
            filename ='/home/charliepi/ScraperLogs/TGtv.log',
            level = logging.DEBUG,
            format = '%(levelname)s:%(asctime)s:%(message)s',
        )

    def new_ep_check(self, p):
        print(p.title)
        if re.search(s1, p.title) != None:
            return p.title, p.link
        elif re.search(s2, p.title) != None:
            return p.title, p.link
        # elif re.search(s3, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s4, p.title) != None:
        #     return p.title, p.link
        elif re.search(s5, p.title) != None:
            return p.title, p.link
        elif re.search(s6, p.title) != None:
            return p.title, p.link
        elif re.search(s7, p.title) != None:
            return p.title, p.link
        elif re.search(s8, p.title) != None:
            return p.title, p.link
        # elif re.search(s9, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s10, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s11, p.title) != None:
        #     return p.title, p.link
        elif re.search(s12, p.title) != None:
            return p.title, p.link
        elif re.search(s13, p.title) != None:
            return p.title, p.link
        elif re.search(s14, p.title) != None:
            return p.title, p.link
        elif re.search(s15, p.title) != None:
            return p.title, p.link
        elif re.search(s16, p.title) != None:
            return p.title, p.link
        elif re.search(s17, p.title) != None:
            return p.title, p.link
        elif re.search(s18, p.title) != None:
            return p.title, p.link
        # elif re.search(s19, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s20, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s21, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s22, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s23, p.title) != None:
        #     return p.title, p.link
        elif re.search(s24, p.title) != None:
            return p.title, p.link
        elif re.search(s25, p.title) != None:
            return p.title, p.link
        elif re.search(s26, p.title) != None:
            return p.title, p.link
        elif re.search(s27, p.title) != None:
            return p.title, p.link
        elif re.search(s28, p.title) != None:
            return p.title, p.link
        # elif re.search(s29, p.title) != None:
        #     return p.title, p.link

        elif re.search(s30, p.title) != None:
            return p.title, p.link
        elif re.search(s31, p.title) != None:
            return p.title, p.link
        elif re.search(s32, p.title) != None:
            return p.title, p.link

        # elif re.search(s37, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s38, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s39, p.title) != None:
        #     return p.title, p.link

        elif re.search(s40, p.title) != None:
            return p.title, p.link
        elif re.search(s41, p.title) != None:
            return p.title, p.link
        elif re.search(s42, p.title) != None:
            return p.title, p.link
        elif re.search(s43, p.title) != None:
            return p.title, p.link
        elif re.search(s44, p.title) != None:
            return p.title, p.link
        elif re.search(s45, p.title) != None:
            return p.title, p.link
        elif re.search(s46, p.title) != None:
            return p.title, p.link
        elif re.search(s47, p.title) != None:
            return p.title, p.link
        elif re.search(s48, p.title) != None:
            return p.title, p.link
        elif re.search(s49, p.title) != None:
            return p.title, p.link

        elif re.search(s50, p.title) != None:
            return p.title, p.link
        elif re.search(s51, p.title) != None:
            return p.title, p.link
        elif re.search(s52, p.title) != None:
            return p.title, p.link
        elif re.search(s53, p.title) != None:
            return p.title, p.link
        # elif re.search(s54, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s55, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s56, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s57, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s58, p.title) != None:
        #     return p.title, p.link
        elif re.search(s59, p.title) != None:
            return p.title, p.link

        elif re.search(s60, p.title) != None:
            return p.title, p.link
        elif re.search(s61, p.title) != None:
            return p.title, p.link
        elif re.search(s62, p.title) != None:
            return p.title, p.link
        elif re.search(s63, p.title) != None:
            return p.title, p.link
        elif re.search(s64, p.title) != None:
            return p.title, p.link
        elif re.search(s65, p.title) != None:
            return p.title, p.link
        elif re.search(s66, p.title) != None:
            return p.title, p.link
        elif re.search(s67, p.title) != None:
            return p.title, p.link
        elif re.search(s68, p.title) != None:
            return p.title, p.link
        elif re.search(s69, p.title) != None:
            return p.title, p.link



        # elif re.search(s74, p.title) != None:
        #     return p.title, p.link
        elif re.search(s75, p.title) != None:
            return p.title, p.link
        elif re.search(s76, p.title) != None:
            return p.title, p.link
        elif re.search(s77, p.title) != None:
            return p.title, p.link
        # elif re.search(s78, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s79, p.title) != None:
        #     return p.title, p.link

        # elif re.search(s80, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s81, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s82, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s83, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s84, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s85, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s86, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s87, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s88, p.title) != None:
        #     return p.title, p.link
        elif re.search(s89, p.title) != None:
            return p.title, p.link


        # elif re.search(s90, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s91, p.title) != None:
        #     return p.title, p.link
        elif re.search(s92, p.title) != None:
            return p.title, p.link
        elif re.search(s93, p.title) != None:
            return p.title, p.link
        # elif re.search(s94, p.title) != None:
        #     return p.title, p.link
        # elif re.search(s95, p.title) != None:
            return p.title, p.link

        else:
            return None

    # def email_list2(self, provider, emailList):
    #     email = "porthose.cjsmo.cjsmo@gmail.com"
    #     pas = "!!Porthose19600"
    #     sms_gateway = '9038201482@mymetropcs.com'
    #     smtp = "smtp.gmail.com"
    #     port = 587
    #     server = smtplib.SMTP(smtp, port)
    #     server.starttls()
    #     server.login(email, pas)
    #     msg = MIMEMultipart()
    #     msg['From'] = email
    #     msg['To'] = smtp
    #     prov = provider + '\n'
    #     msg['Subject'] = prov
    #     new_string = ''
    #     if len(emailList) != 0:
    #         for em in emailList:
    #             new_email = em[:-10] + "\n\n"
    #             new_string = new_string + new_email
    #     else:
    #         new_string = "No New TvShows\n"
    #         logging.debug("No New TvShows")
    #     body = new_string
    #     msg.attach(MIMEText(body, 'plain'))
    #     sms = msg.as_string()
    #     server.sendmail(email,sms_gateway,sms)
    #     server.quit()

    def tg_rss2(self):
        print("TG RSS Feed")
        Feed = feedparser.parse('https://torrentgalaxy.mx/rss')
        pointer = Feed.entries
        eplist = []
        for p in pointer:
            if p.tags[0]['term'] == "Music : Albums" or p.tags[0]['term'] == "Music : Loseless":
                print(p.title)
            if p.tags[0]['term'] == "TV : Episodes HD":
                foo = self.new_ep_check(p)
                if foo != None:
                    eplist.append(foo[0])
            if p.tags[0]['term'] == "TV : Episodes SD":
                foo = self.new_ep_check(p)
                if foo != None:
                    eplist.append(foo[0])
        if len(eplist) < 1:
            print("No new TvShows")
            logging.debug("No New TvShows")
        else:
            print(eplist)
            logging.debug(len(eplist))

    def eztv_rss2(self):
        print("\nEZTV RSS Feed")
        Feed = feedparser.parse('https://eztv.re/ezrss.xml')
        print(Feed)
        pointer = Feed.entries
        ep_list = []
        for p in pointer:
            if p.category == "TV":
                foo = self.new_ep_check(p)
                if foo != None:
                    ep_list.append(foo[0])
        if len(ep_list) < 1:
            logging.debug("No new TvShows")
            print("No new TvShows")
        else:
            # self.email_list2('eztv', ep_list)
            print(ep_list)
            logging.debug(len(ep_list))

    def main(self):
        self.tg_rss2()
        time.sleep(15)
        self.eztv_rss2()

if __name__ == "__main__":
    bar = FeedChecker()
    bar.main()
