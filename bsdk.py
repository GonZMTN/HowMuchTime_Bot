## import modules
import os
from telegram import *
from telegram.ext import *
import time
from datetime import datetime, timedelta

# import bot token (mandatory)
updater = Updater('5079202031:AAENcYeG3K5IeUddmyDm5p09hRPQCWDuwrE')


## define your functions
def bsdk(update, context):
  gali=update.message.reply_text("Ha Bsdk bhai 🙋‍♂ !")
  time.sleep(3)
  context.bot.editMessageText(
        message_id=gali.message_id, 
        chat_id=update.message.chat_id, 
        text=f"""Teri user ID = {update.message.from_user.id}
USERName = @{update.message.from_user.username}
Name = {update.message.from_user.first_name}
Chat id = {update.message.chat_id}
Group user name = @{update.message.chat.username}
       """ )
def s(update, context):
    d=update.message.date
    fdate=int(time.mktime(d.timetuple()))
    sfdate=str(fdate)
    astime=str(datetime.now())
    actime=astime.rfind('.')
    actimee = int(actime)
    actually=actimee - 8
    qtime=astime[actually:actimee]
    update.message.reply_text(f"Timer started at {qtime}")
    with open('time.py', 'w+') as f:
      f.truncate()
      f.write(sfdate)
def e(update, context):
    with open('time.py', 'r') as f:
       ok=f.readlines()
       for i in ok:
         etime=i
    d=update.message.date
    fdate=int(time.mktime(d.timetuple()))
    TotalTime=int(int(fdate) - int(etime))
    hello=str(timedelta(seconds=TotalTime))
    update.message.reply_text(f"Time elapsed = *{hello}* ", parse_mode='MARKDOWN')  
    
    

## cmd handler moment
def setup_dispatcher(dp):  
   dp.add_handler(CommandHandler('bsdk', bsdk))
   dp.add_handler(CommandHandler('e', e))
   dp.add_handler(CommandHandler('s', s))
   return dp

## settings dispatcher
dp = updater.dispatcher
dp = setup_dispatcher(dp)

## starting the bot
updater.start_polling(allowed_updates=Update.ALL_TYPES)
print("\n\nPru aff bot has been started ,,, noobs stay away !!")


