import os, unittest, yagmail, HTMLTestReportCN
from bs4 import BeautifulSoup
from datetime import datetime

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="testcase/", pattern="*TestCase.py")
    suite.addTests(tests)

    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    reporter_generator_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    reporter = r"{0}\report\startBBs自动化测试_{1}.html".format(BASE_DIR, reporter_generator_time)
    fp = open(reporter, 'wb')
    runner = HTMLTestReportCN.HTMLTestRunner(
        stream=fp,
        title='startBBs自动化测试报告',
        description='本轮测试的测试点主要为：注册模块、登录模块、发表模块。',
        tester='FanDeyi'
        )
    runner.run(suite)
    fp.close()

    yag = yagmail.SMTP(user="fan_de_yi@163.com", password="fandeyi520", host="smtp.163.com")
    soup = BeautifulSoup(open(reporter, encoding="utf-8"), features="html.parser")
    subject = soup.h1.get_text()
    contents = " ".join(str(i) for i in soup.select("div.heading>p"))
    attachments = reporter
    # 将邮件发送给xxx人：收件人信息
    yag.send('fdy19930621@gmail.com', subject, contents, attachments,)