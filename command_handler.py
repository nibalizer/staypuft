commands_available = {}

from actions.echo import echo
commands_available['echo'] = echo

from actions.zuulstatus import zuulstatus
commands_available['zuulstatus'] = zuulstatus
commands_available['zs'] = zuulstatus

from actions.puppettypes import puppet_type_ref
commands_available['puppet type'] = puppet_type_ref

from actions.pagerduty import get_vanguard, get_sentinel, get_schedule
commands_available['vanguard'] = get_vanguard
commands_available['sentinel'] = get_sentinel

def bothelp(bot, user, channel, msg, config):
    msg = "Use {0}".format(",".join(commands_available.keys()))
    bot.msg(channel, msg)

commands_available['help'] = bothelp

def command_handler(bot, user, channel, msg, config):
    stripped_msg = msg.lstrip()

    if channel == bot.nickname:
        channel = user
    for command in commands_available.keys():
        if stripped_msg.startswith(command):
            commands_available[command](bot, user, channel, msg, config)
            return

    msg = "%s: Command not found" % user
    bot.msg(channel, msg)



