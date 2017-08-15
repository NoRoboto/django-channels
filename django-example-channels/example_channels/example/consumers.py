from channels import Group


def ws_connect(message):
    #Group('user-{}'.format(message.user.id)).add(message.reply_channel)
    Group('users').add(message.reply_channel)
    message.reply_channel.send({'accept': True})


def ws_receive(message):
    print(message.content)
    text = message.content.get('text')
    if text:
        Group('users').send({"text": text})
        #message.reply_channel.send({"text": "You said: {}".format(text)})


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)
