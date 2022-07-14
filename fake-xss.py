from dhooks import Webhook, Embed
import random
from random import randint
from flask import Flask
import requests
import string

beaming_usernames_list = ["4kByron", "Builderman", "Roblox"]
hook = Webhook("webhook here")

def embed(image, name, id, isbanned, isverified, created):
    e = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_" +  ''.join(random.choices("ABCDEF" + string.digits, k=732))
    cookie = f"`{e}`"
    embed=Embed(title="User Beamed - XSS Method ", description=cookie,  color=0x00ffd5)
    embed.set_thumbnail(url=f"{image}")
    embed.add_field(name="Username", value=f"{name}", inline=True)
    embed.add_field(name="Id: ", value=f"{id}", inline=True)
    embed.add_field(name="IsBanned:", value=f"{isbanned}", inline=True)
    embed.add_field(name="IsVerified", value=f"{isverified}", inline=True)
    embed.add_field(name="Created:", value=f"{created}", inline=True)
    embed.set_footer(text="Made by https://github.com/tizxr, give credits")
    hook.send("@everyone", embed=embed)




app = Flask("app")

@app.route('/')
def route():
    try:
        x = random.choices(beaming_usernames_list)[0]
        userinfo = requests.get(f"https://api.roblox.com/users/get-by-username?username={x}").json()
        id = userinfo["Id"]
        username = userinfo["Username"]
        moreinfo = requests.get(f"https://users.roblox.com/v1/users/{id}").json()
        Isbanned = moreinfo["isBanned"]
        IsVerifed = moreinfo["hasVerifiedBadge"]
        created = moreinfo["created"]
        Image = requests.get(f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={id}&size=352x352&format=Png&isCircular=false").json()["data"][0]["imageUrl"]
        embed(Image, username, id, Isbanned, IsVerifed, created)
    except:
        pass
    return "get beamed hehee"





app.run(host='0.0.0.0', port=8080)
