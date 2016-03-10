#encoding:utf8

from . import WeChatRequest

class WeChatEvent(WeChatRequest):
    _allowed_keys = dict(WeChatRequest._allowed_keys, **dict(
        Event=str,
        EventKey=str,
        Ticket=str
    ))

    _event = None

    @property
    def event(self):
        return self._event
        
    @event.setter
    def event(self, value):
        self._event = value