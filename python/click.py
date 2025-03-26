from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def create_driver(openUrl):
    try:
        # 创建 Chrome 配置对象
        chrome_options = Options()
        
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # 添加无痕模式参数
        chrome_options.add_argument("--incognito")

        service = Service('./chromedriver-win32/chromedriver.exe')

        # 创建浏览器实例
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # 访问连接
        driver.get(openUrl[0])
        
        # 保持浏览器窗口打开(直到手动关闭或程序结束)
        input("按回车键关闭浏览器...")
        
    except Exception as e:
        print(f"发生错误: {e}")
    finally:
        # 关闭浏览器
        try:
            driver.quit()
        except:
            pass