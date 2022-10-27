#_*_coding: utf-8_*_
from ast import AugStore, keyword
from email import message
import random
from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Youtube Live Chat Popout URL here
ytLiveChat = "https://www.youtube.com/live_chat?is_popout=1&v=ZoUeMiFZf74" 

def getHTML(url):
    # start web browser
    browser=webdriver.Firefox()
    # get source code
    browser.get(ytLiveChat)
    time.sleep(2)
    page_source = browser.page_source
    browser.close()  #dont forget close the browser
    return page_source

def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')

def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")

def getParticipants(messages):
    #if you want to init a emty set, you have to use set()
    participants = set() 

    for message in messages:
        content = message.find("div", {"id": "content"})
        author = message.find("span", {"id": "author-name"}).text
        message_content = message.find("span", {"id": "message"}).text
        if "emre" in message_content.lower():
            participants.add(author)
    return participants

def startDrawing(participantsList):
    print("Draw is starting. {totalUserCount} people joined the draw".format(totalUserCount = len(participantsList)))
    time.sleep(2)
    print("Participants: ", participantsList)
    print("Winner: ", random.choice(participantsList))
    

html_source = getHTML(ytLiveChat)
soup = parseHTML(html_source)
messages = getMessages(soup)
participants =  getParticipants(messages)
participantsList = list(participants)
startDrawing(eligibleUsersList)