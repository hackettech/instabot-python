import instabot
bot=instabot.Bot()
bot.login(username=input("Type your Username:"), password=input("Type your Password:"))
bot.send_message(text=input ("Type Your message:"),user_ids=input ("Type friends Instagram username:"))
bot.logout()
