# Day39 Web自动化详解（12）——高级篇——实战脚本示例



# 自动化测试

### 

```python
#开展自动化测试需要的工具：
'''
python解释器
selenium包
浏览器
集成开发环境
'''

pip install selenium == 2.48.0
pip uninstall selenium
pip show selenium
#定位（8）
元素属性定位：
	id 、name、class_name
标签名称:
    tag_name
超链接定位：
	link_text、partial_link_text
 元素路径定位：
	Xpath
 css选择器定位：
	css
    
    
from selenium import webdriver
from time import sleep

driver = webdriver.Firefor()
url = 'xxxxx'
driver.get(url)
user=driver.find_element_by_id("userA")
user.send_keys("admin")
sleep(3)
driver.quit()


#
find_element[s]_by_xxx()

eg:
 driver.find_element_by_tag_name("input[1]").send_keys("123456")
=
 driver.find_elements_by_tag_name("input")[1].send_keys("123456")


#
driver.find_element_by_xpth()

//*[@id="userA"]
//*[@id='p1']/input
//*[@id='telA' and @class='telA']
//*[text()="xxx"]          文本内容是xxx的元素
//*[starts-with(@attribute,'xxx')]      属性以xxx开头的元素
//*[contains(@attribute,'Sxxx')]        属性中含有xxx的元素



driver.find_element_by_css_selector()
1. id选择器
2. class选择器
3. 元素选择器
4. 属性选择器
5. 层级选择器
选择器	例子	描述
#id	#userA	id选择器，选择id="userA"的所有元素
.class	.telA	class选择器，选择class="telA"的所有元素
element	input	选择所有input元素
[attribute=value]	[type="password"]	选择type="password"的所有元素
element>element	p>input	选择所有父元素为p元素的input元素

定位方式	XPath	CSS
元素名	//input	input
id	//input[@id='userA']	#userA
class	//*[@class='telA']	.telA
属性	1. //※[text()="xxx"]
2. //※[starts-with(@attribute,'xxx')]
3. //※[contains(@attribute,'xxx')]	
1. input[type^='p']
2. input[type$='d']
3. input[type*='w']


from selenium.webdriver.common.by import By


find_element_by_xxx() 变成
find_element(By.xxx,'xxx')





###综上背一下这个
from selenium import webdriver
from time import sleep

driver = webdriver.Firefor()
url = 'xxxxx'
driver.get(url)
driver.XXXX()#操作浏览器方法

XX1=driver.find_element_by_xxx("XXXXA")
XX1.send_keys("admin")
XX1.clear()
XX1.click()
sleep(3)
driver.quit()

#元素操作
clear()
send_keys()
click()

#WebDriver操作浏览器
maximize_window()
set_window_size(100,100)
set_window_position(300,200)
back()
forward()
refresh()
close()
quit()


#refresh	英[rɪˈfreʃ] 美[rɪˈfreʃ]
#v.	刷新; 使恢复精力; 使凉爽; 重新斟满; 提醒; 提示; 使想起;

#WebDriver其他常用方法
size
text
title
current_url
get_attribute("xxx")
is_display()
is_enabled()

size\text\title\current_url #为属性，调用时无括号 xxx.size
title、current_url #使用浏览器实例化对象直接调用 driver.title

#操作鼠标
context_click() 右击
double_click() 
drag_and_drop() 拖动
move_to_element() 悬停
perform()		执行

from selenium.webdriver.common.action_chains import ActionChains
Action = ActionChains(driver)
element = Action.context_click(username)
element.perform()

#context	英[ˈkɒntekst] 美[ˈkɑːntekst]
#n.	上下文; 语境; (事情发生的)背景，环境，来龙去脉;

1. 源元素   socure=driver.find_element_by_id(xxx)
2. 目标元素 target=driver.find_element_by_id(xxx)
3. 调用方法 Action.drag_and_drop(source,target).perform()



#### 键盘操作
from selenium.webdriver.common.keys import Keys

driver = webdriver.xxx()
driver.find_element_by_xxx("xxx").send_keys(XXX)

send_keys(Keys.BACK_SPACE)
send_keys(Keys.SPACE)
send_keys(Keys.TAB)
send_keys(Keys.ESCAPE)
send_keys(Keys.ENTER)
send_keys(Keys.CONTROL,'a')
send_keys(Keys.CONTROL,'c')
send_keys(Keys.CONTROL,'v')

'''
退格键（英语：Backspace)

space	英[speɪs]
美[speɪs]
n.	空间; (可利用的)空地; 空隙; 空子; 空当; 宽敞; 空旷; 开阔; 外层空间; 一段时间; 空白; 自我支配的自由;
vt.	以一定间隔排列;

tab	英[tæb]
美[tæb]
n.	标签; 签条; 突耳; 凸舌; (待付的)账单，账款; 费用; (尤指)餐厅账单; 药片，药丸(指毒品);
vt.	说(某人)适合于(某工作或角色); 把(某人)视为…; 使用制表键;


escape	英[ɪˈskeɪp]
美[ɪˈskeɪp]
v.	逃跑; (从监禁或管制中)逃走; 逃出; (从不愉快或危险处境中)逃脱; 摆脱; 逃避; 避免(不愉快或危险的事物); 逃脱，幸免于难; 被忘掉; 漏出; （不自觉地）由…发出;
n.	逃脱; 逃避; 逃避现实; 解脱; 消遣; 漏出; 渗出(量); Esc键;

control	英[kənˈtrəʊl] 美[kənˈtroʊl]
vt.	控制; 指挥; 掌管; 支配; 限制; 限定; 阻止蔓延(或恶化); 操纵，控制（机器或系统等）; 抑制;
n.	管制; 管理; (对国家、地区、机构等的)管理权，控制权，支配权; 控制(或操纵)能力; 限制; 限定; 约束; （机器或车辆的）操纵装置，开关，按钮; 对照标准; 指挥（或检查、控制）站; （键盘上的）控制键;
'''

#元素等待
#显式等待（了解）
element = WebDriverWait(driver,timeout ,poll_frequency=0.5).until(EC.presence_of_element_located((By.ID,'userA')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

url = "xxx"
driver = webdriver.xxx()
driver.get(url)
element = WebDriverWait(diver,5).until(EC.presence_of_element_located((By.ID,'userA')))
element.send_keys("admin")


#隐式等待
implicitly_wait(timeout)


##下拉选择框、警告框、滚动条操作

什么是下拉选择框
说明：下拉框就是HTML中<select>元素；

select_by_index()
select_by_value()
select_by_visible_text()

#eg:
from selenium.webdriver.suppor.select import Select
select = Select(webelement)
	webelement: dirver.find_element_by_id("selectA")
select.select_by_xxx(xxx)

说明：WebDriver中对处理警告框的操作，有专用的处理方法；

提示：
    HTML中常用的对话框有三种，处理的方法都一样
        1). alert
        2). confirm
        3). prompt
2.1 警告框处理方法

text
accept()
dismiss()

#eg:
alert = driver.swith_to.alert
alert.text
alert.accept()
alert.dismiss()
'''...
# 定位alerta按钮
driver.find_element_by_id("alerta").click()
# 获取警告框
alert=driver.switch_to.alert
# 打印警告框文本
print(alert.text)
# 接受警告框
alert.accept()
# 取消警告框
#alert.dismiss()
...'''

WebDriver类库中并没有直接提供对滚动条进行操作方法，但是它提供了可调用JavaScript脚本的方法，所以我们可以通过JavaScript脚本来达到操作滚动条的目的；

js = "window.scollTO(0,1000)"
driver.execute_script(js)

...
# 最底层
js1="window.scrollTo(0,1000)"
# 最顶层
js2="window.scrollTo(0,0)"
# 执行最底层
driver.execute_script(js1)
# 执行最顶层
driver.execute_script(js2)
...

frame表单切换、多窗口切换

 1). driver.switch_to.frame("myframe1")        -->    切换表单方法
            (myframe1：为frame表单的name或id)
2). driver.switch_to.default_content()        --> 恢复默认页面方法
            (在frame表单中操作其他页面，必须先回到默认页面，才能进一步操作)
#
a)若iframe具有id属性，直接使用id属性值切换进内层页面
            driver.switch_to.frame(value)/driver.switch_to_frame(value)
b) 定位到iframe元素，再切换进入
            el = driver.find_element_by_xxx(value)
            driver.switch_to.frame(el)    /driver.switch_to_frame(el)
注意：
    switch_to.frame()只能切换到当前页面内嵌的子级页面，若是多级页面的嵌套，需要依次在各页面中通过switch_to.frame()方法切换进入。

#
1. 跳回最外层的页面
    driver.switch_to.default_content() -- 切换到最外层(对于多层页面，可通过该方法直接切换到最外层)
    
2. 跳回上层的页面
    driver.switch_to.parent_frame()   -- 进行向上的单层切换


多窗口切换

方法：
    1). driver.current_window_handle         --> 获取当前窗口句柄
    2). driver.window_handles                 --> 获取所有窗口句柄
    3). driver.switch_to.window(handle)        --> 切换指定句柄窗口



窗口截图
方法：
    1). get_screenshot_as_file(imgpath)            --> 截取当前窗口
        (imgpath：图片保存路径)


1. 打开注册实例.html
2. 切换注册A页面frame表单         --> driver.switch_to.frame(myframe1)
3. 输入注册信息
4. 调用截屏方法                    --> driver.get_screenshot_as_file("../Image/Image01.jpg")



说明：
    1. WebDriver中对cookie操作提供相应的方法

方法：
    1. get_cookie(name)                    --> 获取指定cookie
       (name:为健名)
    2. get_cookies()                    --> 获取本网站所有本地cookies
    3. add_cookie(str)                    -->    添加cookie
       (str：为python中的字典格式)


from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.add_cookie({'name':'BAIDUID','value':'根据实际填写'})
driver.add_cookie({'name':'BDUSS','value':'根据实际填写'})
time.sleep(3)
driver.refresh()
time.sleep(3)



：UnitTest框架是专门用来进行执行代码测试的框架；


1. TestCase
2. TestSuite
3. TextTestRunner
4. Fixture

说明：(翻译：测试用例)一个TestCase就是一条测试用例；
使用：
    1. 导包：import unittest             --> 导入unitest框架
    2. 继承：unittest.TestCase             --> 新建测试类继承unittest.TestCase

提示：
    1). 测试用例：在自动化测试中，一条用例就是一个完整的测试流程；                
    2). 测试方法名称命名必须以test开头；
       (原因：unittest.TestCase类批量运行的方法是搜索执行test开头的方法)





import unittest
from time import sleep
from selenium import webdriver
class TestLoginOut(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        url = "http://localhost/iwebshop/"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("setUp")
    def test_login(self):
        driver=self.driver
        driver.find_element_by_link_text("登录").click()
        driver.find_element_by_css_selector("input[alt*='邮箱']").send_keys("admin")
        driver.find_element_by_css_selector("input[alt*='密码']").send_keys("123456")
        driver.find_element_by_css_selector(".submit_login").click()
        sleep(3)
        driver.find_element_by_css_selector(".reg").click()
    def tearDown(self):
        sleep(2)
        self.driver.quit()
        print("tearDown")
if __name__ == '__main__':
    # 调用main方法执行unitetest内所有test开头方法
    unittest.main()



1. 复制HTMLTestRunner.py文件到项目文件夹
2. 导入HTMLTestRunner、UnitTest包    
3. discover加载要执行的用例
      (discover=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py"))
4. 设置报告生成路径和文件名
   (file_name=file_dir+nowtime+"Report.html")
5. 打开报告 with open(file_name,'wb') as f:
6. 实例化HTMLTestRunner对象：runner=HTMLTestRunner(stream=f,[title],[description])
    参数说明：
               (stream：文件流，打开写入报告的名称及写入编码格式)
               (
                       []，为可选；
                       title为报告标题，如XXX自动化测试报告
                       description：为说明；比如操作系统、浏览器等版本
               )
7. 执行：runner.run(discover)




import time
from CodeEdit.LX04.Tools.HTMLTestRunner import HTMLTestRunner
import unittest
# 加载当前目录
test_dir='.'
# 加载当前目录下iweb开头的.py文件
discover=unittest.defaultTestLoader.dn="test*.py")
if __name__ == '__main__':
    # 定义报告目录
    file_dir="../Report/"
    # 定义报告名称格式
    nowtime=time.strftime("%Y-%m-%d %H_%M_%S")
    # 报告完整路径和名称
    file_name=file_dir+nowtime+"Report.html"
    with open(file_name,"wb")as f:
        # 实例化HTMLTestRunenr对象，传入报告文件流f
        runner=HTMLTestRunner(stream=f,title="iweb_shop项目Web自动化测试报告",description="测试用例共计2条")
        runner.run(discover)



```





