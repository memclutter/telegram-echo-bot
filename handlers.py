"""
Handlers module.

Contains bot handlers.
"""

def echo(bot, update):
    """Echo handler"""
    update.message.reply_text(update.message.text)
