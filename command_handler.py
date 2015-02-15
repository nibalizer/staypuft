commands_available = {}

from actions.echo import echo
commands_available['echo'] = echo

def command_handler(bot, user, channel, msg):
    stripped_msg = msg.lstrip()
    for command in commands_available.keys():
        if stripped_msg.startswith(command):
            commands_available[command](bot, user, channel, msg)
            return

    msg = "%s: Command not found" % user
    bot.msg(channel, msg)



