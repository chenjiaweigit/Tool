import requests,os,time,random
from io import BytesIO
import tkinter as tk
from tkinter.messagebox import *
from tkinter.simpledialog import *
from PIL import Image
class Random_avatar:

    def head_type(self):
        root = Tk()
        root.title('头像类型选择')
        group = LabelFrame(root, text='选择你喜欢的头像类型', padx=5, pady=5)
        screenwidth = root.winfo_screenwidth()  # 屏幕宽度
        screenheight = root.winfo_screenheight()  # 屏幕高度
        width = 200
        height = 200
        x = int((screenwidth - width) / 2)
        y = int((screenheight - height) / 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        group.pack(padx=20, pady=20)

        #	输出头像类型[a1（男头）|b1（女头）|c1（动漫头像）|c2（动漫女头）|c3（动漫男头）]默认为c1
        LANGS = [
            ('男生头像',0),
            ('女生头像', 1),
            ('动漫头像', 2),
            ('动漫女头', 3),
            ('动漫男头', 4)]
        # print(type(LANGS))
        v = IntVar()

        for lang, num in LANGS:
            # b = Radiobutton(group, text=lang, variable=v, value=num,indicatoron=False,command=root.quit) #应用程序结束关闭
            b = Radiobutton(group, text=lang, variable=v, value=num,selectcolor='black',indicatoron=False,command=root.destroy)  #循环结束只关闭mainloop小部件
            # fill=X设置和其父窗口一样宽, 可以使用 fill=X 属性
            b.pack(anchor=W)
        root.mainloop()
        return v.get()
    # print(head_type())

    def tou(self):
        lx = ['a1','b1','c1','c2','c3']

        # lx = random.choice(['a1','b1','c1','c2','c3'])# 随机选择头像类型
        we = requests.get(url=f'https://api.btstu.cn/sjtx/api.php?lx={lx[Random_avatar().head_type()]}&format=images')
        image = Image.open(BytesIO(we.content))
        image.show()

        file_path  = os.path.dirname(__file__)+'/img'
        img_url = we.url
        file_name = 'portrait'+''+str(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        file_suffix = os.path.splitext(img_url)[1]
        filename = '{}{}{}{}'.format(file_path, os.sep, file_name, file_suffix)
        try:
            if not os.path.exists(file_path):
                os.mkdir(file_path)
            if not os.path.exists(filename):
                time.sleep(1)
                result = askquestion(title='提示', message='是否保存到本地？')
                if result == 'yes':
                    with open(filename,'wb') as f:
                        f.write(we.content)
                        f.close()
                        print("头像已成功保存到:"+file_path)
                elif result == 'no':
                    print('保存已取消！')
            else:
                print('头像保存失败！')
        except:
            print('头像保存失败！')
if __name__ == '__main__':
    Random_avatar().tou()