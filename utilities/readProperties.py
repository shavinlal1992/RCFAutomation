import configparser

config=configparser.RawConfigParser()

config.read('.\\Configurations\\config.ini')

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url=config['DEFAULT']['baseURL']
        return url

    @staticmethod
    def getUseremail():
        username=config['DEFAULT']['username']
        return username

    @staticmethod
    def getUserpassword():
        password=config['DEFAULT']['password']
        return password