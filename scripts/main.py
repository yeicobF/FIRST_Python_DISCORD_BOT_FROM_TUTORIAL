# Viernes, 29 de enero del 2021 [12:38 AM]
#
# Para que el programa funcione hay que instalar la librería de Python de
#   Discord, discord.py, escribiendo el siguiente comando en la terminal:
#       
#       pip install -U discord.py
# FUENTE: https://realpython.com/how-to-make-a-discord-bot-python/

import discord # Discord Library
# Import os in order to access TOKEN from the .env file.
import os
# Utilizaremos una API, por lo que necesitamos utilizar requests, que hace una
#   solicitud mediante HTML, y la recibe como JSON, por lo que también tendremos
#   que importar JSON.
import requests
import json

TOKEN = "ODA0NTkyMjA2OTc5NTMwNzc0.YBOk4g.RXiPE_ruWKE32rK1b-NYWqEwYAQ"
# from pathlib import Path  # Python 3.6+ only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# Create an instance to a Client. A connection to Discord.
client = discord.Client()

# Para obtener frases inspiracionales de una API.
def get_quote():
    # Request data from the API URL.
    # It returns a random quote.
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text) # This way we get the json file.
    # In order to get the quote, we must figure out how it comes in the json file.
    # json_data[0]['q'] = quote, json_data[0]['a'] = author.
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

# Use the client.creator.event to register an event.
# This client uses events to make it work. This is how you register an event.
# This is an asyncronous library which used callbacks (function called when
# something else happens.)
@client.event
# The event will be called when the bot started being used.
# It will print the next message to the console when it is ready to run.
# Event that happens as soon as the bot is ready and working.
async def on_ready(): # When the bot is running and ready to be used.
    # It will print the client.
    print("\n - We have logged in as {0.user}".format(client))
    print(f"\n - client.user.name {client.user.name}")
    # # Hacer que el bot muestre que está viendo un directo.
    # # No funcionó así, solo muestra el nombre.
    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Escape Utópico",
                                                        #    url="https://www.twitch.tv/videos/725928952", details="Nostalgia..."))
    # Hacer que el bot muestre que está viendo un directo.
    await client.change_presence(activity=discord.Streaming(name="Escape Utópico", url="https://www.twitch.tv/escape_utopico"))

@client.event
# To now what to do when a message is received.
# If the message is from the bot, it will do nothing.
async def on_message(message):
    # If the message is sent by the bot, do nothing.
    if message.author == client.user:
        return

    # Prefijo con el que se manejarán los comandos del bot.
    if message.content.startswith("sergio"):
        # El mensaje que se mandará cuando se reciba el comando.
        await message.channel.send(".")

    # Lo de abajo no funcionó.
    # if message.content.startswith("!!."):
    #     await client.change_presence(activity="Sergio", status=, afk=True)

    if message.content.startswith("german"):
        await message.channel.send("...")

    if message.content.startswith("rodrigo"):
        await message.channel.send("basado")

    # To send the inspirational quote.
    if message.content.startswith("!inspiration"):
        await message.channel.send(get_quote())

# Empezaremos a correr el bot. Se debe poner el Token dentro de run()
# Accedemos utilizando la variable que agregamos en el archivo .env
client.run(TOKEN)

# No funciona en este repositorio, creo que tendría que instalar dotnet,
#   pero en repl.it sí funciona.
# client.run(os.getenv('TOKEN'))
