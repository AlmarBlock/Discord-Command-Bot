import requests
import json
import inspect
import sys
import random

from colorama import Fore, Style

# Make sure that the user is running Python 3.8 or higher
if sys.version_info < (3, 8):
    exit("Python 3.8 or higher is required to run this bot!")

# Now make sure that the discord.py library is installed or/and is up to date
try:
    from discord import app_commands, Intents, Client, Interaction
except ImportError:
    exit(
        "Either discord.py is not installed or you are running an older and unsupported version of it."
        "Please make sure to check that you have the latest version of discord.py! (try reinstalling the requirements?)"
    )



# Try except block is useful for when you'd like to capture errors
try:
    with open("config.json") as f:
        config = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # You can in theory also do "except:" or "except Exception:", but it is not recommended
    # unless you want to suppress all errors
    config = {}


while True:
    # If no token is stored in "config" the value defaults to None
    token = config.get("token", None)
    if token:
        print(f"\n--- Detected token in {Fore.GREEN}./config.json{Fore.RESET} (saved from a previous run). Using stored token. ---\n")
    else:
        # Take input from the user if no token is detected
        token = input("> ")

    # Validates if the token you provided was correct or not
    # There is also another one called aiohttp.ClientSession() which is asynchronous
    # However for such simplicity, it is not worth playing around with async
    # and await keywords outside of the event loop
    try:
        data = requests.get("https://discord.com/api/v10/users/@me", headers={
            "Authorization": f"Bot {token}"
        }).json()
    except requests.exceptions.RequestException as e:
        if e.__class__ == requests.exceptions.ConnectionError:
            exit(f"{Fore.RED}ConnectionError{Fore.RESET}: Discord is commonly blocked on public networks, please make sure discord.com is reachable!")

        elif e.__class__ == requests.exceptions.Timeout:
            exit(f"{Fore.RED}Timeout{Fore.RESET}: Connection to Discord's API has timed out (possibly being rate limited?)")

        # Tells python to quit, along with printing some info on the error that occured
        exit(f"Unknown error has occurred! Additional info:\n{e}")

    # If the token is correct, it will continue the code
    if data.get("id", None):
        break  # Breaks out of the while loop

    # If the token is incorrect, an error will be printed
    # You will then be asked to enter a token again (while Loop)
    print(f"\nSeems like you entered an {Fore.RED}invalid token{Fore.RESET}. Please enter a valid token (see Github repo for help).")

    # Resets the config so that it doesn't use the previous token again
    config.clear()


# This is used to save the token for the next time you run the bot
with open("config.json", "w") as f:
    # Check if 'token' key exists in the config.json file
    config["token"] = token

    # This dumps our working setting to the config.json file
    # Indent is used to make the file look nice and clean
    # If you don't want to indent, you can remove the indent=2 from code
    json.dump(config, f, indent=2)


class FunnyBadge(Client):
    def __init__(self, *, intents: Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self) -> None:
        """ This is called when the bot boots, to setup the global commands """
        await self.tree.sync()


# Variable to store the bot class and interact with it
# Since this is a simple bot to run 1 command over slash commands
# We then do not need any intents to listen to events
client = FunnyBadge(intents=Intents.none())


@client.event
async def on_ready():
    """ This is called when the bot is ready and has a connection with Discord
        It also prints out the bot's invite URL that automatically uses your
        Client ID to make sure you invite the correct bot with correct scopes.
    """
    print(inspect.cleandoc(f"""
        Logged in as {client.user} (ID: {client.user.id})

        Use this URL to invite {client.user} to your server:
        {Fore.LIGHTBLUE_EX}https://discord.com/api/oauth2/authorize?client_id={client.user.id}&scope=applications.commands%20bot{Fore.RESET}
    """), end="\n\n")



@client.tree.command()
async def hallo(interaction: Interaction):
    """ Sage hallo """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"Hi **{interaction.user}**", ephemeral=True)

@client.tree.command()
async def UserNameHier(interaction: Interaction):
    """ Infos über UserNameHier """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"**UserNameHier** mag __Züge__!!!")

@client.tree.command()
async def info(interaction: Interaction):
    """ Infos, Infos, Infos """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"**__Infos__**\n-Die Regeln sind unter <#ChannelIDHier> zu finden.\n-Bei Problem/Feedback melde dich unter: <#ChannelIDHier>\n__-Wir hoffen dir gefällt dieser Discord.__", ephemeral=True)

@client.tree.command()
async def test(interaction: Interaction):
    """ Test """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"**Test**", ephemeral=True)

@client.tree.command()
async def UserNameHier(interaction: Interaction):
    """ Infos über UserNameHier """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"**<@UserIDHier>** mag Züge zum Frühstück!")

@client.tree.command()
async def me(interaction: Interaction):
    """ Infos über mich """
    # Then responds in the channel with this message
    antworten = ["mag Züge", "schaut Almar_Block", "spielt Minecraft", "kann nicht spielen", "muss auf Klo", "hat sich in die Hose gemacht", "hat sich kurz vor dem Klo in die Hose gemacht", "ist ein Ni||nj||a"]
    zufällige_antwort = random.choice(antworten)
    user_id = interaction.user.id
    await interaction.response.send_message(content=f"<@{user_id}> {zufällige_antwort}!")

@client.tree.command()
async def würfeln(interaction: Interaction):
    """ Würfel ein Würfel """
    # Then responds in the channel with this message
    antworten = ["1", "2", "3", "4", "5", "6"]
    zufällige_antwort = random.choice(antworten)
    user_id = interaction.user.id
    await interaction.response.send_message(content=f"<@{user_id}> hat eine **__{zufällige_antwort}__** gewürfelt.")

@client.tree.command()
async def commands(interaction: Interaction):
    """ Liste der verfügbaren Commands """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"Dies ist die Liste aller verfügbaren Commands.\n\n```/hallo\n/info\n/ip\n/me\n/test\n/würfeln```\n\nSolltest du finden, dass es noch mehr sein sollen, melde dich unter <#ChannelIDHier>!", ephemeral=True)

@client.tree.command()
async def help(interaction: Interaction):
    """ Liste der verfügbaren Commands """
    # Then responds in the channel with this message
    await interaction.response.send_message(content=f"Dies ist die Liste aller verfügbaren Commands.\n\n```/hallo\n/info\n/ip\n/me\n/test\n/würfeln```\n\nSolltest du finden, dass es noch mehr sein sollen, melde dich unter <#ChennelIDHier>!", ephemeral=True)



# Runs the bot with the token you provided
client.run(token)
