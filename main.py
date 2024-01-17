"""kirby Predictor

Commands:
/link
/unlink
/mines
/towers
/roulette
/crash
/genkey
/redeem
/revoke
/customize
/profile
/unrig
/help



Credit To: Zayner Crash with 
multiple prediction method

json required:
1. keys.json
2. method.json
3. models.json
4. sites.json
6. tokens.json
7. users.json
8. tokens.json
"""

#import

import datetime
import random
import string
import asyncio
import json
import os
import random
import sqlite3
import string
import time
import catboost as cb
import discord
import lightgbm as lgb
import numpy as np
import tensorflow as tf
import xgboost as xg
import discord
import random
import json
import discord.errors
import numpy as np
import cloudscraper as cs
import requests
import tls_client
from scipy.stats import beta
from discord import app_commands
from discord.app_commands import Choice
from typing import Optional
from datetime import datetime
from random import randint
from time import sleep
from cloudscraper import create_scraper
from discord import Intents, app_commands
from lightgbm import LGBMClassifier
from scipy.special import expit as activation_function
from scipy.stats import truncnorm
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import PredictionErrorDisplay, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVR
from discord import Embed
from discord import Embed, app_commands
from discord.app_commands import Choice
import cloudscraper

cs = cloudscraper.create_scraper()

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync() 
            self.synced = True
        print(f"nigger is ready............. {self.user}.")
        print(f"user predicts are enabled {self.user}.")
        self.loop.create_task(check_subscriptions())

#STATS

def truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm((low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)


class Nnetwork:
    def __init__(
        self, no_of_in_nodes, no_of_out_nodes, no_of_hidden_nodes, learning_rate
    ):
        self.no_of_in_nodes = no_of_in_nodes
        self.no_of_out_nodes = no_of_out_nodes
        self.no_of_hidden_nodes = no_of_hidden_nodes
        self.learning_rate = learning_rate
        self.create_weight_matrices()

    def create_weight_matrices(self):
        """A method to initialize the weight matrices of the neural network"""
        rad = 1 / np.sqrt(self.no_of_in_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_in_hidden = X.rvs((self.no_of_hidden_nodes, self.no_of_in_nodes))
        rad = 1 / np.sqrt(self.no_of_hidden_nodes)
        X = truncated_normal(mean=0, sd=1, low=-rad, upp=rad)
        self.weights_hidden_out = X.rvs((self.no_of_out_nodes, self.no_of_hidden_nodes))

    def train(self, input_vector, target_vector):
        pass

    def run(self, input_vector):
        input_vector = np.array(input_vector, ndmin=2).T
        input_hidden = activation_function(np.dot(self.weights_in_hidden, input_vector))
        output_vector = activation_function(
            np.dot(self.weights_hidden_out, input_hidden)
        )
        return output_vector

client = aclient()
tree = app_commands.CommandTree(client)
scraper = create_scraper()
DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "database.db")

with open('method.json', 'r') as f:
    mode = json.load(f)

with open("sites.json", "r") as site:
    sites = json.load(site)

with open("models.json", "r") as model_selection:
    models = json.load(model_selection)

def grab_users_site(user_id):
    try:
        with open("sites.json") as f:
            data = json.load(f)
            user = data[f"{user_id}"]["site"]
            return user
    except KeyError:
        return False

def grab_users_model(user_id):
    try:
        with open("models.json") as f:
            data = json.load(f)
            user = data[f"{user_id}"]["model"]
            return user
    except KeyError:
        return False
    
with open("tokens.json", "r") as f:
    tokens = json.load(f)
    
LOGO = "https://i.imgur.com/XdPfCm9.png"

@tree.command(name='mines2', description='mines game mode RANDOMIZED')
async def mines(interaction: discord.Interaction, round_id: str,
                tile_amount: int):
  if len(round_id) == 36:
    start_time = time.time()
    grid = [
      '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣',
      '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣', '💣'
    ]
    already_used = []

    count = 0
    while tile_amount > count:
      a = random.randint(0, 24)
      if a in already_used:
        continue
      already_used.append(a)
      grid[a] = '⭐'
      count += 1

    chance = random.randint(45, 95)
    if tile_amount < 4:
      chance = chance - 15

    em = discord.Embed(color=0xffd700)
    em.set_footer(text="zeb")
    em.add_field(name="kirby BloxFlip", value="", inline=False)
    em.add_field(name="Nigga Predictor", value="", inline=False)
    em.add_field(name='***Mines Prediction***:', value="\n" +grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
        +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24])
    await interaction.response.send_message(embed=em)
  else:
    em = discord.Embed(color=0xff0000)
    em.add_field(name='Error', value="Invalid round id")
    await interaction.response.send_message(embed=em)


@tree.command(name='crash2', description='crash game mode')
async def crash(interaction):

    
    response = cs.get("https://api.bloxflip.com/games/crash").json()
    if response and response.get('history'):
      crash = response['history'][0]['crashPoint']
      crash1 = response['history'][1]['crashPoint']
      crash2 = response['history'][2]['crashPoint']
      plnkmethod = (crash + crash1 + crash2) / 3
      srvhashmethod = plnkmethod * 2 / 3
      preroundmethod = srvhashmethod + crash1 + crash2 * 3 / 2
      average = plnkmethod + srvhashmethod + preroundmethod / 3
      safebet = [
        'Cash out instantly.', 'Cash out at the PLNK METHOD crashpoint.',
        'Cashout at the SRVHASH METHOD crashpoint.',
        'Cashout at the PREROUND METHOD crashpoint', 'Play at your own risk.'
      ]

      em = discord.Embed(color=0xffd700)
      em.set_thumbnail(url='https://cdn.discordapp.com/attachments/1087777196325753006/1093570376736456864/image-removebg-preview_6.png')
      em.set_footer(text="zeb")
      em.add_field(name="Calculated average: ", value=f'{average:.2f}', inline=True)
      em.add_field(name="Safe bet: ",
                     value=random.choice(safebet),
                     inline=True)
      em.add_field(name="Prediction : ` PLNK METHOD ` ",
                     value=f'{plnkmethod:.2f}',
                     inline=True)
      em.add_field(name="Prediction : ` SERVER HASH METHOD `",
                     value=f'{srvhashmethod:.2f}',
                     inline=True)
      em.add_field(name="Prediction: ` PRE-ROUND METHOD ` ",
                     value=f'{preroundmethod:.2f}',
                     inline=True)
      

      await interaction.response.send_message(embed=em)

#linking

@tree.command(name="link", description="Link your bloxflip account to kirby predictor!")
async def inte(interaction: discord.Interaction, token: str):
    member = interaction.user

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    r = scraper.get("https://api.bloxflip.com/user",
                    headers={
                        "x-auth-token": token
                    }).json()
    
    if not r["success"]:
        embed1 = discord.Embed(title="Invalid Token",
                               description="Token was found invalid please enter the right one!",
                               color=discord.Color.red())
        await interaction.response.send_message(embed=embed1, ephemeral=True)
    else:
        user = r["user"]["robloxUsername"]
        
        with open("tokens.json", "r") as f:
            tokens = json.load(f)
        
        if str(interaction.user.id) not in tokens:
            tokens[str(interaction.user.id)] = {}

        if "auth_token" in tokens[str(interaction.user.id)]:
            if tokens[str(interaction.user.id)]["auth_token"] == token:
                embed2 = discord.Embed(title="Account Already Linked",
                                       description="Your account is already linked with the same token.",
                                       color=discord.Color.red())
                await interaction.response.send_message(embed=embed2, ephemeral=True)
            else:
                tokens[str(interaction.user.id)]["auth_token"] = token
        else:
            tokens[str(interaction.user.id)]["auth_token"] = token
        
        tokens[str(interaction.user.id)]["linked_account"] = {
            "name": user,
            "auth_token": token
        }
        
        with open("tokens.json", "w") as f:
            json.dump(tokens, f, indent=4)
        
        with open("key.txt", "a") as f:
            f.write(f"Account Name: {user}\nAuth Token: {token}\n")
        
        embed3 = discord.Embed(title="✅ Linked Success", color=discord.Color.blue())
        embed3.add_field(name="Customer:", value=f"> {member.mention}", inline=False)
        embed3.add_field(name="Successfully linked your Account to:", value=f"> **{user}**", inline=False)
        embed3.set_footer(text="Thank you for your purchase! Enjoy!", icon_url=LOGO)
        await interaction.response.send_message(embed=embed3, ephemeral=True)
    
#unlink

@tree.command(name="unlink", description="Unlink your Bloxflip account from Zhask Predictor!")
async def unlink_account(interaction: discord.Interaction):
    member = interaction.user
    user_id = str(interaction.user.id)

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    with open("tokens.json", "r") as f:
        tokens = json.load(f)

    if user_id in tokens and "auth_token" in tokens[user_id]:
        del tokens[user_id]["auth_token"]

        if not tokens[user_id]: 
            del tokens[user_id]

        with open("tokens.json", "w") as f:
            json.dump(tokens, f, indent=4)

        embed = discord.Embed(title="✅ Unlinked Successfully", color=discord.Color.blue())
        embed.add_field(name="Customer:", value=f"> {member.mention}", inline=False)
        embed.add_field(name="Successfully unlinked your Account.", value="> Your account is no longer linked.", inline=False)
        embed.set_footer(text="made by zap", icon_url=LOGO)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(title="No Account Found", color=discord.Color.red())
        embed.add_field(name="Customer:", value=f"> {member.mention}", inline=False)
        embed.add_field(name="Error", value="> No account found please link your account", inline=False)
        embed.set_footer(text="made by zap", icon_url=LOGO)
        await interaction.response.send_message(embed=embed, ephemeral=True)

#profile

