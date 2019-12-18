from telegram.ext import Updater ,CommandHandler

import requests

bot_token=""

#bot = telegram.Bot(token=bot_token)

updater = Updater(bot_token, use_context=True)

dispatcher = updater.dispatcher

def fetch_fork_num(update,context):
    res=requests.get("https://api.github.com/orgs/fedora-infra/repos").json()
    output=str()
    for i in res:
        output+=(" - repo: "+i["name"]+"\n"+"    forks count : "+str(i["forks_count"])+"\n")
    #print(output)
    update.message.reply_text(output)

dispatcher.add_handler(CommandHandler("fetch_fork_num", fetch_fork_num))
 
if __name__=="__main__":
    updater.start_polling()
    updater.idle()