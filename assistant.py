import discord
import argparse
from selenium import webdriver

class Assistant(discord.Client):
    def __init__(self, channel):
        self.channel = channel
        self.players = {
            "GUBETON": "GUBET",
            "Tomygub": "gub",
            "Poltibo": "5406",
            "Clavelloux": "EUW",
            "Lambabar": "EUW"
        }

        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(intents=intents)

    async def on_ready(self):
        print("Assistant ready")
        await self.user.edit(username="LP Assistant")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='une game catastrophique'))

    async def on_message(self, message):
        channel = self.get_channel(self.channel)
        if message.author.bot:
            return
        
        if "Statut de partie" in message.content:
            for player in self.players:
                if player in message.content:
                    await channel.send(player + " - " + self.players[player])
            return

parser = argparse.ArgumentParser()
parser.add_argument('--dev', action='store_true')
parser.add_argument('--token', default="")

args = parser.parse_args()

if args.dev:
    channel = 1177613261475152005
else:
    channel = 1177345536127418379

lp_assistant = Assistant(channel)
lp_assistant.run(args.token)

#DRIVER = "chromedriver"
#driver = webdriver.Chrome(DRIVER)
#driver.get('https://www.spotify.com')
#screenshot = driver.save_screenshot('my_screenshot.png')
#driver.quit()