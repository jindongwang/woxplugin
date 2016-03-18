#encoding=utf8

from wox import Wox,WoxAPI
from os.path import dirname,join

#用户写的Python类必须继承Wox类 https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#这里的Wox基类做了一些工作，简化了与Wox通信的步骤。
class Main(Wox):

  icon = join(dirname(__file__), "images", "mooncake.png")

  #必须有一个query方法，用户执行查询的时候会自动调用query方法
  def query(self,key):
    if  key == None or len(key) < 3:
        return [
            {
                "Title":"input number",
                "IcoPath":self.icon,
            }
        ]
    if " " not in key:
        return [
            {
                "Title":"input number",
                "IcoPath":self.icon,
            }
        ]
    nums = []
    scales = ["dec","bin","oct","hex"]
    inps = key.split(" ")
    scale = inps[0]
    num = inps[1]
    if scale == "b":
        num10 = int(num,2)
    elif scale == "d":
        num10 = int(num)
    elif scale == "o":
        num10 = int(num,8)
    elif scale == "h":
        num10 = int(num,16)
    else:
        return [
            {
                "Title":"input number",
                "IcoPath":self.icon,
            }
        ]
    nums.append(num10)
    nums.append(bin(num10))
    nums.append(oct(num10))
    nums.append(hex(num10))
    results = list()
    for i in range(4):
        results.append({"Title": scales[i],
                    "IcoPath":self.icon,
                    "SubTitle":nums[i]
                    })
    return results

#以下代码是必须的
if __name__ == "__main__":
  Main()