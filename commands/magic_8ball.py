import random
import time

from client_interaction import delete_message, send_message


"""
Command function template
Description

@param client: The discord client, generally assumed to be the bot user itself
@param message: The message the discord bot is responding to
@param other_args: Whatever other args that are passed into this template
@result: sends a message on...
@result: deletes a message on...
@result: adds a react on....
"""
async def command(client, message, other_args):
  await delete_message(message)

  
answers = [
      "As I see it, yes", "Ask again later", "Better not tell you now", 
      "Cannot predict now", "Concentrate and ask again", "Don't count on it", 
      "It is certain", "It is decidedly so", "Most likely", "Most likely", 
      "My sources say no", "Outlook not so good", "Outlook good", 
      "Reply hazy, try again", "Signs point to yes", "Very doubtful", 
      "Without a doubt","Yes", "Yes - definitely", "You may rely on it"
      "Fire Bruce Weber", "Fire Bruce Weber", "Fire Bruce Weber", "Fire Bruce Weber"]

print ("Stacy's Mom shakes the Magic 8-Ball")

time.sleep(2)

response_message = "The Magic 8-Ball says: " + random.choice(answers)


# String that triggers this command
TRIGGER = '!Magic8ball'

def is_triggered(message_content):
  return message_content.lower() == TRIGGER