```Python
from selenium import webdriver
from time import sleep


#加载驱动
driver = webdriver.Chrome()
#输入网址
url = 'http://10.2.10.7:8081/'
    # 获取url的网页地址
driver.get(url)

#定位输入框
sleep(3)
userId=driver.find_element_by_xpath('//*[@id="UserIDShort"]')
userId.send_keys("180927")

#定位密码框输入密码
driver.find_element_by_xpath('//*[@id="text2"]').send_keys("qwe!23456789")

#点击登录
driver.find_element_by_xpath('//*[@id="modalButton"]').click()

import csv
#读取本地CSv文件（改一下位置喽~）
date = csv.reader(open(r"./a工作/格力互联/qwe.csv","r",encoding='utf-8'))
# 循环输出每一行信息
for user in date:
    print(user)
    print(user[0])
    text=user[0]
    #定位输入框输入关键字
    driver.find_element_by_xpath('//*[@id="searchInput"]').send_keys(text)
    sleep(2)
    #点击下拉框这里可能会点击错  （ul--前端无序排列）
    driver.find_element_by_xpath('//*[@id="mainContent"]/div[3]/div/div[1]/div/div[2]/ul').click()
    #5秒检查时间
    sleep(5)
    print(user[0]+"测试完毕")
    #情况搜索框方便下次搜索
    driver.find_element_by_xpath('//*[@id="searchInput"]').clear()
    sleep(1)
    # driver.switch_to_default_content()
    # driver.switch_to.active_element().sendkeys("180981")


sleep(120)
# 关闭浏览器
driver.close()
# 关闭浏览器及驱动程序
driver.quit()
```









































































