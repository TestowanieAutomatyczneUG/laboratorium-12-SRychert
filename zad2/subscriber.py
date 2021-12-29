class Subscriber:
    def __init__(self):
        self.clients = []

    def add_client(self, client: str):
        if isinstance(client, str):
            if client not in self.clients:
                self.clients.append(client)
                return self.clients
            else:
                raise ValueError
        else:
            raise TypeError

    def delete_client(self, client: str):
        if isinstance(client, str):
            if client in self.clients:
                self.clients.remove(client)
                return self.clients
            else:
                raise ValueError
        else:
            raise TypeError

    def msg_client(self, client: str, msg: str):
        if isinstance(client, str) and isinstance(msg, str):
            if client in self.clients:
                pass
            else:
                raise ValueError
        else:
            raise TypeError
