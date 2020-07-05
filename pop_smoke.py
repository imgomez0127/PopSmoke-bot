import logging
import os
from urllib.parse import urljoin
from random import randrange
import traceback
import discord

class PopSmoke(discord.Client):
    def __init__(self,debug=True):
        super().__init__()
        if debug:
            if(not os.path.exists("./logs")):
                os.mkdir("./logs")
            logger = logging.getLogger('discord')
            logger.setLevel(logging.DEBUG)
            handler = logging.FileHandler(filename="./logs/discord.log",encoding="utf-8",mode="a")
            handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s"))
            logger.addHandler(handler)
        self.special_users = {}
        self.should_play = True
        self.music_files = ["clip1.mp3", "clip2.mp3", "clip3.mp3"]

    async def on_ready(self):
        print("logged in as {0}!".format(self.user))

    async def on_message(self,message):
        if message.author == self.user:
            return
        if message.content.startswith("PopSmoke add"):
            ids = message.content.split(" ")[2:]
            for client_id in ids:
                self.special_users.add(int(client_id))
        if message.content.startswith("PopSmoke remove"):
            self.special_users -= set(map(int,message.content.split(" ")[2:]))
        if message.content.startswith("!PopSmoke"):
            self.should_play = not self.should_play
            return

    async def on_voice_state_update(self,member,before,after):
        if self.should_play:
            if member.id in self.special_users:
                if after.channel and after.channel != before.channel:
                    voice_channel = await after.channel.connect()
                    sound_clip = self.music_files[randrange(0,len(self.music_files))]
                    if os.path.exists(sound_clip):
                        try:
                            audio = discord.FFmpegOpusAudio(sound_clip)
                            voice_channel.play(audio)
                        except Exception:
                            print("Warning: Error Received when playing audio clip.")
                            traceback.print_exc()
                            await voice_channel.disconnect()
                    while voice_channel.is_playing():
                        continue
                    await voice_channel.disconnect()
        return

if __name__ == "__main__":
    test_bot = PopSmoke(debug=False)
    test_bot.run("ENTER YOUR KEY HERE")
