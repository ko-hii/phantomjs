from threading import Thread


class PhantomGetThread(Thread):
    """
    PhantomJSはseleniumのタイムアウト設定がきかないみたいなので、スレッド化してタイムアウトを実装する
    使い方としては、呼び出し元でこのスレッドをrunしたあとにjoin(timeout=x)
    x秒joinで待った後、self.reの値を見て、状況を把握する
    """
    def __init__(self, phantom_driver, url):
        super(PhantomGetThread, self).__init__()
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
            
    """
    使い方
    driver = (略)
    url = (略)
    t = phantom_get.PhantomGetThread(driver, url)
    t.start()
    t.join(timeout=60)   # 60秒のget待機時間
    if t.re is False:
        print('time out')
    elif t.re is True:
        print('ok')
    else:
        print('error : ' str(t.re))
    """
