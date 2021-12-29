class TemplateEngine:
    def make_msg(self, client, msg):
        pass


class MailServer:
    def send_msg(self, msg_dict):
        pass

    def get_msg(self, client):
        pass


def all_strings(list_of_args: list):
    return all(isinstance(some_arg, str) for some_arg in list_of_args)


class Messenger:
    def __init__(self):
        self.template = TemplateEngine()
        self.server = MailServer()

    def send_msg(self, client: str, msg: str):
        if all_strings([client, msg]):
            self.server.send_msg(self.template.make_msg(client, msg))
        else:
            raise TypeError

    def receive_msg(self, client: str):
        if all_strings([client]):
            self.server.get_msg(client)
        else:
            raise TypeError
