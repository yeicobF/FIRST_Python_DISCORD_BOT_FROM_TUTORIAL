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

# from pathlib import Path  # Python 3.6+ only
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)

# Create an instance to a Client. A connection to Discord.
client = discord.Client()

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
        await message.channel.send("sergio")

    if message.content.startswith("german"):
        await message.channel.send("...")

    if message.content.startswith("rodrigo"):
        await message.channel.send("basado")



# Empezaremos a correr el bot. Se debe poner el Token dentro de run()
# Accedemos utilizando la variable que agregamos en el archivo .env
client.run(os.getenv(ODA0NTkyMjA2OTc5NTMwNzc0.YBOk4g.6lv2eVYrGbzCKrzd-aftbwXRu2w))

# No funciona en este repositorio, creo que tendría que instalar dotnet,
#   pero en repl.it sí funciona.
# client.run(os.getenv('TOKEN'))
