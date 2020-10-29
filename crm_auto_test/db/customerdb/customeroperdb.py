from util.db_operation import DbOperation


class CustomerOperationDb:
    def __init__(self):
        self.dbop=DbOperation()

    def dele_customer(self):
        self.dbop.update("....")