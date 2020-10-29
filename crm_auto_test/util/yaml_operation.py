import yaml

from util.auto_log import AutoLog


class YamlOperation():
    def __init__(self, locator_file):
        self.log=AutoLog()
        with open(locator_file,encoding="UTF-8") as yaml_file:
            self.data = yaml.load(yaml_file, yaml.FullLoader)

    def get_locatoer(self, page, local):
            try:
                local=self.data[page][local]
                self.log.set_messge("yaml:{} 读取成功".format(local),"info")
                return local
            except Exception as e:
                self.log.set_messge(e, "error")


if __name__ == '__main__':
    y = YamlOperation("../config/locator.yaml")
    print(y.get_locatoer("LoginPage", "username"))
