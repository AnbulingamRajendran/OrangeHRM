import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\conf.ini")


class readConfig:
    @staticmethod
    def getUrl():
        url = config.get('url_credentials', 'url')
        return url

    @staticmethod
    def getUsername():
        username = config.get('url_credentials', 'username')
        return username

    @staticmethod
    def getPassword():
        username = config.get('url_credentials', 'password')
        return username
