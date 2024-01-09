from mycroft import MycroftSkill, intent_file_handler


class Easyshop(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('easyshop.intent')
    def handle_easyshop(self, message):
        self.speak_dialog('easyshop')


def create_skill():
    return Easyshop()

