

import re

def search_and_respond(bot, user, channel, msg, config):
    stub = "https://review.hpcloud.net/#/c/57038/"
    pattern = re.compile(' \d\d\d\d\d ')
    results = pattern.findall(msg)
    bot.logger.log("gerrit_hp {0}".format(results))
    for i in results:
        bot.msg(channel, make_hp_gerrit_url(i))

def make_hp_gerrit_url(change):
    return "https://review.hpcloud.net/#/c/{0}".format(change)

if __name__ == "__main__":
    import sys 
    pattern = re.compile('\d\d\d\d\d')
    #example_string = "testing 57038, 57031, 57020"
    example_string = "testing "
    results = pattern.findall(example_string)
    for i in results:
        print make_hp_gerrit_url(i)
    


