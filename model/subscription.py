def create_subscription(uid: str):
def get_subscription(uid: str):
def delete_subscription(uid: str):

class Subscription:
    def __init__(self, dict: dict):
        self.object_id = dict['object_id'];
        self.subscription_id = dict['subscription_id'];
        self.aspect = dict['aspect'];
        self.callback_url = dict['callback_url'];
        self.object = dict['object'];
        self.type = dict['type'];
        self.id = dict['id'];

    def delete(self):
        return self.uid
