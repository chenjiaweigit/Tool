import requests,os,time,random
from PIL import Image
from io import BytesIO

lx = random.choice(['a1','b1','c1','c2','c3'])#	输出头像类型[a1（男头）|b1（女头）|c1（动漫头像）|c2（动漫女头）|c3（动漫男头）]默认为c1
we = requests.get(url=f'https://api.btstu.cn/sjtx/api.php?lx={lx}&format=images')
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
        with open(filename,'wb') as f:
            f.write(we.content)
            f.close()
            print("头像已成功保存到:"+file_path)
    else:
        print('头像保存失败')
except:
    print('头像保存失败')

