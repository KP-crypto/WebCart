import configparser

config=configparser.RawConfigParser()
config.read("C:/Users/Acer/PycharmProjects/wpmobil/configuration/config.txt")

class Readconfig:

    @staticmethod
    def getApplicationURL():

        url=config.get('common info','URL')
        return url








