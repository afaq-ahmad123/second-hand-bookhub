
from channels.routing import route

channel_routing = [
    route('websocket.receive', 'chat.consumers.ws_echo'),
]
# # This function will display all messages received in the console
# def message_handler(message):
#     print(message['text'])
#
#
# channel_routing = [
#     route("websocket.receive", message_handler)  # we register our message handler
# ]
