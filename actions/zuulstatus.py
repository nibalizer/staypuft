import requests

def zuulstatus(bot, user, channel, msg, config):
    r = requests.get(config.zuul_status)
    
    length = r.json()['trigger_event_queue']['length']
    msg = 'Queue length: {0}'.format(length)
    bot.msg(channel, msg)


#mock the bot
class mybot():

    def msg(self, chan, resp):
        print resp

#mock the config
class myconfig():
    zuul_status = 'http://zuul.openstack.org/status.json'

if __name__ == "__main__":
    import sys 
    bot = mybot()
    config = myconfig()
    zuulstatus(bot, 'nibalizer', '#ghostbusters', 'zuulstatus', config)

