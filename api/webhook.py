import os
import json
import requests
from http.server import BaseHTTPRequestHandler

TOKEN = os.environ.get("TOKEN")

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        update = json.loads(body)

        if "chat_member" in update:
            member = update["chat_member"]
            if member["new_chat_member"]["status"] == "member":
                user_id = member["new_chat_member"]["user"]["id"]
                requests.post(
                    f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                    data={
                        "chat_id": user_id,
                        "caption": "Coucou ♥️
Trop cool que tu sois venue sur mon telegram privé !\n\nSi ça te dit je te donne un accès gratuit pour mon OF pour aujourd’hui pour qu’on puisse faire connaissance 😏\n\nhttps://onlyfans.com/amanda.lpz/c66",
                        "photo": "https://raw.githubusercontent.com/angelfan081223-spec/bienvenue-bot-telegram/main/photo.jpg.png"
                    }
                )

        self.send_response(200)
        self.end_headers()
