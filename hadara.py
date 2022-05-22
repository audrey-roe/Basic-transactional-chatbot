import json
import requests
# from cgitb import text
import requests
from .connect import whatsapp as wa

class Whatsappbot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.WhatsappAPIUrl = '' #paste Url here
        self.token = '' #paste token here update every 23 hours until permanent token is made, remember to keep private

    def send_requests(self, type, data):
        url = f"{self.WhatsappAPIUrl}{type}?token={self.token}"
        headers = { "Authorization" : "Bearer ", #input token
            "Content-type" : "application/json"}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = """Hello, welcome to Hadara kid👋🏾, what can i help you with today?\n
            [1] 📱 Browse Catalogue\n
            [2] 🔻 Discounts\n
            [3] 🛒 Place Order\n
            [4] 🤝 Subcribe to news letter
            """
        else:
            welcome_string = "I'm sorry i don't think I understand you"
        return self.send_message(chatID, welcome_string)

    def Welcome_prompt(self):
        if self.dict_messages != []:
            message =self.dict_messages
            text = message['body'].split()
            if not message['fromMe']:
                chatID  = message['from'] 
                if text[0].lower() == 'Browse Catalogue' or '1':
                    return self.browse_catalogue(chatID)
                elif text[0].lower() == 'Discounts' or '2':
                    return self.discounts(chatID)
                elif text[0].lower() == 'Place Order' or '3':
                    return self.send_image(chatID)
                elif text[0].lower() == 'Subcribe to News Letter' or '4':
                    return self.send_video(chatID)
                else:
                    return self.welcome(chatID, True)
            else: 
                return self.send_error_message(chatID)

    def browse_catalogue(self, chatID):
        data = {"to" : chatID,
                "preview_url": True,
                "type": "text",
                "data" : "website browse catalouge  https://hadarakids.com/product-category/girl-2/"}
        answer = self.send_requests('message/chat', data)
        return answer

    def discounts(self, chatID):
        data = {"to" : chatID,
                "preview_url": True,
                "type": "text",
                "data" : "only products with discounted prices in the catalogue are displayed each product still has a special two digit numerical Identifier"}
        answer = self.send_requests('message/chat', data)
        return answer

    def place_order(self, chatID):
        data = {"to" : chatID,
                "type": "text",
                "data" : input("please input the product 2 digit ID to place an order")}
        answer =  self.send_requests('input', data) #come back to correct function
        return answer
    
    def news_letter(self, chatID):
        data = {"to": chatID,
                "type": "text",
                "data" : "Please may we have your email address" }
        answer = self.send_requests('messages/chat', data)
        return answer
