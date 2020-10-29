import logging
import time


class AutoLog:

    logger = logging.getLogger("log")
    @classmethod
    def set_messge(self,msg,level):
        global fh
        try:
            now_date = time.strftime("%Y-%m-%d", time.localtime())
            # 创建文件handle
            fh = logging.FileHandler("../../log/auto{}.log".format(now_date),encoding="UTF-8")
            # 创建控制台
            ch = logging.StreamHandler()
            # 格式化
            fm = logging.Formatter("%(levelname)s %(asctime)s %(message)s")
            # 对文件格式化
            fh.setFormatter(fm)
            # 对控制台格式化
            ch.setFormatter(fm)
            # 文件句柄加入logger
            AutoLog.logger.addHandler(fh)
            # 控制台句柄加入logger
            AutoLog.logger.addHandler(ch)
            # 设置打印级别
            AutoLog.logger.setLevel(logging.DEBUG)
            # 输入info
            if level=="debug":
                self.logger.debug(msg)
            elif level=="info":
                self.logger.info(msg)
            elif level=="error":
                self.logger.error(msg)
            elif level=="critical":
                self.logger.critical(msg)
            elif level=="warning":
                self.logger.warning(msg)
            # 移除文件句柄
            self.logger.removeHandler(fh)
            # 移除控制台对象
            self.logger.removeHandler(ch)
        except:
            print("file exception")
        finally:
            fh.close()

