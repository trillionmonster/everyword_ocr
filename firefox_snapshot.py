from pymouse import PyMouse
from pykeyboard import PyKeyboard

from selenium import webdriver
import time
import base64

def capture(url, save_fn="capture.png"):
    mouse = PyMouse()
    keyboard = PyKeyboard()

    browser = webdriver.Firefox(executable_path = '/home/wws/Soft/geckodriver')  # Get local session of firefox

    browser.set_window_size(1900, 900)
    browser.get(url)

    mouse.click(300, 250)
    # Load page
  #   browser.execute_script("""
  #   (function () {
  #     var y = 0;
  #     var step = 100;
  #     window.scroll(0, 0);
  #
  #     function f() {
  #       if (y < document.body.scrollHeight) {
  #         y += step;
  #         window.scroll(0, y);
  #         setTimeout(f, 50);
  #       } else {
  #         window.scroll(0, 0);
  #         document.title += "scroll-done";
  #       }
  #     }
  #
  #     setTimeout(f, 1000);
  #   })();
  # """)
  #   browser.execute_script()

    # browser.save_screenshot('first.png')
    keyboard.press_keys([keyboard.shift_key,'F2'])
    # keyboard.release_keys(["Shift","F2"])
    # png = base64.b64decode(browser.execute('screenshot --fullpage')['value'].encode('ascii'))
    # with open('first1.png', 'wb') as f:
    #     f.write(png)
    # # browser.execute("screenshot")
    #
    # keyboard.press_key(keyboard.page_down_key)
    # keyboard.release_key(keyboard.page_down_key)
    # time.sleep(1)
    # browser.save_screenshot('second.png')
    # browser.close()
    time.sleep(1)
    keyboard.type_string("screenshot --fullpage /home/wws/workspace/git/SPIDER/Crawler-master/amazon/fullpage.png")

    keyboard.press_key(keyboard.enter_key)
    keyboard.release_key(keyboard.enter_key)
    time.sleep(1)
    # browser.close()

if __name__ == "__main__":
    capture("https://www.amazon.cn")
