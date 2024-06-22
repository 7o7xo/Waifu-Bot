class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1813373023"
    sudo_users = "1813373023"
    GROUP_ID = -1002103727164
    TOKEN = "7191385539:AAFltreD07ywamDRqqNsKbX9PSeZ3RRlZCg"
    mongo_url = "mongodb+srv://Villan:villan654@villen.ifsk8q0.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL =["https://telegra.ph/file/469cd413260ce9c675ca3.jpg", "https://telegra.ph/file/ffc54f46e63067f787258.jpg"]
    SUPPORT_CHAT = "FallenXDeveloper"
    UPDATE_CHAT = "FallenXDeveloper"
    BOT_USERNAME = "Keqing_WaifuBot"
    CHARA_CHANNEL_ID = "--1002236858053"
    api_id = 21846639
    api_hash = "2cebc99bd8378b5237b31ea8e7496d79"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
