from threading import Thread


"""
PhantomJSはseleniumのタイムアウト設定がきかないみたいなので、スレッド化してタイムアウトを実装する
使い方は、呼び出し元でこのスレッドをstartしたあとにjoin(timeout=x)
x秒joinで待った後、self.reの値を見て、状況を把握する
戻り値(self.re)がいらないなら、クラスじゃなくて関数でもいい
"""
class PhantomGetThread(Thread):
    def __init__(self, phantom_driver, url):
        super(GetPhantomThread, self).__init__()
        self.phantom_driver = phantom_driver
        self.url = url
        self.re = False

    def run(self):
        try:
            self.phantom_driver.get(self.url)
        except Exception as e:
            self.re = e
        else:
            self.re = True
