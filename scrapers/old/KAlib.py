#!/usr/bin/python3
import re
from bs4 import BeautifulSoup
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from email.mime.multipart import MIMEMultipart
# import logging

TEN = re.compile("1080p")
SEV = re.compile("720p")

# def newnew_search_for_new_episode(metadata, EP):
#     linklist = []
#     list1080p = []
#     list720p = []
#     for meta in metadata:
#         if meta[0] != None:
#             s1 = re.search(ML, meta[0])
#             s2 = re.search(EP, meta[0])
#             # s3 = re.search(SMB, meta[0])
#             s4 = re.search(TEN, meta[0])
#             s5 = re.search(SEV, meta[0])
#             # if s1 is not None and s2 is not None and s3 is not None:
#             if s1 is not None and s2 is not None:
#                 if s4 is not None:
#                     # if s1 != None and s2 != None and s3 != None and s4 != None:
#                     list1080p.append(meta)
#                 elif s4 is None and s5 is not None:
#                     # elif s1 != None and s2 != None and s3 != None and s4 == None and s5 != None:
#                     list720p.append(meta)
#                 else:
#                     pass
#     if len(list1080p) != 0:
#         linklist.append(list1080p[0])
#     elif len(list720p) != 0:
#         linklist.append(list720p[0])
#     return linklist

# def search_entry_for_title(page, search1):
#     returnlist = []
#     soup = BeautifulSoup(page, 'html.parser')
#     for link in soup.findAll("a"):
#         meta = (link.get("title"), link.get('href'))
#         if meta[0] != None:
#             # if re.search(MP4, meta[1]) != None:
#             # print(meta[1])
#             for element in search1:
#                 if re.search(element, meta[0]) != None:
#                     returnlist.append(meta)
#     return returnlist

def search_for_new_episode(page, title, episode):
    linklist = []
    list1080p = []
    list720p = []
    soup = BeautifulSoup(page, 'html.parser')
    count = 0
    for link in soup.findAll("a"):
        count += 1
        meta = (link.get("title"), link.get('href'))

        if meta[0] != None:
            if re.search(title, meta[1]) != None:
                if re.search(episode, meta[1]) != None:
                    if re.search(TEN, meta[1]) != None:
                        list1080p.append(meta[1])
                    elif re.search(SEV, meta[1]) != None:
                        list720p.append(meta[1])
                    else:
                        pass

    # print(list1080p)
    # print(list720p)
    return (list1080p, list720p)
    #         s1 = re.search(ML, meta[0])
    #         s2 = re.search(EP, meta[0])
    #         # s3 = re.search(SMB, meta[0])
    #         s4 = re.search(TEN, meta[0])
    #         s5 = re.search(SEV, meta[0])
    #         # if s1 is not None and s2 is not None and s3 is not None and s4 is not None:
    #         if s1 is not None and s2 is not None and s4 is not None:

    #             list1080p.append(meta)
    #         # elif s1 is not None and s2 is not None and s3 is not None and s4 is None and s5 is not None:
    #         elif s1 is not None and s2 is not None and s4 is None and s5 is not None:
    #             list720p.append(meta)
    #         else:
    #             pass
    # if len(list1080p) != 0:
    #     linklist.append(list1080p[0])
    # elif len(list720p) != 0:
    #     linklist.append(list720p[0])
    # return linklist

# def tgx_search_entry_for_title(page, search1):
#     returnlist = []
#     soup = BeautifulSoup(page, 'html.parser')
#     for link in soup.findAll("a"):
#         meta = (link.get("title"), link.get('href'))

#         skiplist = [
#             None,
#             'comments',
#             "Trusted Uploader",
#             "Torrent Officer",
#             "Trial Uploader",
#             "Verified Uploader",
#         ]

#         if meta[0] not in skiplist:
#             for element in search1:
#                 if re.search(element, meta[0]) != None:
#                     returnlist.append(meta)

#         # if meta[0] != None:
#         #     if meta[0] != 'comments':
#         #         if meta[0] != "Trusted Uploader":
#         #             if meta[0] != "Torrent Officer":
#         #                 if meta[0] != "Trial Uploader":
#         #                     if meta[0] != "Verified Uploader":
#         #                         print(meta[0])
#         #                         for element in search1:
#         #                             if re.search(element, meta[0]) != None:
#         #                                 returnlist.append(meta)
#     return returnlist




# def ep_check(p, asearch):
#     for s in asearch:
#         if re.search(s, p.title) != None:
#             return p.title, p.link
#         else:
#             return None

# def tgx_search_rss(feed, asearch):
#     print("TG RSS Feed")
#     # Feed = feedparser.parse('https://torrentgalaxy.mx/rss')
#     pointer = feed.entries
#     eplist = []
#     for p in pointer:
#         if p.tags[0]['term'] == "TV : Episodes HD":
#             foo = ep_check(p, asearch)
#             if foo != None:
#                 eplist.append(foo[0])
#     if len(eplist) < 1:
#         print("No new TvShows")
#         # logging.debug("No New TvShows")
#         return None
#     else:
#         print(eplist)
#         # self.email_list2('tg', eplist)
#         # logging.debug(eplist)
#         return eplist

# def email_list3(provider, emailList):
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
#         new_string =  emailList + "  found\n"
#         logging.debug(new_string)
#     else:
#         new_string = "No New TvShows\n"
#         logging.debug(new_string)
#     body = new_string
#     msg.attach(MIMEText(body, 'plain'))
#     sms = msg.as_string()
#     server.sendmail(email,sms_gateway,sms)
#     server.quit()