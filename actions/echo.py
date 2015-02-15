
def echo(bot, user, channel, msg):
    bot.msg(channel, msg[5:])


#mock the bot
class mybot():

    def msg(self, chan, resp):
        print resp

if __name__ == "__main__":
    import sys 
    bot = mybot()
    echo(bot, 'nibalizer', '#ghostbusters', 'echo {0}'.format(sys.argv[1]))