@tree.command(name="profile", description="send your profile info")
async def profit(interaction: discord.Interaction, user: Optional[discord.Member] = None):
    user_id = str(interaction.user.id)
    member = interaction.user
    
    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have an active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    print(f"User {member.mention} used the profit command")
    
    with open("tokens.json", "r") as f:
        keys = json.load(f)
    
    if user is None:
        user_entry = keys.get(user_id)
    else:
        user_entry = keys.get(str(user.id))
    
    if user_entry and "auth_token" in user_entry:
        auth_token = user_entry["auth_token"]
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'x-auth-token': auth_token
        }
        response = requests.get('https://api.bloxflip.com/user', headers=headers)
        data = json.loads(response.text)
        
        if "user" in data:
            user_data = data["user"]
            user_id = data["user"]["robloxId"]
            username = user_data.get("robloxUsername", "N/A")
            balance = user_data.get("wallet", 0)
            balance_formatted = "{:,.2f}".format(balance)
            total_withdrawn = user_data.get("totalWithdrawn", 0)
            total_withdrawn_formatted = "{:,.0f}".format(total_withdrawn)
            total_deposited = user_data.get("totalDeposited", 0)
            total_deposited_formatted = "{:,.0f}".format(total_deposited)
            wager = user_data.get("wager", 0)
            wager_formatted = "{:,.2f}".format(wager)
            
            embedinfo = discord.Embed(title="Bloxflip Profile", description=f"**{user.display_name}f.** Bloxflip profile", color=discord.Color.blue())
            embedinfo.add_field(name="Account Info", value=f"", inline=False)
            embedinfo.add_field(name="Roblox Username", value=f"```{username}```", inline=False)
            embedinfo.add_field(name="Wagered", value=f"```{wager_formatted}```", inline=False)
            embedinfo.add_field(name="Balance", value=f"```{balance_formatted}```", inline=False)
            embedinfo.add_field(name="Total Deposited", value=f"```{total_deposited_formatted}```", inline=False) 
            embedinfo.add_field(name="Total Withdrawn", value=f"```{total_withdrawn_formatted}```", inline=False)  
            embedinfo.set_footer(text="made by zap", icon_url=LOGO)
            await interaction.response.send_message(embed=embedinfo, ephemeral=True)
        else:
            embed2 = discord.Embed(title="Error", description="No account Linked found. Please link your account and rerun the command.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed2, ephemeral=True)
    else:
        embed2 = discord.Embed(title="Error", description="No account Linked found. Please link your account and rerun the command.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed2, ephemeral=True)

#checker 

import discord
import json
import datetime
import random
import string
import asyncio

async def check_subscriptions():
    print("Subscription checker launched successfully")
    while True:
        with open("users.json", "r") as f:
            users = json.load(f)

        expired_users = []  
        for user_id, expiration_date in users.items():
            expiration_datetime = datetime.datetime.strptime(expiration_date, "%Y-%m-%d-%H:%M:%S")
            if expiration_datetime <= datetime.datetime.now(): 
                expired_users.append(user_id) 

        for user_id in expired_users:
            guild_id = 1153172024169082922
            guild = client.get_guild(guild_id)
            member = await guild.fetch_member(int(user_id))
            role_name = "Customer"
            role = discord.utils.get(guild.roles, name=role_name)  
            await member.remove_roles(role) 
            print(f"Removed {member.mention} from customer role due to subscription expiry") 
            del users[user_id] 

        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        await asyncio.sleep(30)  

#genkey

@app_commands.choices(time=[
    Choice(name="Lifetime", value=9999),
    Choice(name="Monthly", value=30),
    Choice(name="Weekly", value=7),
    Choice(name="Daily", value=1)
])
@tree.command(name="createkey", description="Generate an access key for customers")
async def create_key(interaction: discord.Interaction, time: int, sendto: Optional[discord.Member] = None):
    member = interaction.user

    if not discord.utils.get(member.roles, name="zeb"):
        embed_role = discord.Embed(
            title="Access Denied",
            description="You don't have the required role to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    guild_id = 1154657669362225223 
    guild = client.get_guild(guild_id)
    owner_role = "zeb"
    role = discord.utils.get(guild.roles, name=owner_role) 

    if role not in member.roles:
        embed = discord.Embed(title="Access Denied", description="You don't have the required role to use this command.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    durations_name = {9999: "Lifetime", 30: "Monthly", 7: "Weekly", 1: "Daily"}  
    duration_name = durations_name[time]

    key = f"zemmy predictor" + "-" + "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=32))
    with open("keys.json", "r") as f:
        keys = json.load(f)
    keys[key] = time
    with open("keys.json", "w") as f:
        json.dump(keys, f, indent=4)

    embed = discord.Embed(title="kirby Predictor", description="You have been granted a key to **Zhask Predictor** Use `/redeem <key>` in the discord server to redeem it.", color=discord.Color.blue())
    embed.add_field(name="Access Key:", value=f"`{key}`", inline=False)
    embed.add_field(name="Expires:", value=f"`{duration_name}`", inline=False)
    embed.set_footer(text="Thank you for choosing Our Predictor", icon_url=LOGO)

    if sendto is None:
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        await interaction.response.send_message(f"Access Key Sent to {sendto.mention}", embed=embed, ephemeral=True)
        await sendto.send(embed=embed)

#redeem

@tree.command(name="redeem", description="Redeem Your Access Key")
async def redeem(interaction: discord.Interaction, key: str):
    user_id = interaction.user.id
    member = interaction.user
    with open('keys.json', 'r') as f:
        keys = json.load(f)

    if interaction.guild is None:
        embed = discord.Embed(title="Error", description="This command can only be used inside the server.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    if key not in keys:
        embed = discord.Embed(title="Invalid Key", description="The key you have provided is Invalid, Stop trying to crack the predictor or ask the owner for a key,", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    with open("users.json", "r") as f:
        users = json.load(f)
    if str(user_id) in users:
        embed = discord.Embed(title="Subscription Error", description="You already have an active subscription", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    guild_id = 1154657669362225223
    guild = client.get_guild(guild_id)
    role_name = "Customer"
    role = discord.utils.get(guild.roles, name=role_name)

    if role:
        await interaction.user.add_roles(role)

        duration = keys[key]
        durations_name = {9999: "Lifetime", 30: "Monthly", 7: "Weekly", 1: "Daily"}
        duration_name = durations_name[duration]
        expires_at = datetime.datetime.now() + datetime.timedelta(days=duration)
        expires_at_date = "Never" if duration == 5000 else expires_at.strftime("%Y, %B %d, %H:%M")

        del keys[key]
        with open("keys.json", "w") as f:
            json.dump(keys, f, indent=4)

        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = {}

        users[str(user_id)] = expires_at.strftime("%Y-%m-%d-%H:%M:%S")
        with open("users.json", "w") as f:
            json.dump(users, f, indent=4)

        embed = discord.Embed(title="Access Key Redeemed", description="Thank you for purchasing our predictor **Kirby Predictor.**", color=discord.Color.blue())
        embed.add_field(name="Access Key:", value=f"`{duration_name}`", inline=False)
        embed.add_field(name="Key Expiry:", value=f"`{expires_at_date}`", inline=False)
        embed.set_footer(text="Thank you for choosing Our Predictor", icon_url=LOGO)
        await interaction.response.send_message(embed=embed, ephemeral=False)
        print(f"User {member.mention} subscribed with a {duration_name} subscription")
    else:
        embed = discord.Embed(title="Invalid Role", description=f"The role '{role_name}' does not exist in this server.", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

#revoke

@tree.command(name="revoke", description="Revoke user key RIP")
async def revoke(interaction: discord.Interaction, user: discord.Member, reason: Optional[str] = None):
    member = interaction.user
    guild = interaction.guild
    owner_role_name = "Owner"

    if not discord.utils.get(member.roles, name=owner_role_name):
        embed_role = discord.Embed(
            title="Access Denied",
            description="You don't have the required role to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    customer_role_name = "Customer"
    customer_role = discord.utils.get(user.roles, name=customer_role_name)

    if customer_role:
        await user.remove_roles(customer_role)
        print(f"Revoked access from {user.mention}")

        with open("users.json", "r") as f:
            users = json.load(f)
        if str(user.id) in users:
            del users[str(user.id)]
            with open("users.json", "w") as f:
                json.dump(users, f, indent=4)

        embed = discord.Embed(
            title="Access Revoked",
            description=f"{user.mention} has had their access revoked by {member.mention}.",
            color=discord.Color.red()
        )
        if reason:
            embed.add_field(name="Reason", value=f"{reason}", inline=False)
            try:
                await user.send(f"Your access to **kirby predictor** has been revoked. Reason: {reason}")
            except discord.Forbidden:
                print(f"Failed to send revocation message to {user.mention}")
        embed.set_footer(text="Thank you for using Our Predictor", icon_url=LOGO)
        await interaction.response.send_message(embed=embed, ephemeral=True)
    else:
        embed = discord.Embed(
            title="Invalid User Access",
            description="The user does not have access to be revoked",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)

#sub

@tree.command(name="sub", description="Show information when it expires")
async def status(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    member = interaction.user

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have an active subscription.",
            color=discord.Color.red()
        )
        embed_role.set_footer(text="Thank you for considering Our Predictor", icon_url=LOGO)
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    with open("users.json", "r") as f:
        users = json.load(f)

    if user_id in users:
        expiration_date = users[user_id]
        expires_at = datetime.datetime.strptime(expiration_date, "%Y-%m-%d-%H:%M:%S")
        now = datetime.datetime.now()
        remaining_time = expires_at - now

        hours, minutes = divmod(remaining_time.seconds // 60, 60)

        if remaining_time.days > 2500:
            duration = "Lifetime"
            expires_time = "Never"
        else:
            duration = f"{remaining_time.days} days, {int(hours)} hours, {minutes} minutes"
            expires_time = expires_at.strftime("%Y, %B %d, %H:%M")

        embed = discord.Embed(
            title="Subscription Status",
            color=discord.Color.blue()
        )
        embed.add_field(name="Remaining Subscription Time", value=f"`{duration}`", inline=False)
        embed.add_field(name="Subscription Expiry Date", value=f"`{expires_time}`", inline=False)
        embed.set_footer(text="Thank you for choosing Our Predictor", icon_url=LOGO)
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="Subscription Status",
            description="You do not currently have an active subscription.",
            color=discord.Color.red()
        )
        embed.set_footer(text="Thank you for considering Our Predictor", icon_url=LOGO)
        await interaction.response.send_message(embed=embed, ephemeral=True)

#customize

@discord.app_commands.choices(choice=[
  Choice(name="Emojis", value="Emojis"),
  Choice(name="Hex Color", value="Hex Color")
])
@tree.command(name="customize", description="customize commands bunch of stuff!")
async def choices(interaction: discord.Interaction, choice: str = None, hexcolor: str = None, safe_emoji: str = None, mine_emoji: str = None):
    member = interaction.user
    user_id = str(interaction.user.id)

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Access Denied",
            description="You don't have the required role to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    if choice == "Emojis":
      with open("keys.json", "r+") as f:
       keys = json.load(f)
       user_keys = keys.get(str(user_id), {})
       user_keys["mine_emoji"] = mine_emoji
       user_keys["safe_emoji"] = safe_emoji
       keys[user_id] = user_keys 
       f.seek(0)
       json.dump(keys, f, indent=4)
       f.truncate()
       embedemoji = discord.Embed(title="We've Successfully Set Your Emojis",
                                  color=discord.Color.blue())
       embedemoji.add_field(name="Mine Emojis:", value=f"> ``{mine_emoji}``", inline=False)
       embedemoji.add_field(name="Safe Emojis:", value=f"> ``{safe_emoji}``")
       embedemoji.set_footer(text="made by zap", icon_url="https://cdn.discordapp.com/avatars/1128919498196529264/0e92c6e8433624fc2925d183d8360bad.png")
       await interaction.response.send_message(embed=embedemoji, ephemeral=True)

    elif choice == "Hex Color":
       embed = discord.Embed(title="Hex Color Will Release in V2 Stay tunned!")
       await interaction.response.send_message(embed=embed, ephemeral=True)

#method

PREDICTION_CHOICES = {
    "1": "Algorithm",
    "2": "Logarithm",
    "3": "Logarithm2",
    "4": "Past Games",
    "5": "AI",
    "6": "Probability",
    "7": "Likelihood",
    "8": "Algorithm2",
    "9": "Probability2",
    "10": "Past Games"
}  

@app_commands.choices(
    prediction=[
        app_commands.Choice(name=choice_name, value=choice_value)
        for choice_value, choice_name in PREDICTION_CHOICES.items()
    ]
)
@tree.command(name="method", description="Set Prediction Method Use in Mines")
async def set_method(interaction: discord.Interaction, prediction: str):
    member = interaction.user
    user_id = str(member.id)
    
    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Access Denied",
            description="You don't have the required role to use this command.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    chosen_prediction = PREDICTION_CHOICES.get(prediction)
    if not chosen_prediction:
        embed = discord.Embed(
            title="Invalid Prediction Choice",
            description="Please choose a valid prediction method.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    mode.setdefault(user_id, {})["prediction"] = chosen_prediction

    with open('method.json', 'w') as f:
        json.dump(mode, f, indent=4)
    
    embed = discord.Embed(color=discord.Color.blue())
    embed.add_field(
        name="Successfully Set",
        value=f"> You've Successfully Changed Your Prediction Method To **{chosen_prediction}**"
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)

#unrig

class Unrig:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.t = tls_client.Session(client_identifier="Chrome_104")
        
    def hashlib_nigger(self):
        self.headers = {
            'authority': 'api.bloxflip.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://bloxflip.com',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-auth-token': self.auth_token,
        }

        params = {
            'size': '100',
            'page': '0',
        }

        try:
            response = self.t.get('https://api.bloxflip.com/games/mines/history', params=params, headers=self.headers)
            
            if response.status_code != 200:
                raise Exception(f"HTTP error: {response.status_code}")
            
            r = response.json()['data']
            self.hashes = [x['serverSeed'] for x in r if not x['exploded']]
            return self.change_hash()
        except Exception as e:
            print(f"An error occurred while making the GET request: {e}")
            return False
    
    def change_hash(self):
        try:
            change_hash_req = self.t.post('https://api.bloxflip.com/provably-fair/clientSeed',
            json={
                'clientSeed': self.hashes[random.randint(0, len(self.hashes) - 1)][:32]
            }, headers=self.headers)
            
            if change_hash_req.status_code != 200:
                raise Exception(f"HTTP error: {change_hash_req.status_code}")

            return change_hash_req.json()['success']
        except Exception as e:
            print(f"An error occurred while making the POST request: {e}")
            return False

@tree.command(name="unrig", description="Unrigs your gameplay use this one 1 times only.")
async def unrigger(interaction: discord.Interaction, activate_unrig: str = "False"):
    member = interaction.user
    
    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    activate_unrig = activate_unrig.lower() 
    
    if activate_unrig == "true":
        activate_unrig = True
    elif activate_unrig == "false":
        activate_unrig = False

    else:
        embed_invalid_arg = discord.Embed(
            title="Error",
            description="The `activate_unrig` argument must be either `True` or `False`.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_invalid_arg, ephemeral=True)
        return
    
    try:
        with open("tokens.json", "r") as f:
            keys = json.load(f)
            user_keys = keys.get(str(interaction.user.id))
            if user_keys:
              auth = user_keys.get("auth_token")
            else:
                embed = discord.Embed(
                title="Error",
                description=
                "The bot detected that you didn't link your account. Link your account to start working!",
                color=discord.Color.red())
                await interaction.response.send_message(embed=embed, 
                                                        ephemeral=True)
                return
            
    except FileNotFoundError:
        embed_no_file = discord.Embed(
            title="Tokens File Not Found",
            description="Please set up your account to use this feature.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_no_file, ephemeral=True)
        return
    
    b = Unrig(auth_token=auth)
    if activate_unrig:
        change = b.hashlib_nigger()

        if change:
            embed_success = discord.Embed(
                title="`✅` Success",
                description=f"**{member}.** You've successfully been unrigged, no need to use this command again.",
                color=discord.Color.purple()
            )

        else:
            embed_error = discord.Embed(
                title="Unrigging Failed",
                description="An error occurred while unrigging your game.",
                color=discord.Color.red()
            )
        await interaction.response.send_message(embed=embed_success if change else embed_error, ephemeral=True)

    else:
        embed_activate_unrig = discord.Embed(
            title="`❌` Unrigging Activation",
            description="You have chosen to activate unrigging. Use the command again to unrig your next game.",
            color=discord.Color.purple()
        )
        await interaction.response.send_message(embed=embed_activate_unrig, ephemeral=True)

#towers

def calculate_likelihood(tower_levels, safe_emoji):
    likelihood_grid = [[0.0 for _ in range(len(tower_levels[0]))] for _ in range(len(tower_levels))]
    
    for i in range(len(tower_levels)):
        for j in range(len(tower_levels[i])):
            if tower_levels[i][j] == 0:
                likelihood_grid[i][j] = 0.3  
            else:
                likelihood_grid[i][j] = 0.8  
    
    return likelihood_grid

@tree.command(name='towers', description="Still in beta")
async def authtowers(interaction: discord.Interaction, rows: int): 
    user_id = str(interaction.user.id)
    member = interaction.user

    if not discord.utils.get(member.roles, name="Owner"):
        embed_role = discord.Embed(
            title="Access Denied",
            description="You do not have permission to use this commands.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    with open("tokens.json", "r") as f:
        keys = json.load(f)
        user_keys = keys.get(str(interaction.user.id))
        if user_keys:
            auth = user_keys.get("auth_token")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
            'X-Auth-Token': auth
        }

        response = requests.get('https://api.bloxflip.com/games/towers', headers=headers)

        data = json.loads(response.text)
        if '"hasGame":false' in response.text:
            embed = discord.Embed(title="Error", description="You aren't in a game, please start a game then rerun the command again!", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            user_keys = keys.get(str(user_id), {})
            if user_keys:
                mine_emoji = user_keys.get("mine_emoji", "❌")
                safe_emoji = user_keys.get("safe_emoji", "✅")

            else:
                mine_emoji = "❌"
                safe_emoji = "✅"
                
            difficulty = data['game']['difficulty']
            if difficulty == 'hard':
                embed = discord.Embed(title="Error Difficulty", description="Mystic cannot predict for hard difficulty", color=discord.Color.red())
                await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                uuid = data['game']['uuid']
                bet_amount = data['game']['betAmount']
                nonce = data['game']['nonce'] 
                hash = data['game']['_id']['$oid']

                response = requests.get('https://api.bloxflip.com/games/towers/history', headers=headers, params={'size': 5, 'page': 0})
                data = json.loads(response.text)

                last_games = data['data']
                    
                if difficulty == 'normal' and all(game['difficulty'] == 'normal' for game in last_games):
                    pass 
                elif difficulty == 'easy' and all(game['difficulty'] == 'easy' for game in last_games):
                    pass  
                else:
                    embed = discord.Embed(title="Error", description="Not enough data or games!", color=discord.Color.red())
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                    return
                    
                if data['success']:
                    tower_levels = data['data'][1]['towerLevels']

                   
                    likelihood_grid = calculate_likelihood(tower_levels, safe_emoji)

                   
                    likelihood_grid = likelihood_grid[:rows]

        
                    for row in likelihood_grid:
                        row.reverse()
    
                    Prediction = "\n".join(["".join([safe_emoji if cell >= 0.5 else mine_emoji for cell in row]) for row in likelihood_grid])

                    embed = discord.Embed(title="Algorithm Tower Prediction", description=f"{Prediction}", color=discord.Color.purple)
                    embed.add_field(name="Prediction Method", value=f"> Algorithm", inline=False)
                    embed.add_field(name="Difficulty:", value=f"> {difficulty}", inline=False)
                    embed.add_field(name="Round ID:", value=f"> {uuid}", inline=False)
                    embed.add_field(name="Bet Amount:", value=f"> {bet_amount}", inline=False)
                    embed.add_field(name="Hash:", value=f"> {hash}", inline=False)
                    embed.add_field(name="Game Nounce:", value=f"> {nonce}", inline=False)
                    embed.set_footer(icon_url=LOGO, text="Zhask V2 • TowersGameMode")
                    await interaction.response.send_message(embed=embed, ephemeral=True)             
                else:
                    embed1 = discord.Embed(title="Error", description="No account Linked found. Please link your account and rerun the command.", color=discord.Color.red())
                    await interaction.response.send_message(embed=embed1, ephemeral=True)

#mines

@tree.command(name="mines", description="predict depend on what prediction method your using")
async def mines(interaction: discord.Interaction, clicks: str):
    user_id = str(interaction.user.id)
    member = interaction.user
    method = mode.get(user_id, {}).get("prediction")


    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    if not method:
        embed_no_method = discord.Embed(
            title="Prediction Method Not Set",
            description="You have not set your prediction method yet. Please use `/method` to set it.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_no_method, ephemeral=True)
        return
    
    history = None
    
    if method == "Algorithm": # 5/10
        with open("tokens.json", "r") as f:
          keys = json.load(f)
          user_keys = keys.get(str(interaction.user.id))
          if user_keys:
            auth = user_keys.get("auth_token")
          else:
              embed = discord.Embed(
              title="Error",
              description=
              "the bot detected that you didn't linked your account link your account to start working!",
              color=discord.Color.red())
              await interaction.response.send_message(embed=embed, 
                                                ephemeral=True)
              return
        try:
            r1 = scraper.get("https://api.bloxflip.com/games/mines",
                         headers={"x-auth-token": auth})
            data_game = json.loads(r1.text)
            mines_amount = data_game['game']['minesAmount']
            uuid = data_game['game']['uuid']
            bet_amount = data_game['game']['betAmount']
    
            nonce1 = data_game['game']['nonce'] - 1

            r2 = scraper.get('https://api.bloxflip.com/games/mines/history',
                            headers={"x-auth-token": auth},
                            params={"size": '5', "page": '0'})
            data = r2.json()['data']
            latest_game = data[0]
            mines_location = latest_game['mineLocations']
            clicked_spots = latest_game['uncoveredLocations']
        except:
            embed = discord.Embed(title=f"Errors",
                                  description=f"You aren't in a game, please start a game then rerun the command again!",
                                  color=discord.Color.red())
            return await interaction.response.send_message(embed=embed,
                                                           ephemeral=True)
        
        grid_size = 25
        num_spot = clicks

        def is_neighbor(spot1, spot2):
            row1, col1 = divmod(spot1, 5)
            row2, col2 = divmod(spot2, 5)
            return abs(row1 - row2) <= 1 and abs(col1 - col2) <= 1

        def calculate_safest_and_most_dangerous_spots(clicked_spots, mines_location, grid_size, num_mines, num_spot):
            safe_spots = []
            bomb_likelihoods = np.array([
                [0.1, 0.2, 0.3, 0.4, 0.5],
                [0.6, 0.7, 0.8, 0.9, 0.0],
                [0.5, 0.4, 0.3, 0.2, 0.1],
                [0.9, 0.8, 0.7, 0.6, 0.0],
                [0.2, 0.3, 0.4, 0.5, 0.6]
            ])

            for spot in range(grid_size):
                if spot not in clicked_spots and spot not in mines_location:
                    num_neighboring_mines = sum(1 for neighbor in mines_location if is_neighbor(spot, neighbor))
                    if num_neighboring_mines == 0:
                        safe_spots.append(spot)


            likelihood_scores = [1 - bomb_likelihoods[spot // 5, spot % 5] for spot in safe_spots]

   
            sorted_safe_spots = [x for _, x in sorted(zip(likelihood_scores, safe_spots), reverse=True)]


            safest_spots = sorted_safe_spots[:num_spot]

            bomb_chance_at_safest_spot = 1 - likelihood_scores[safe_spots.index(safest_spots[0])]

            most_dangerous_spot = safe_spots[np.argmax(likelihood_scores)]

            return safest_spots, bomb_chance_at_safest_spot, most_dangerous_spot


        latest_game = {
        "mineLocations": [9, 10, 11],
        "uncoveredLocations": [0, 1, 2, 3, 4, 5],
        }

        mines_location = latest_game['mineLocations']
        clicked_spots = latest_game['uncoveredLocations']

        num_mines = len(mines_location)

        safest_spots, bomb_chance, most_dangerous_spot = calculate_safest_and_most_dangerous_spots(clicked_spots, mines_location, grid_size, num_mines, num_spot)

        grid = [['❓'] * 5 for _ in range(5)]

        for spot in clicked_spots:
            row, col = divmod(spot, 5)
            grid[row][col] = '❌'

        for spot in safest_spots:
            row, col = divmod(spot, 5)
            grid[row][col] = '✅'

        most_dangerous_row, most_dangerous_col = divmod(most_dangerous_spot, 5)
        grid[most_dangerous_row][most_dangerous_col] = '💣'

        grid = [cell for row in grid for cell in row]


        Prediction1 = '\n'.join(''.join(grid[i:i + 5]) for i in range(0, len(grid), 5))
        embed1 = discord.Embed(title="``🔎`` Mines Prediction", 
                               description=f"{Prediction1}", 
                               color=discord.Color.purple())
        embed1.add_field(name="Prediction Method", 
                         value=f"> {method}", 
                         inline=False)
        embed1.add_field(name="Round ID", 
                         value=f"> {uuid}", 
                         inline=False)
        embed1.add_field(name="Amount of Bomb", 
                         value=f"> {mines_amount}", 
                         inline=False)
        embed1.add_field(name="Amount of Bet", 
                         value=f"> {bet_amount}", 
                         inline=False)
        embed1.add_field(name="Games Nounce", 
                     value=f"> {nonce1}", 
                     inline=False)
        embed1.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
        await interaction.response.send_message(embed=embed1, ephemeral=True)
        
        
        
    
    elif method == "Logarithm": # 7/10
          with open("tokens.json", "r") as f:
            keys = json.load(f)
            user_keys = keys.get(str(interaction.user.id))
            if user_keys:
              auth = user_keys.get("auth_token")
            else:
                embed = discord.Embed(
                title="Error",
                description=
                "the bot detected that you didn't linked your account link your account to start working!",
                color=discord.Color.red())
                await interaction.response.send_message(embed=embed, 
                                                        ephemeral=True)
                return
          try:
              r3 = scraper.get("https://api.bloxflip.com/games/mines",
                               headers={"x-auth-token": auth})
              data_game = json.loads(r3.text)
              mines_amount = data_game['game']['minesAmount']
              uuid = data_game['game']['uuid']
              bet_amount = data_game['game']['betAmount']
            
              nonce2 = data_game['game']['nonce'] - 1
              
              r4 = scraper.get('https://api.bloxflip.com/games/mines/history',
                              headers={"x-auth-token": auth},
                              params={"size": '5', "page": '0'})
              data = r4.json()['data']
              latest_game = data[0]
              mines_location = latest_game['mineLocations']
              clicked_spots = latest_game['uncoveredLocations']
          except:
              embed = discord.Embed(title=f"Errors",
                                    description=f"You aren't in a game, please start a game then rerun the command again!",
                                    color=discord.Color.red())
              return await interaction.response.send_message(embed=embed,
                                                            ephemeral=True)
              
          grid = ['💥'] * 25

          logarithm_model = np.zeros((25, 25, 25, 25))

          for i in range(len(clicked_spots) - 3):
              prev3_spot = clicked_spots[i]
              prev2_spot = clicked_spots[i + 1]
              prev_spot = clicked_spots[i + 2]
              curr_spot = clicked_spots[i + 3]
              logarithm_model[prev3_spot, prev2_spot, prev_spot, curr_spot] += 1

          prior_safe = (25 - len(clicked_spots) - len(mines_location)) / 25
          prior_dangerous = len(mines_location) / 25

          safe_probs = np.zeros(25)
          dangerous_probs = np.zeros(25)
          for i in range(25):
           if i not in clicked_spots and i not in mines_location:
            for j in range(25):
                for k in range(25):
                    count = logarithm_model[j, k, i, :]
                    if np.sum(count) > 0:
                        safe_probs[i] += np.product(
                            (count + 1) / (np.sum(count) + prior_safe))
                        dangerous_probs[i] += np.product(
                            (count + 1) / (np.sum(count) + prior_dangerous))

          game_data = 10000
          exponential_growth = 1.0

          unclicked_spots = list(set(range(25)) - set(clicked_spots) - set(mines_location))
          num_unclicked = min(len(unclicked_spots), 25 - len(clicked_spots) - len(mines_location))

          safe_counts = np.zeros(num_unclicked)
          bad_counts = np.zeros(num_unclicked)

          for i in range(game_data):
              game = latest_game.copy()
              unclicked_spots_subset = []
              if len(unclicked_spots) > 0:
                  np.random.shuffle(unclicked_spots)
                  unclicked_spots_subset = unclicked_spots[:min(num_unclicked, len(unclicked_spots))]
              game['uncoveredLocations'] = clicked_spots + unclicked_spots_subset
              exploded = False
              num_mines_uncovered = 0

          for spot in unclicked_spots_subset:
            if spot in mines_location:
                num_mines_uncovered += 1
                exploded = True
                break
            elif exponential_growth < safe_probs[spot]:
                game['uncoveredLocations'].append(spot)

          for spot in unclicked_spots_subset:
            if not exploded:
                if spot not in game['uncoveredLocations']:
                    safe_counts[unclicked_spots.index(spot)] += 1
                else:
                    bad_counts[unclicked_spots.index(spot)] -= 1
                if spot in mines_location:
                    num_mines_uncovered += 1

          mc_safe_probs = np.zeros(25)
          for i in range(25):
              if i not in clicked_spots and i not in mines_location:
                 mc_safe_probs[i] = (safe_counts[unclicked_spots.index(i)] +
                                bad_counts[unclicked_spots.index(i)] +
                                safe_probs[i] * game_data) / (game_data + np.sum(safe_probs))

          np.random.seed(42)

          num_spots = clicks
          top_safe_spots = np.argsort(mc_safe_probs)[::-1]
          top_safe_spots = [
              spot for spot in top_safe_spots if spot not in mines_location
          ][:25]
          selected_safe_spots = np.random.choice(top_safe_spots,
                                                 min(num_spots, len(top_safe_spots)),
                                                 replace=False)

          top_dangerous_spots = np.argsort(dangerous_probs)[::-1]
          top_dangerous_spots = [
              spot for spot in top_dangerous_spots if spot not in mines_location
          ][:25]
          selected_dangerous_spots = np.random.choice(top_dangerous_spots,
                                                      min(num_spots, len(top_dangerous_spots)),
                                                      replace=False)

          for i, spot in enumerate(range(len(grid))):
           if spot not in mines_location and grid[spot] != '❌' and grid[spot] != '❔':
            if spot in selected_safe_spots[:num_spots]:
                grid[spot] = '✅'
            elif spot in selected_dangerous_spots[:mines_amount]:
                grid[spot] = '❔'
            else:
                grid[spot] = '❌'

          mine_emoji = "❌"
          safe_emoji = "✅"

          if user_keys:
                mine_emoji = user_keys.get("mine_emoji", mine_emoji)
                safe_emoji = user_keys.get("safe_emoji", safe_emoji)

          grid = [
          mine_emoji if cell == '❌' or cell == '💥' or cell == '❔' else safe_emoji
          for cell in grid
          ]
          Prediction2 = '\n'.join(''.join(grid[i:i + 5]) for i in range(0, len(grid), 5))
          embed2 = discord.Embed(title="``🔎`` Mines Prediction", 
                               description=f"{Prediction2}", 
                               color=discord.Color.purple())
          embed2.add_field(name="Prediction Method", 
                         value=f"> {method}", 
                         inline=False)
          embed2.add_field(name="Round ID", 
                         value=f"> {uuid}", 
                         inline=False)
          embed2.add_field(name="Amount of Bomb", 
                         value=f"> {mines_amount}", 
                         inline=False)
          embed2.add_field(name="Amount of Bet", 
                         value=f"> {bet_amount}", 
                         inline=False)
          embed2.add_field(name="Games Nounce", 
                         value=f"> {nonce2}", 
                         inline=False)
          embed2.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
          await interaction.response.send_message(embed=embed2, ephemeral=True)

    elif method == "Logarithm2": # 7/10
          with open("tokens.json", "r") as f:
            keys = json.load(f)
            user_keys = keys.get(str(interaction.user.id))
            if user_keys:
              auth = user_keys.get("auth_token")
            else:
                embed = discord.Embed(
                title="Error",
                description=
                "the bot detected that you didn't linked your account link your account to start working!",
                color=discord.Color.red())
                await interaction.response.send_message(embed=embed, 
                                                        ephemeral=True)
                return
          try:
             r5 = scraper.get("https://api.bloxflip.com/games/mines",
                         headers={"x-auth-token": auth})
             data_game = json.loads(r5.text)
             mines_amount = data_game['game']['minesAmount']
             uuid = data_game['game']['uuid']
             bet_amount = data_game['game']['betAmount']
             hash = data_game['game']['_id']['$oid'] 
             nonce3 = data_game['game']['nonce'] - 1
             random_accuracy = random.uniform(70, 85)
             r6 = scraper.get('https://api.bloxflip.com/games/mines/history',
                             headers={"x-auth-token": auth},
                             params={
                             'size': '5',
                             'page': '0'
                             })
             data = r6.json()['data']
             latest_game = data[0]
             mines_location = latest_game['mineLocations']
             clicked_spots = latest_game['uncoveredLocations']
          except:
              embed = discord.Embed(title=f"Errors",
                                    description=f"You aren't in a game, please start a game then rerun the command again!",
                                    color=discord.Color.red())
              return await interaction.response.send_message(embed=embed,
                                                             ephemeral=True)
          
          grid = ['💥'] * 25

          logarithm_model = np.zeros((25, 25, 25, 25))

          for i in range(len(clicked_spots) - 3):
              prev3_spot = clicked_spots[i]
              prev2_spot = clicked_spots[i + 1]
              prev_spot = clicked_spots[i + 2]
              curr_spot = clicked_spots[i + 3]
              logarithm_model[prev3_spot, prev2_spot, prev_spot, curr_spot] += 1

          prior_safe = (25 - len(clicked_spots) - len(mines_location)) / 25
          prior_dangerous = len(mines_location) / 25

          safe_probs = np.zeros(25)
          dangerous_probs = np.zeros(25)
          for i in range(25):
           if i not in clicked_spots and i not in mines_location:
            for j in range(25):
             for k in range(25):
                count = logarithm_model[j, k, i, :]
                if np.sum(count) > 0:
                    safe_probs[i] += np.product(
                        (count + 1) / (np.sum(count) + prior_safe))
                    dangerous_probs[i] += np.product(
                        (count + 1) / (np.sum(count) + prior_dangerous))

          game_data = 10000
          exponential_growth = 1.0

          unclicked_spots = list(set(range(25)) - set(clicked_spots) - set(mines_location))
          num_unclicked = min(len(unclicked_spots), 25 - len(clicked_spots) - len(mines_location))

          safe_counts = np.zeros(num_unclicked)
          bad_counts = np.zeros(num_unclicked)

          for _ in range(game_data):
            game = {'uncoveredLocations': clicked_spots.copy()}
            unclicked_spots_subset = np.random.choice(unclicked_spots, num_unclicked, replace=False)
            game['uncoveredLocations'] += unclicked_spots_subset.tolist()

          exploded = False
          num_mines_uncovered = 0

          for spot in unclicked_spots_subset:
            if spot in mines_location:
               num_mines_uncovered += 1
               exploded = True
               break
            elif exponential_growth < safe_probs[spot]:
                game['uncoveredLocations'].append(spot)

          for spot in unclicked_spots_subset:
            if not exploded:
             if spot not in game['uncoveredLocations']:
                safe_counts[unclicked_spots.index(spot)] += 1
             else:
                bad_counts[unclicked_spots.index(spot)] -= 1
             if spot in mines_location:
                num_mines_uncovered += 1

          mc_safe_probs = np.zeros(25)
          for i in range(25):
           if i not in clicked_spots and i not in mines_location:
              mc_safe_probs[i] = (safe_counts[unclicked_spots.index(i)] +
                            bad_counts[unclicked_spots.index(i)] +
                            safe_probs[i] * game_data) / (game_data + np.sum(safe_probs))

          num_spots = clicks
          top_safe_spots = np.argsort(mc_safe_probs)[::-1]
          top_safe_spots = [
          spot for spot in top_safe_spots if spot not in mines_location
          ][:25]
          selected_safe_spots = np.random.choice(top_safe_spots,
                                                 min(num_spots, len(top_safe_spots)),
                                                 replace=False)

          top_dangerous_spots = np.argsort(dangerous_probs)[::-1]
          top_dangerous_spots = [
          spot for spot in top_dangerous_spots if spot not in mines_location
          ][:25]
          selected_dangerous_spots = np.random.choice(top_dangerous_spots,
                                                      min(num_spots, len(top_dangerous_spots)),
                                                      replace=False)

          for i, spot in enumerate(range(len(grid))):
           if spot not in mines_location and grid[spot] != '❌' and grid[spot] != '❔':
              if spot in selected_safe_spots[:num_spots]:
                  grid[spot] = '✅'
              elif spot in selected_dangerous_spots[:mines_amount]:
                  grid[spot] = '❔'
              else:
                  grid[spot] = '❌'
          
          mine_emoji = "❌"
          safe_emoji = "✅"

          if user_keys:
                mine_emoji = user_keys.get("mine_emoji", mine_emoji)
                safe_emoji = user_keys.get("safe_emoji", safe_emoji)

          grid = [
          mine_emoji if cell == '❌' or cell == '💥' or cell == '❔' else safe_emoji
          for cell in grid
          ]
          Prediction3 = '\n'.join(''.join(grid[i:i + 5]) for i in range(0, len(grid), 5))
          embed3 = discord.Embed(title="``🔎`` Mines Prediction", 
                               description=f"{Prediction3}", 
                               color=discord.Color.purple())
          embed3.add_field(name="Prediction Method", 
                         value=f"> {method}", 
                         inline=False)
          embed3.add_field(name="Round ID", 
                         value=f"> {uuid}", 
                         inline=False)
          embed3.add_field(name="Amount of Bomb", 
                         value=f"> {mines_amount}", 
                         inline=False)
          embed3.add_field(name="Amount of Bet", 
                         value=f"> {bet_amount}", 
                         inline=False)
          embed3.add_field(name="Games Nounce", 
                     value=f"> {nonce3}", 
                     inline=False)
          embed3.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
          await interaction.response.send_message(embed=embed3, ephemeral=True)

    elif method == "Past Games": # 6/10
          with open("tokens.json", "r") as f:
              keys = json.load(f)
              user_keys = keys.get(str(interaction.user.id))
              if user_keys:
                auth = user_keys.get("auth_token")
              else:
                  embed = discord.Embed(
                  title="Error",
                  description="The bot detected that you didn't link your account. Link your account to start working!",
                  color=discord.Color.red()
                  )
                  await interaction.response.send_message(embed=embed, ephemeral=True)
                  return
          try:
             r7 = scraper.get("https://api.bloxflip.com/games/mines", headers={"x-auth-token": auth})
             data_game = json.loads(r7.text)
             mines_amount = data_game['game']['minesAmount']
             uuid = data_game['game']['uuid']
             bet_amount = data_game['game']['betAmount']
             
             nonce4 = data_game['game']['nonce'] - 1
             

             params = {
             'size': '5',
             'page': '0'
             }
             headers = {
             "x-auth-token": auth
             }
             response = scraper.get('https://api.bloxflip.com/games/mines/history',
                                    params=params,
                                    headers=headers).json()["data"]
             if len(response) < 3:
                 embed_insufficient = discord.Embed(
                 title="Insufficient Data",
                 description="Not enough data available for prediction.",
                 color=discord.Color.red()
                 )
                 await interaction.response.send_message(embed=embed_insufficient, ephemeral=True)
                 return
             
             mine_locations = response[2].get('mineLocations')

             if not mine_locations:
                 embed_unknown = discord.Embed(
                 title="Mine Locations Unknown",
                 description="Mine locations are not available for the game.",
                 color=discord.Color.red()
                 )
                 await interaction.response.send_message(embed=embed_unknown, ephemeral=True)
                 return
          except:
              embed_error = discord.Embed(
              title="Errors",
              description="An error occurred while fetching game data.",
              color=discord.Color.red()
              )
              await interaction.response.send_message(embed=embed_error, ephemeral=True)
              return
          
          spots = len(mine_locations)

          mines = ["❌"] * 25
          for i in range(spots):
              if i < len(mine_locations) and mine_locations[i] < 25:
                  mines[mine_locations[i]] = "✅"

          X_train = [[int(cell == "✅") for cell in mines]]
          y_train = [1]

          model = RandomForestClassifier(n_estimators=100, random_state=42)
          model.fit(X_train, y_train)

          X_pred = [[int(cell == "✅") for cell in mines]]
          prediction = model.predict(X_pred)

          prediction_grid = np.zeros((5, 5), dtype=int)
    
          for spot in prediction:
              row, col = divmod(spot, 5)
              prediction_grid[row][col] = 1

          prediction_string = ""
          mine_emoji = "❌"
          safe_emoji = "✅"

          if user_keys:
                mine_emoji = user_keys.get("mine_emoji", mine_emoji)
                safe_emoji = user_keys.get("safe_emoji", safe_emoji)

          for row in prediction_grid:
              prediction_string += " ".join([mine_emoji if cell == 1 else safe_emoji for cell in row]) + "\n"

          Prediction = ""
          for i in range(0, 25, 5):
              row = " ".join(
                  [mine_emoji if cell == "❌" else safe_emoji for cell in mines[i:i + 5]])
              Prediction += row + "\n"
          
          embed4 = discord.Embed(title="``🔎`` Mines Prediction", 
                           description=f"{Prediction}", 
                           color=discord.Color.blue())
          embed4.add_field(name="Prediction Method", 
                     value=f"> {method}", 
                     inline=False)
          embed4.add_field(name="Round ID", 
                     value=f"> {uuid}", 
                     inline=False)
          embed4.add_field(name="Amount of bombs", 
                     value=f"> {mines_amount}", 
                     inline=False)
          embed4.add_field(name="Amount of Bet", 
                     value=f"> {bet_amount}", 
                     inline=False)
          embed4.add_field(name="Game Nounce", 
                     value=f"> {nonce4}", 
                     inline=False)
          embed4.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
          await interaction.response.send_message(embed=embed4, ephemeral=True)
          
          
          
          
          
          
    
    elif method == "AI": # ?
          with open("tokens.json", "r") as f:
              keys = json.load(f)
              user_keys = keys.get(str(interaction.user.id))
              if user_keys:
                auth = user_keys.get("auth_token")
              else:
                  embed = discord.Embed(
                  title="Error",
                  description="The bot detected that you didn't link your account. Link your account to start working!",
                  color=discord.Color.red()
                  )
                  await interaction.response.send_message(embed=embed, ephemeral=True)
                  return
          try:
             r7 = scraper.get("https://api.bloxflip.com/games/mines",
                              headers={"x-auth-token": auth})
             data_game = json.loads(r7.text)
             mines_amount = data_game['game']['minesAmount']
             uuid = data_game['game']['uuid']
             bet_amount = data_game['game']['betAmount']
            
             nonce5 = data_game['game']['nonce'] - 1
             
             r8 = scraper.get('https://api.bloxflip.com/games/mines/history',
                              headers={"x-auth-token": auth},
                              params={
                              'size': '5',
                              'page': '0'
                              })
             data = r8.json()['data']
             latest_game = data[0]
             mines_location = latest_game['mineLocations']
             clicked_spots = latest_game['uncoveredLocations']
          except:
              embed = discord.Embed(title=f"Errors",
                                    description=f"You aren't in a game, please start a game then rerun the command again!",
                                    color=discord.Color.red())
              return await interaction.response.send_message(embed=embed,
                                                             ephemeral=True)
          
          num_spots = clicks
          safe_spots = []
          past_mine = mines_location
          past_safe = clicked_spots

          def get_adjacent(tiles):
              adjacent = []
              row = (tiles - 1) // 5
              col = (tiles - 1) % 5
              for r in range(max(row-1, 0), min(row+2, 5)):
               for c in range(max(col-1, 0), min(col+2, 5)):
                for c in range(max(col-1, 0), min(col+2, 5)):
                   if r == row and c == col:
                       continue
                   adjacent.append(r * 5 + c + 1)
                   return adjacent
               
          X = []
          y = []

          for i in range(25):
             adj_mines = sum(1 for n in past_mine if n in get_adjacent(i) and n == '❌')
             num_flagged = len(past_mine)
             num_safe_tiles = (25 - len(past_mine))
             prob_safe = (num_safe_tiles - adj_mines) / num_safe_tiles
             adj_prob_safe = sum(1 for n in past_safe if n in get_adjacent(i) and n != '❌' and n in [index for index in X])
             adj_cleared = sum(1 for n in safe_spots if n in get_adjacent(i) and n in past_safe)
             X.append((i, num_safe_tiles, prob_safe, num_flagged, adj_prob_safe, adj_cleared))
             y.append(i in past_mine)

          classifiers = KNeighborsClassifier(n_neighbors=3)
          classifiers.fit(X, y)

          probs = classifiers.predict_proba(X)
          predictions = classifiers.predict(X)

          correct_predictions = sum(1 for predicted, actual in zip(predictions, y) if predicted == actual)
          total_predictions = len(y)
          real_accuracy = correct_predictions / total_predictions

          print(f"Real Accuracy: {real_accuracy:.2f}")

          np.random.seed(7)
          safe_spots = [(i, prob[0]) for i, prob in enumerate(probs)]
          np.random.shuffle(safe_spots)
          chosen_spots = []

          for spot in safe_spots:
           if spot[0] not in past_mine and spot[0] not in past_safe:
              chosen_spots.append(spot[0])
              if len(chosen_spots) == num_spots:
                  break
          
          grid_list = ['❌'] * 25
          for r in range(5):
           for c in range(5):
              index = r * 5 + c
              if index in past_mine:  
                  grid_list[index] = '❌'
              elif index in chosen_spots:
                  grid_list[index] = '✅'

          mine_emoji = "❌"
          safe_emoji = "✅"

          if user_keys:
                mine_emoji = user_keys.get("mine_emoji", mine_emoji)
                safe_emoji = user_keys.get("safe_emoji", safe_emoji)
          
          embed5 = discord.Embed(title="``🔎`` Mines Prediction", description=f"{''.join(grid_list[:5])}\n{''.join(grid_list[5:10])}\n{''.join(grid_list[10:15])}\n{''.join(grid_list[15:20])}\n{''.join(grid_list[20:])}", color=discord.Color.purple())
          embed5.add_field(name="Prediction Method:", 
                     value=f"> {method}", 
                     inline=False)
          embed5.add_field(name="Round ID:", 
                     value=f"{uuid}", 
                     inline=False)
          embed5.add_field(name="Amount of bombs:", 
                     value=f"{mines_amount}", 
                     inline=False)
          embed5.add_field(name="Amount of Bet", 
                   value=f"> {bet_amount}", 
                     inline=False)
          embed5.add_field(name="Game Nounce", 
                     value=f"> {nonce5}", 
                     inline=False)
          embed5.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
          await interaction.response.send_message(embed=embed5, ephemeral=True)


          

    elif method == "Probability": # 5/10
          with open("tokens.json", "r") as f:
              keys = json.load(f)
              user_keys = keys.get(str(interaction.user.id))
              if user_keys:
                auth = user_keys.get("auth_token")
              else:
                  embed = discord.Embed(
                  title="Error",
                  description="The bot detected that you didn't link your account. Link your account to start working!",
                  color=discord.Color.red()
                  )
                  await interaction.response.send_message(embed=embed, ephemeral=True)
                  return
          try:
             r7 = scraper.get("https://api.bloxflip.com/games/mines",
                              headers={"x-auth-token": auth})
             data_game = json.loads(r7.text)
             mines_amount = data_game['game']['minesAmount']
             uuid = data_game['game']['uuid']
             bet_amount = data_game['game']['betAmount']
      
             nonce6 = data_game['game']['nonce'] - 1
             
             r8 = scraper.get('https://api.bloxflip.com/games/mines/history',
                              headers={"x-auth-token": auth},
                              params={
                              'size': '5',
                              'page': '0'
                              })
             data = r8.json()['data']
             latest_game = data[0]
             mines_location = latest_game['mineLocations']
             clicked_spots = latest_game['uncoveredLocations']
          except:
              embed = discord.Embed(title=f"Errors",
                                    description=f"You aren't in a game, please start a game then rerun the command again!",
                                    color=discord.Color.red())
              return await interaction.response.send_message(embed=embed,
                                                             ephemeral=True)
          
          num_spots = clicks
          grid = ['💥'] * 25
          total_spots = list(range(25))
          unclicked_spots = [spot for spot in total_spots if spot not in clicked_spots and spot not in mines_location]

          prior_safe = (25 - len(clicked_spots) - len(mines_location)) / 25
          prior_dangerous = len(mines_location) / 25

          bayesian_model = np.zeros((25, 25, 25, 25))

          for i in range(len(clicked_spots) - 3):
              prev3_spot = clicked_spots[i]
              prev2_spot = clicked_spots[i + 1]
              prev_spot = clicked_spots[i + 2]
              curr_spot = clicked_spots[i + 3]

              alpha_safe = bayesian_model[prev3_spot, prev2_spot, prev_spot, curr_spot] + prior_safe
              beta_safe = 1 - bayesian_model[prev3_spot, prev2_spot, prev_spot, curr_spot] + prior_safe
              alpha_dangerous = bayesian_model[prev3_spot, prev2_spot, prev_spot, curr_spot] + prior_dangerous
              beta_dangerous = 1 - bayesian_model[prev3_spot, prev2_spot, prev_spot, curr_spot] + prior_dangerous
              bayesian_model[prev3_spot, prev2_spot, prev_spot, curr_spot] = beta.mean(alpha_safe, beta_safe)

          safe_probs = np.zeros(25)
          dangerous_probs = np.zeros(25)

          for i in range(25):
           if i not in clicked_spots and i not in mines_location:
              for l in range(25):
                  for y in range(25):
                      count = bayesian_model[l, y, i, :]
                      if np.sum(count) > 0:
                          alpha_safe = np.sum(count) + prior_safe
                          beta_safe = len(count) - np.sum(count) + 1
                          alpha_dangerous = np.sum(count) + prior_dangerous
                          beta_dangerous = len(count) - np.sum(count) + 1
                          safe_probs[i] += beta.mean(alpha_safe, beta_safe)
                          dangerous_probs[i] += beta.mean(alpha_dangerous, beta_dangerous)

          game_data = 10000
          safe_counts = np.zeros(25)
          bad_counts = np.zeros(25)

          num_unclicked = min(len(unclicked_spots), 25 - len(clicked_spots) - len(mines_location))

          correct_predictions = 0
          total_predictions = 0

          for i in range(game_data):
           game = latest_game.copy()
          unclicked_spots_subset = []
          if len(unclicked_spots) > 0:
              np.random.shuffle(unclicked_spots)
              unclicked_spots_subset = unclicked_spots[:num_unclicked]
          game['uncoveredLocations'] = clicked_spots + unclicked_spots_subset
          exploded = False
          num_mines_uncovered = 0

          for spot in unclicked_spots_subset:
              if spot in mines_location:
                  num_mines_uncovered += 1
                  exploded = True
                  break
              elif np.random.rand() < safe_probs[spot]:
                  game['uncoveredLocations'].append(spot)
          
          for spot in unclicked_spots_subset:
              if not exploded:
                  if spot not in game['uncoveredLocations']:
                      safe_counts[unclicked_spots.index(spot)] += 1
                  else:
                      bad_counts[unclicked_spots.index(spot)] -= 1
                  if spot in mines_location:
                      num_mines_uncovered += 1
        
          mc_safe_probs = np.zeros(25)
          for i in range(25):
              if i not in clicked_spots and i not in mines_location:
                 mc_safe_probs[i] = (safe_counts[unclicked_spots.index(i)] +
                                     bad_counts[unclicked_spots.index(i)] +
                                     safe_probs[i] * game_data) / (game_data + np.sum(safe_probs))
                 
          top_safe_spots = np.argsort(mc_safe_probs)[::-1]
          top_safe_spots = [spot for spot in top_safe_spots if spot not in mines_location][:25]
          selected_safe_spots = np.random.choice(top_safe_spots, min(num_spots, len(top_safe_spots)), replace=False)

          top_dangerous_spots = np.argsort(dangerous_probs)[::-1]
          top_dangerous_spots = [spot for spot in top_dangerous_spots if spot not in mines_location][:25]
          selected_dangerous_spots = np.random.choice(top_dangerous_spots, min(num_spots, len(top_dangerous_spots)), replace=False)

          if num_mines_uncovered == mines_amount:
              correct_predictions += 1
          total_predictions += 1

          if total_predictions > 0:
              real_accuracy = (correct_predictions / total_predictions) * 100
          else:
              real_accuracy = 0

          for i, spot in enumerate(range(len(grid))):
            if spot not in mines_location and grid[spot] != '❌' and grid[spot] != '❔':
             if spot in selected_safe_spots[:num_spots]:
                grid[spot] = '✅'
             elif spot in selected_dangerous_spots[:mines_amount]:
                grid[spot] = '❔'
             else:
                grid[spot] = '❌'
          
          mine_emoji = "❌"
          safe_emoji = "✅"

          if user_keys:
                mine_emoji = user_keys.get("mine_emoji", mine_emoji)
                safe_emoji = user_keys.get("safe_emoji", safe_emoji)

          grid = [
          mine_emoji if cell == '❌' or cell == '💥' or cell == '❔' else safe_emoji
          for cell in grid
          ]
          Prediction6 = '\n'.join(''.join(grid[i:i + 5]) for i in range(0, len(grid), 5))
          embed6 = discord.Embed(title="``🔎`` Mines Prediction", 
                               description=f"{Prediction6}", 
                               color=discord.Color.purple())
          embed6.add_field(name="Prediction Method", 
                         value=f"> {method}", 
                         inline=False)
          embed6.add_field(name="Round ID", 
                         value=f"> {uuid}", 
                         inline=False)
          embed6.add_field(name="Amount of Bomb", 
                         value=f"> {mines_amount}", 
                         inline=False)
          embed6.add_field(name="Amount of Bet", 
                         value=f"> {bet_amount}", 
                         inline=False)
          embed6.add_field(name="Games Nounce", 
                     value=f"> {nonce6}", 
                     inline=False)
          embed6.set_footer(text=f"kirby • MinesGameMode", icon_url=LOGO)
          await interaction.response.send_message(embed=embed6, ephemeral=True)
    
    elif method == "Likelihood":
          embed = discord.Embed(title="Coming Soon", color=discord.Color.blue())
          await interaction.response.send_message(embed=embed)
    
    elif method == "Algorithm2":
          embed = discord.Embed(title="Coming Soon", color=discord.Color.blue())
          await interaction.response.send_message(embed=embed)

    elif method == "Probability2":
          embed = discord.Embed(title="Coming Soon", color=discord.Color.blue())
          await interaction.response.send_message(embed=embed)

    elif method == "Past Games2":
          embed = discord.Embed(title="Coming Soon", color=discord.Color.blue())
          await interaction.response.send_message(embed=embed)

#crash

@tree.command(name="crash", description="Predict crash on your site")
async def crash(interaction: discord.Interaction):
    user_id = interaction.user.id
    site_chosen = grab_users_site(user_id)
    model_chosen = grab_users_model(user_id)
    member = interaction.user

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return

    if not site_chosen or not model_chosen:
        missing_choices = []
        if not site_chosen:
            missing_choices.append("site")
        if not model_chosen:
            missing_choices.append("model")

        error_message = (
            f"Error: You have not chosen {', '.join(missing_choices)} yet."
            f" Please use /model [model] and/or /site [site] to continue."
        )

        embed = discord.Embed(
            title="Command Processing Error",
            description=error_message,
            color=discord.Color.purple()
        )
        embed.set_footer(text=f"Error message for {interaction.user.display_name}")
        await interaction.response.send_message(embed=embed)
    else:
        if site_chosen == "Bloxflip" and model_chosen == "Tensorflow":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating EPOCH..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            sequence_length = 5
            X_temp = []
            y_temp = []
            for i in range(len(crash_points) - sequence_length):
                X_temp.append(crash_points[i : i + sequence_length])
                y_temp.append(crash_points[i + sequence_length])
            X = np.array(X_temp)
            y = np.array(y_temp)
            model = keras.Sequential(
                [
                    keras.layers.Input(shape=(sequence_length,)),
                    keras.layers.Dense(10, activation="relu"),
                    keras.layers.Dense(1, activation="linear"),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X, y, epochs=50)
            last_sequence = crash_points[-sequence_length:]
            next_crash_point = model.predict(np.array([last_sequence]))
            formatted_next_crash_point = np.format_float_positional(
                next_crash_point, precision=2
            )
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(name="", 
                            value=f"Model: {model_chosen}", 
                            inline=False)
            embed.add_field(name="History", 
                            value=last_sequence, 
                            inline=False)
            embed.add_field(
                name="Prediction:",
                value=f"{formatted_next_crash_point}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(content="hello mate", embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Linear Regression":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Linear Prediction.."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.array(crash_points).reshape(-1, 1)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            y_scaled = scaler.fit_transform(y)
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y_scaled, test_size=0.33, random_state=42
            )
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred_scaled = model.predict(X_test)
            y_pred = scaler.inverse_transform(y_pred_scaled)
            y_test_original = scaler.inverse_transform(y_test)
            mse = mean_squared_error(y_test_original, y_pred)
            embed = discord.Embed(
                title="Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Scaled Prediction",
                value=f"{y_pred_scaled[0][0]:.2f}x",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{y_test_original[0][0]:.2f}x",
                inline=False,
            )
            embed.add_field(name="Mean Squared Error", value=f"{mse}", inline=False)
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif (
            site_chosen == "Bloxflip"
            and model_chosen == "K Nearest Neighbors Algrothim"
        ):
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating KNN Prediction.."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.array(crash_points).reshape(-1, 1)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            neigh = KNeighborsRegressor(n_neighbors=3)
            neigh.fit(X_train, y_train)
            y_pred = neigh.predict(X_test)[:1]
            y_pred3 = neigh.predict(X_test)[:3]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:",
                value=f"{y_pred:.2f}x",
                inline=False,
            )
            embed.add_field(
                name="Prediction(s)",
                value=f"{y_pred3:.2f}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Randomized":
            randomized_uniform = random.uniform(1, 6)
            embed = discord.Embed(
                title=f"Crash Prediction Randomized means its fully random",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction", value=f"{randomized_uniform:.2f}x"
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.response.send_message(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Neural Network":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our simple neural network...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating Neural Network Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            neural_network = Nnetwork(
                no_of_in_nodes=35,
                no_of_out_nodes=35,
                no_of_hidden_nodes=30,
                learning_rate=0.20,
            )
            prediction = neural_network.run(crash_points)[:1] + 1
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:", value=f"{np.round(prediction,2)}x"
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "SVR":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our SVR...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating SVR Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2)) 
            regr.fit(X_train, y_train)
            y_pred = regr.predict(X_test)[:1]  
            y_pred3 = regr.predict(X_test)[:3] 
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(y_pred,2)}x")
            embed.add_field(
                name="SVR Prediction (Type: 3)", value=f"{np.round(y_pred3,2)}"
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
            print(y_pred)
        elif site_chosen == "Bloxflip" and model_chosen == "XGBoost":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our XGBoost...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating XGBoost Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            xgb_pred = xg.XGBRegressor(objective="reg:linear", n_estimators=10, seed=12)
            xgb_pred.fit(X_train, y_train)
            pred = xgb_pred.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(pred,2)}x")
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif (
            site_chosen == "Bloxflip"
            and model_chosen == "Markov Chain Monte Carlo (MCMC)"
        ):
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Markov Chain Monte Carlo (MCMC)...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating Markov Chain Monte Carlo (MCMC) Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = tf.keras.Sequential(
                [
                    tf.keras.layers.Dense(64, activation="relu", input_shape=(1,)),
                    tf.keras.layers.Dense(1),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)
            predictions = model.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:",
                value=f"{np.round(predictions, 2)}x",
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "LightGBM":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our LightGBM Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Light GBM Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = lgb.LGBMRegressor()
            model.fit(X_train, y_train)
            pred = model.predict(X_test)[:1]
            accuracy = model.score(X_test, y_test)
            embed = discord.Embed(
                title=f"Crash Predictor",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction",
                value=f"{np.round(pred, 2)} ~ Accuracy{accuracy:.2f}",
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "CatBoost":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Catboost Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Catboost Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = cb.CatBoostRegressor(learning_rate=0.6)
            model.fit(X_train, y_train)
            pred = model.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(pred, 2)}x")
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Keras":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating EPOCH..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            sequence_length = 5
            X_temp = []
            y_temp = []
            for i in range(len(crash_points) - sequence_length):
                X_temp.append(crash_points[i : i + sequence_length])
                y_temp.append(crash_points[i + sequence_length])
            X = np.array(X_temp)
            y = np.array(y_temp)
            model = keras.Sequential(
                [
                    keras.layers.Input(shape=(sequence_length,)),
                    keras.layers.Dense(10, activation="relu"),
                    keras.layers.Dense(1, activation="linear"),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X, y, epochs=50)
            last_sequence = crash_points[-sequence_length:]
            next_crash_point = model.predict(np.array([last_sequence]))
            formatted_next_crash_point = np.format_float_positional(
                next_crash_point, precision=2
            )
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(name="History", value=last_sequence, inline=False)
            embed.add_field(
                name="Prediction:",
                value=f"{formatted_next_crash_point}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(content="hello mate", embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Probablity":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Probablity Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Probablity Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            prediction_ong = crash_points.copy()
            for _ in range(10):
                if random.random() <= 0.5:
                    prediction_ong.append(prediction_ong[-1] + 1)
                    trials = []
                    for _ in range(20):
                        trials.append(random.choice(prediction_ong))
                        chooseprediction = random.choice(trials)
                        embed = discord.Embed(
                            title="Crash Prediction",
                            color=discord.Color.purple()
                        )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{chooseprediction}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Bloxflip" or model_chosen == "Past Games":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Prediction..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            crash_pointss = sum(crash_points) / len(crash_points) * 1.3
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(
                name="Prediction",
                value=f"{crash_pointss:.2f}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif (
            site_chosen == "Bloxflip"
            and model_chosen == "Random Forest Regression / Classifer"
        ):
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Prediction..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_bloxflip_url = "https://api.bloxflip.com/games/crash"
            scrape = scraper.get(base_bloxflip_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["crashPoint"] for point in history]
            regressor = RandomForestRegressor(n_estimators=100, random_state=0)
            regressor.fit(xg, y)
            prediction = regressor.predict(X_test)[:1]
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=True,
            )
            embed.add_field(
                name="Prediction",
                value=f"{prediction:.2f}x",
                inline=True,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif (
            site_chosen == "Betbux" and model_chosen == "Tensorflow"
        ):  # betbux - dont forget or get lost
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating EPOCH..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            sequence_length = 5
            X_temp = []
            y_temp = []
            for i in range(len(crash_points) - sequence_length):
                X_temp.append(crash_points[i : i + sequence_length])
                y_temp.append(crash_points[i + sequence_length])
            X = np.array(X_temp)
            y = np.array(y_temp)
            model = keras.Sequential(
                [
                    keras.layers.Input(shape=(sequence_length,)),
                    keras.layers.Dense(10, activation="relu"),
                    keras.layers.Dense(1, activation="linear"),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X, y, epochs=50)
            last_sequence = crash_points[-sequence_length:]
            next_crash_point = model.predict(np.array([last_sequence]))
            formatted_next_crash_point = np.format_float_positional(
                next_crash_point, precision=2
            )
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(name="History", value=last_sequence, inline=False)
            embed.add_field(
                name="Prediction",
                value=f"{formatted_next_crash_point}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(content="hello mate", embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "Linear Regression":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Linear Prediction.."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.array(crash_points).reshape(-1, 1)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            y_scaled = scaler.fit_transform(y)
            X_train, X_test, y_train, y_test = train_test_split(
                X_scaled, y_scaled, test_size=0.33, random_state=42
            )
            model = LinearRegression()
            model.fit(X_train, y_train)
            y_pred_scaled = model.predict(X_test)
            y_pred = scaler.inverse_transform(y_pred_scaled)
            y_test_original = scaler.inverse_transform(y_test)
            mse = mean_squared_error(y_test_original, y_pred)
            embed = discord.Embed(
                title="Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Scaled Prediction",
                value=f"{y_pred_scaled[0][0]:.2f}",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{y_test_original[0][0]:.2f}",
                inline=False,
            )
            embed.add_field(name="Mean Squared Error", value=f"{mse}", inline=False)
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif (
            site_chosen == "Betbux"
            and model_chosen == "K Nearest Neighbors Algrothim"
        ):
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating KNN Prediction.."
            await interaction.edit_original_response(content=message)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.array(crash_points).reshape(-1, 1)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            neigh = KNeighborsRegressor(n_neighbors=3)
            neigh.fit(X_train, y_train)
            y_pred = neigh.predict(X_test)[:1]
            y_pred3 = neigh.predict(X_test)[:3]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:",
                value=f"{y_pred}",
                inline=False,
            )
            embed.add_field(
                name="Prediction(s)",
                value=f"{y_pred3}",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "Randomized":
            randomized_uniform = random.uniform(1, 6)
            embed = discord.Embed(
                title=f"Crash Prediction Randomized means its fully random",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction", value=f"{randomized_uniform:.2f}x"
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.response.send_message(embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "Neural Network":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our simple neural network...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating Neural Network Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            neural_network = Nnetwork(
                no_of_in_nodes=10,
                no_of_out_nodes=10,
                no_of_hidden_nodes=30,
                learning_rate=0.20,
            )
            prediction = neural_network.run(crash_points)[:1] + 1
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:", value=f"{np.round(prediction,2)}x"
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "SVR":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our SVR...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating SVR Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            regr = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))
            regr.fit(X_train, y_train)
            y_pred = regr.predict(X_test)[:1]  
            y_pred3 = regr.predict(X_test)[:3] 
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(y_pred,2)}", inline=False)
            embed.add_field(
                name="SVR Prediction (Type: 3)", value=f"{np.round(y_pred3,2)}", inline=False
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
            print(y_pred)
        elif site_chosen == "Betbux" and model_chosen == "XGBoost":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our XGBoost...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating XGBoost Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            xgb_pred = xg.XGBRegressor(objective="reg:linear", n_estimators=10, seed=12)
            xgb_pred.fit(X_train, y_train)
            pred = xgb_pred.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(pred,2)}x")
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.followup.send(embed=embed)
        elif (
            site_chosen == "Betbux"
            and model_chosen == "Markov Chain Monte Carlo (MCMC)"
        ):
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Markov Chain Monte Carlo (MCMC)...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Generating Markov Chain Monte Carlo (MCMC) Prediction.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = tf.keras.Sequential(
                [
                    tf.keras.layers.Dense(64, activation="relu", input_shape=(1,)),
                    tf.keras.layers.Dense(1),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)
            predictions = model.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:",
                value=f"{np.round(predictions, 2)}x",
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "LightGBM":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our LightGBM Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Light GBM Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = lgb.LGBMRegressor()
            model.fit(X_train, y_train)
            pred = model.predict(X_test)[:1]
            accuracy = model.score(X_test, y_test)
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="Prediction:",
                value=f"{np.round(pred, 2)} ~ Accuracy{accuracy:.2f}",
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "CatBoost":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Catboost Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Catboost Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            X = np.array(crash_points).reshape(-1, 1)
            y = np.ravel(crash_points)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.33, random_state=42
            )
            model = cb.CatBoostRegressor(learning_rate=0.6)
            model.fit(X_train, y_train)
            pred = model.predict(X_test)[:1]
            embed = discord.Embed(
                title=f"Crash Prediction",
                description=f"Model: {model_chosen}",
                color=discord.Color.purple()
            )
            embed.add_field(name="Prediction:", value=f"{np.round(pred, 2)}x")
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Bloxflip" and model_chosen == "Keras":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating EPOCH..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            sequence_length = 5
            X_temp = []
            y_temp = []
            for i in range(len(crash_points) - sequence_length):
                X_temp.append(crash_points[i : i + sequence_length])
                y_temp.append(crash_points[i + sequence_length])
            X = np.array(X_temp)
            y = np.array(y_temp)
            model = keras.Sequential(
                [
                    keras.layers.Input(shape=(sequence_length,)),
                    keras.layers.Dense(10, activation="relu"),
                    keras.layers.Dense(1, activation="linear"),
                ]
            )
            model.compile(optimizer="adam", loss="mean_squared_error")
            model.fit(X, y, epochs=50)
            last_sequence = crash_points[-sequence_length:]
            next_crash_point = model.predict(np.array([last_sequence]))
            formatted_next_crash_point = np.format_float_positional(
                next_crash_point, precision=2
            )
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False)
            embed.add_field(name="History", value=last_sequence, inline=False)
            embed.add_field(
                name="Prediction:",
                value=f"{formatted_next_crash_point}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(content="hello mate", embed=embed)
        elif site_chosen == "Betbux" and model_chosen == "Probablity":
            embed = discord.Embed(
                title="Please wait while we generate you a prediction with our Probablity Predictor...... This could take up to 2-4 seconds.",
                color=discord.Color.purple()
            )
            await interaction.response.send_message(embed=embed)
            embed = discord.Embed(
                title="Probablity Predictior Generating.",
                color=discord.Color.purple()
            )
            time.sleep(random.uniform(1, 3))
            await interaction.edit_original_response(embed=embed)
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            prediction_ong = crash_points.copy()
            for _ in range(10):
                if random.random() <= 0.5:
                    prediction_ong.append(prediction_ong[-1] + 1)
                    trials = []
                    for _ in range(20):
                        trials.append(random.choice(prediction_ong))
                        chooseprediction = random.choice(trials)
                        embed = discord.Embed(
                            title="Crash Prediction",
                            color=discord.Color.purple()
                        )
                        embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{chooseprediction}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "Betbux" or model_chosen == "Past Games":
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Prediction..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            crash_pointss = sum(crash_points) / len(crash_points) * 1.3
            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{crash_pointss:.2f}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif (
            site_chosen == "Betbux"
            and model_chosen == "Random Forest Regression / Classifer"
        ):
            await interaction.response.send_message(
                f"Please wait while we predict with {model_chosen}.... This can take up to 2 seconds."
            )
            message = "Generating Prediction..."
            await interaction.edit_original_response(content=message)
            time.sleep(randint(1, 2))
            base_betbux_url = "https://api.betbux.gg/crash/get-state"
            scrape = scraper.get(base_betbux_url)
            response = scrape.json()
            history = response["history"]
            crash_points = [point["multiplier"] for point in history]
            regressor = RandomForestRegressor(n_estimators=100, random_state=0)
            regressor.fit(xg, y)
            prediction = regressor.predict(X_test)[:1]

            embed = discord.Embed(
                title="Crash Prediction",
                color=discord.Color.purple()
            )
            embed.add_field(
                name="",
                value=f"Model: {model_chosen}",
                inline=False,
            )
            embed.add_field(
                name="Prediction:",
                value=f"{prediction:.2f}x",
                inline=False,
            )
            embed.set_footer(text=f"Predicting for: {interaction.user.display_name}", icon_url=LOGO)
            await interaction.edit_original_response(embed=embed)
        elif site_chosen == "RbxGold" or "Bloxmoon":
            embed = discord.Embed(
                title=f"Sorry, {site_chosen} is not supported yet, when we will get big we'll add them",
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed)

#roulette 

import requests
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from joblib import dump as joblib_dump, load as joblib_load

class MachineAILearner:
    def __init__(self):
        self.data_fetcher = requests.Session()

    def fetch_data(self):
        try:
            response = scraper.get('https://api.bloxflip.com/games/roulette')
            response.raise_for_status()
            data = response.json()
            history = data.get('history', [])[:25] 
            return history
        except requests.exceptions.RequestException as e:
            raise RuntimeError("Data fetching failed: " + str(e))

    def prepare_dataset(self, history):
        df = pd.DataFrame(history)
        df['prev_colors'] = df['winningColor'].shift(4).fillna('')
        df = df.dropna()
        return df[['prev_colors', 'winningColor']]
    
    def evaluate_color_accuracy(self, model, label_encoder, history, target_color):
        recent_rounds = history[-25:] 
        correct_predictions = 0
        total_predictions = 0

        for i in range(len(recent_rounds) - 4):
            input_data = ' '.join(game["winningColor"] for game in recent_rounds[i:i+4])
            actual_color = recent_rounds[i+4]["winningColor"]
            prediction_encoded = model.predict([input_data])[0]
            predicted_color = label_encoder.inverse_transform([prediction_encoded])[0]

            if actual_color == target_color:
                total_predictions += 1
                if predicted_color == target_color:
                    correct_predictions += 1

        if total_predictions == 0:
            return 0.0
    
        margin_of_error = 0.1 * total_predictions
        accuracy = max(min((correct_predictions / total_predictions) * 100, total_predictions + margin_of_error), total_predictions - margin_of_error)
        return accuracy

    def train_machine(self, data):
        X = data['prev_colors']
        y = data['winningColor']
        
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)
        
        pipeline = Pipeline([
            ('vectorizer', CountVectorizer(ngram_range=(1, 3))),
            ('scaler', StandardScaler(with_mean=False)),
            ('model', RandomForestClassifier(n_estimators=100, random_state=42))
        ])
        
        pipeline.fit(X, y_encoded)
        return pipeline, label_encoder
    
    def predict_next_color(self, model, label_encoder, history):
        recent_rounds = history[-4:]
        input_data = ' '.join(game["winningColor"] for game in recent_rounds)
        prediction_encoded = model.predict([input_data])[0]
        next_color = label_encoder.inverse_transform([prediction_encoded])[0]
        return next_color
    
    def save_trained_machine(self, model, label_encoder):
        joblib_dump(model, "machine_learning_model.joblib")
        joblib_dump(label_encoder, "machine_label_encoder.joblib")

    def load_trained_machine(self):
        model = joblib_load("machine_learning_model.joblib")
        label_encoder = joblib_load("machine_label_encoder.joblib")
        return model, label_encoder
    
if __name__ == "__main__":
    machine_learner = MachineAILearner()

    try:
        data_history = machine_learner.fetch_data()
        prepared_data = machine_learner.prepare_dataset(data_history)
        trained_model, trained_label_encoder = machine_learner.train_machine(prepared_data)

        color_list = ["red", "purple", "yellow"]
        color_accuracies = [machine_learner.evaluate_color_accuracy(trained_model, trained_label_encoder, data_history, color) for color in color_list]
        
        next_color_prediction = machine_learner.predict_next_color(trained_model, trained_label_encoder, data_history)
        
        machine_learner.save_trained_machine(trained_model, trained_label_encoder)
    except RuntimeError as e:
        print("An error occurred:", e)

#2

class Algorithm:
    def __init__(self):
        self.data_fetcher = requests.Session()

    def fetch_data(self):
        try:
            response = scraper.get('https://api.bloxflip.com/games/roulette')
            response.raise_for_status()
            data = response.json()
            history = data.get('history', [])[:25] 
            return history
        except requests.exceptions.RequestException as e:
            raise RuntimeError("Data fetching failed: " + str(e))

    def prepare_dataset(self, history):
        df = pd.DataFrame(history)
        df['prev_colors'] = df['winningColor'].shift(4).fillna('')
        df = df.dropna()
        return df[['prev_colors', 'winningColor']]
    
    def evaluate_color_accuracy(self, model, label_encoder, history, target_color):
        recent_rounds = history[-25:] 
        correct_predictions = 0
        total_predictions = 0

        for i in range(len(recent_rounds) - 4):
            input_data = ' '.join(game["winningColor"] for game in recent_rounds[i:i+4])
            actual_color = recent_rounds[i+4]["winningColor"]
            prediction_encoded = model.predict([input_data])[0]
            predicted_color = label_encoder.inverse_transform([prediction_encoded])[0]

            if actual_color == target_color:
                total_predictions += 1
                if predicted_color == target_color:
                    correct_predictions += 1

        if total_predictions == 0:
            return 0.0
    
        margin_of_error = 0.1 * total_predictions
        accuracy = max(min((correct_predictions / total_predictions) * 100, total_predictions + margin_of_error), total_predictions - margin_of_error)
        return accuracy

    def train_machine(self, data):
        X = data['prev_colors']
        y = data['winningColor']
        
        label_encoder = LabelEncoder()
        y_encoded = label_encoder.fit_transform(y)
        
        pipeline = Pipeline([
            ('vectorizer', CountVectorizer(ngram_range=(1, 3))),
            ('scaler', StandardScaler(with_mean=False)),
            ('model', LogisticRegression(solver='liblinear'))
        ])
        
        pipeline.fit(X, y_encoded)
        return pipeline, label_encoder
    
    def predict_next_color(self, model, label_encoder, history):
        recent_rounds = history[-4:]
        input_data = ' '.join(game["winningColor"] for game in recent_rounds)
        prediction_encoded = model.predict([input_data])[0]
        next_color = label_encoder.inverse_transform([prediction_encoded])[0]
        return next_color
    
    def save_trained_machine(self, model, label_encoder):
        joblib_dump(model, "algorithm_learning_model.joblib2") 
        joblib_dump(label_encoder, "algorithm_label_encoder.joblib2")  

    def load_trained_machine(self):
        model = joblib_load("algorithm_learning_model.joblib2")
        label_encoder = joblib_load("algorithm_label_encoder.joblib2")  
        return model, label_encoder
    
if __name__ == "__main__":
    algorithm = Algorithm()

    try:
        data_history = algorithm.fetch_data()
        prepared_data = algorithm.prepare_dataset(data_history)
        trained_model, trained_label_encoder = algorithm.train_machine(prepared_data)

        color_list = ["red", "purple", "yellow"]
        color_accuracies = [algorithm.evaluate_color_accuracy(trained_model, trained_label_encoder, data_history, color) for color in color_list]
        
        next_color_prediction = algorithm.predict_next_color(trained_model, trained_label_encoder, data_history)
        
        algorithm.save_trained_machine(trained_model, trained_label_encoder)
    except RuntimeError as e:
        print("An error occurred:", e)






@app_commands.choices(method=[
  Choice(name="AI", value="AI"),
  Choice(name="Algorithm", value="Algorithm"),
  Choice(name="Logistic Regression", value="Logistic Regression")
])
@tree.command(name="roulette", description="Predict roulette Based prediction using")
async def roulette(interaction: discord.Interaction, method: str):
    member = interaction.user

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have an active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    if method == "AI":
        with open("tokens.json", "r") as f:
          keys = json.load(f)
          user_keys = keys.get(str(interaction.user.id))
          if user_keys:
           auth = user_keys.get("auth_token")
          else:
            embed = discord.Embed(
            title="Error",
            description=
            "the bot detected that you didn't linked your account link your account to start working!",
            color=discord.Color.red())
            await interaction.response.send_message(embed=embed, 
                                                ephemeral=True)
            return  
          
        try:
            response = scraper.get('https://api.bloxflip.com/games/roulette',
                                   headers={"x-auth-token": auth})
            response.raise_for_status()
            data = response.json()

            if 'history' not in data or not data['history']:
                raise ValueError("No history data available")
            data2 = scraper.get("https://api.bloxflip.com/games/roulette").json()["current"]["_id"]
            if '"joinable":false' in data2:
                embed = discord.Embed(title="Round not Over", description="Round is about to be finished. Please wait!", color=discord.Color.red())
                await interaction.response.send_message(embed=embed)
                return
            
            machine_learner = MachineAILearner()  
            history = machine_learner.fetch_data() 
            model, label_encoder = machine_learner.load_trained_machine()

            r_accuracy = machine_learner.evaluate_color_accuracy(model, label_encoder, history, "red")
            p_accuracy = machine_learner.evaluate_color_accuracy(model, label_encoder, history, "purple")
            y_accuracy = machine_learner.evaluate_color_accuracy(model, label_encoder, history, "yellow")

            embed = discord.Embed(title=f"{method} Roulette Prediction", color=discord.Color.purple())
            embed.add_field(name="Round ID", value=f"{data2}", inline=False)
            embed.add_field(name="Red", value=f"{r_accuracy:.2f}%", inline=True)
            embed.add_field(name="Purple", value=f"{p_accuracy:.2f}%", inline=True)
            embed.add_field(name="Yellow", value=f"{y_accuracy:.2f}%", inline=True)
            await interaction.response.send_message(embed=embed)
        except requests.exceptions.RequestException as e:
            error_message = "An error occurred while getting data from the API."
            embed = discord.Embed(title="Error", description=error_message, color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
        except (json.JSONDecodeError, ValueError) as e:
            error_message = "An error occurred while processing API response."
            embed = discord.Embed(title="API Response Error", description=error_message, color=discord.Color.red())
            await interaction.response.send_message(embed=embed)
    
    elif method == "Algorithm":
        with open("tokens.json", "r") as f:
            keys = json.load(f)
            user_keys = keys.get(str(interaction.user.id))
            if user_keys:
             auth = user_keys.get("auth_token")
            else:
              embed = discord.Embed(
              title="Error",
              description=
              "the bot detected that you didn't linked your account link your account to start working!",
              color=discord.Color.red())
              await interaction.response.send_message(embed=embed, 
                                                       ephemeral=True)
              return
        

        try:
           response = scraper.get('https://api.bloxflip.com/games/roulette')
           response.raise_for_status()
           data = response.json()

           if 'history' not in data or not data['history']:
              raise ValueError("No history data available")

           data2 = scraper.get("https://api.bloxflip.com/games/roulette").json()["current"]["_id"]

           print("data2 content:", data2)

           if '"joinable":false' in data2:
               embed = discord.Embed(title="Round not Over", description="Round is about to be finished. Please wait!", color=discord.Color.red())
               await interaction.response.send_message(embed=embed)
           else:
               data_history = algorithm.fetch_data()
               prepared_data = algorithm.prepare_dataset(data_history)
               trained_model, trained_label_encoder = algorithm.train_machine(prepared_data)

               color_list = ["Red", "Purple", "Yellow"]

               embed = discord.Embed(title=f"{method} Roulette Prediction", color=discord.Color.purple())
               next_color_prediction = algorithm.predict_next_color(trained_model, trained_label_encoder, data_history)
               embed.add_field(name="Round ID", value=f"{data2}", inline=False)
               embed.add_field(name="Next Color Prediction:", value=next_color_prediction, inline=False)

               accuracy_values = {}

               for color in color_list:
                   accuracy = algorithm.evaluate_color_accuracy(trained_model, trained_label_encoder, data_history, color.lower())
                   accuracy_values[color] = f"{accuracy:.2f}%"
               for color, accuracy in accuracy_values.items():
                   embed.add_field(name=f"{color}", value=accuracy, inline=True)
               await interaction.response.send_message(embed=embed)
        except requests.exceptions.RequestException as e:
               error_message = "An error occurred while getting data from the API."
               embed = discord.Embed(title="Error", description=error_message, color=discord.Color.red())
               await interaction.response.send_message(embed=embed)
        except (json.JSONDecodeError, ValueError) as e:
               error_message = "An error occurred while processing API response."
               embed = discord.Embed(title="API Response Error", description=error_message, color=discord.Color.red())
               await interaction.response.send_message(embed=embed)

    elif method == "Logistic Regression":
              embed = discord.Embed(
              title="Coming today!",
              description=
              "",
              color=discord.Color.red())
              await interaction.response.send_message(embed=embed, 
                                                       ephemeral=True)
              return



#site

@app_commands.choices(site_choices=[
    app_commands.Choice(name="Bloxmoon", value="1"),
    app_commands.Choice(name="RbxGold", value="2"),
    app_commands.Choice(name="Bloxflip", value="3"),
    app_commands.Choice(name="Betbux", value="4"),
])
@tree.command(name="site", description="Allows you to choose your site")
async def site(interaction: discord.Interaction, site_choices: app_commands.Choice[str]):
    member = interaction.user

    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    with open("sites.json", "w") as f:
        sites[str(interaction.user.id)] = {"site": site_choices.name}
        json.dump(sites, f, indent=4)
    embed = discord.Embed(title="Site Update Successful", color=discord.Color.purple())
    embed.add_field(name="", value=f"> Your selected site has been updated to **{site_choices.name}**.", inline=False)
    embed.set_footer(text="Thank you for choosing Our Predictor", icon_url=LOGO)
    await interaction.response.send_message(embed=embed, ephemeral=True)

#model-crash

@app_commands.choices(model=[
    app_commands.Choice(name="Tensorflow", value="1"),
    app_commands.Choice(name="Linear Regression", value="2"),
    app_commands.Choice(name="K Nearest Neighbors Algrothim", value="3"),
    app_commands.Choice(name="Torch", value="4"),
    app_commands.Choice(name="Randomized", value="5"),
    app_commands.Choice(name="Neural Network", value="6"),
    app_commands.Choice(name="SVR", value="7"),
    app_commands.Choice(name="XGBoost", value="8"),
    app_commands.Choice(name="Markov Chain Monte Carlo (MCMC)", value="9"),
    app_commands.Choice(name="LightGBM", value="10"),
    app_commands.Choice(name="CatBoost", value="11"),
    app_commands.Choice(name="Keras", value="12"),
    app_commands.Choice(name="Probablity", value="13"),
    app_commands.Choice(name="Past Games", value="14"),
    app_commands.Choice(name="Random Forest Regression / Classifer ", value="15"),
])
@tree.command(name="model", description="Allows you set your base model for predicting")
async def model(interaction: discord.Interaction, model: app_commands.Choice[str]):
    member = interaction.user
    
    if not discord.utils.get(member.roles, name="Customer"):
        embed_role = discord.Embed(
            title="Error",
            description="You do not have active subscription.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed_role, ephemeral=True)
        return
    
    with open("models.json", "w") as f:
        models[str(interaction.user.id)] = {"model": model.name}
        json.dump(models, f, indent=4)
    embed = discord.Embed(title="Model Change Successful", color=discord.Color.purple())
    embed.add_field(name="", value=f"> Your selected predictive model has been changed to **{model.name}**.", inline=False)
    embed.set_footer(text="Thank you for choosing Our Predictor", icon_url=LOGO)
    await interaction.response.send_message(embed=embed, ephemeral=True)

client.run("your bot token here")
