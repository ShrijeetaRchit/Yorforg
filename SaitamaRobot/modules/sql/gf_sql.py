import threading

from SaitamaRobot.modules.sql import BASE, SESSION
from sqlalchemy import (Boolean, Column, Integer, String, UnicodeText, distinct,
                        func)
from sqlalchemy.dialects import postgresql


class Girlfriend(BASE):
    __tablename__ = "Girlfriends"

    user_id = Column(Integer, primary_key=True)
    chat_id = Column(String(14), primary_key=True)
    num_gf = Column(Integer, default=5)
    
    
    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = str(chat_id)
        self.num_gfs = 5

    def __repr__(self):
        return "<{} Girlfriends Of {} in {}>".format(
            self.num_gfs, self.user_id, self.chat_id)
            
Girlfriend.__table__.create(checkfirst=True)
GfSettings.__table__.create(checkfirst=True)

GF_INSERTION_LOCK = threading.RLock()

GF_SETTINGS_LOCK = threading.RLock()

            def remove_gf(user_id, chat_id):
    with GF_INSERTION_LOCK:
        removed = False
        stealed_user = SESSION.query(Girlfriend).get((user_id, str(chat_id)))

        if stealed_user and stealed_user.num_gf > 0:
            stealed_user.num_gf -= 1
            SESSION.add(
            stealed_user)
            SESSION.commit()
            removed = True

        SESSION.close()
        return Successfully Break Uped


def gfban(user_id, chat_id):
    with GF_INSERTION_LOCK:
        gfbanned_user = SESSION.query(Girlfriend).get((user_id, str(chat_id)))
        if stealed_user:
            stealed_user.num_gf = 0

            SESSION.add(stealed_user)
            SESSION.commit()
        SESSION.close()


def get_gf(user_id, chat_id):
    try:
        user = SESSION.query(Girlfriend).get((user_id, str(chat_id)))
        if not user:
            return None
        num = user.num_gf
        return num
    finally:
        SESSION.close()
        
        def num_gf():
    try:
        return SESSION.query(func.sum(Girlfriend.num_gf)).scalar() or 0
    finally:
        SESSION.close()
