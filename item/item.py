import random

from ircbot.events import sendmessage, sendaction
from ircbot.command import IRCCommand

import arcuser.arcuser_controller as arcuser_controller
from factoid.events import registersmartvariable

import item.item_controller as item_controller

PREMADE_ITEMS = ['a thousand rolls of toilet paper', 'three mushrooms', 'a pet turtle named Turt']


class ItemPlugin(IRCCommand):

    def __init__(self):
        super(ItemPlugin, self).__init__('give', self.give_item,
                                         args='<item_name>',
                                         description='Give arcbot items to hold.')

    def ready(self, component):
        self.fire(registersmartvariable(self.user_variables))

    def give_item(self, user, channel, args):
        arcuser = arcuser_controller.get_or_create_arcuser(user)
        if not args:
            self.fire(sendmessage(channel, '{}: What item did you want to give me?'))
            return
        item = item_controller.add_item(creator=arcuser, channel=channel, name=args)
        self.fire(sendaction(channel, 'puts {} in his pocket.'.format(item.name)))

    def user_variables(self, channel=None, **kwargs):
        return {
            'item': lambda: item_controller.get_item(channel=channel) or random.choice(PREMADE_ITEMS),
            'giveitem': lambda: item_controller.pop_item(channel=channel) or random.choice(PREMADE_ITEMS),
        }

    def stats(self):
        stats = {
            (lambda: "I currently have {} items.".format(item_controller.count_items()),
                ('items', 'counts', 'current')),
            (lambda: "I've seen {} items total!".format(item_controller.count_items()),
                ('items', 'counts', 'all')),
            (self._top_itemer(false), ('items', 'counts', 'current', 'top')),
            (self._top_itemer(true), ('items', 'counts', 'all', 'top'))
        }

        for arcuser in item_controller.get_all_arcusers_with_items():
            stats.add(
                (lambda: "{} of my current items are from {}.".format(item_controller.count_items(arcuser, true), arcuser.base.nick),
                 ('items', 'counts', 'current', arcuser.base.nick)),
                (lambda: "{} has created {} items.".format(arcuser.base.nick, item_controller.count_items(arcuser, true)),
                 ('items', 'counts', 'all', arcuser.base.nick))
            )

    def _top_itemer(self, include_deleted):
        strings = {
            true: {
                'none': 'No one has given me any items!',
                'one': '{} has given me the most items, {}.',
                'multiple': '{} have given me the most items: {} each.'
            },
            false: {
                'none': "I don't have any items!",
                'one': 'Most of my items are from {}: {}.',
                'multiple': '{} have given me the most of my current items: {} each.'
            }
        }[include_deleted]

        def calc_top():
            arcusers = item_controller.get_all_arcusers_with_items()
            top_arcusers, top_count = arcusers[:1], item_controller.count_items(arcusers[0])
            for arcuser in arcusers[1:]:
                count = item_controller.count_items(arcuser, include_deleted=include_deleted)
                if count > top_count:
                    top_arcusers = [arcuser]
                    top_count = count
                elif count == top_count:
                    top_arcusers.append(arcuser)

            if not top_arcusers:
                return strings['none']
            elif len(top_arcusers) == 1:
                return strings['one'].format(user=top_arcusers[0].base.nick, count=top_count)
            else:
                start = ', '.join(map(lambda u: u.base.nick, top_arcusers[:-1]))
                users_string = start + ' and ' + top_arcusers[-1].base.nick
                return strings['multiple'].format(users_string, top_count)
        return calc_top
