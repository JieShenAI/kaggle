# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/22 14:39

"""
1. 根据给的csv文件的url地址进行下载
2. 转换成pytorch类型
3. data,label放到一起

"""

# 检查文件是否存在已经有了就无需下载
import hashlib
import os
import urllib
from typing import Optional, Any, Dict
import urllib.error
import urllib.request

from tqdm import tqdm


@property
def class_to_idx(self) -> Dict[str, int]:
    return {_class: i for i, _class in enumerate(self.classes)}


def _check_exists(self) -> bool:
    return all(
        check_integrity(os.path.join(self.raw_folder, os.path.splitext(os.path.basename(url))[0]))
        for url, _ in self.resources
    )


resources = [
    ("train-images-idx3-ubyte.gz", "f68b3c2dcbeaaa9fbdd348bbdeb94873"),
    ("train-labels-idx1-ubyte.gz", "d53e105ee54ea40749a09fcbcd1e9432"),
    ("t10k-images-idx3-ubyte.gz", "9fb629c4189551a2d022fa330f9573f3"),
    ("t10k-labels-idx1-ubyte.gz", "ec29112dd5afa0611ce80d1b7f02629c")
]


# 　完整性检测函数
def calculate_md5(fpath: str, chunk_size: int = 1024 * 1024) -> str:
    md5 = hashlib.md5()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()


def check_md5(fpath: str, md5: str, **kwargs: Any) -> bool:
    return md5 == calculate_md5(fpath, **kwargs)


def check_integrity(fpath: str, md5: Optional[str] = None) -> bool:
    if not os.path.isfile(fpath):
        return False
    if md5 is None:
        return True
    return check_md5(fpath, md5)


USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 " \
             "Safari/537.36 "


def _urlretrieve(url: str, filename: str, chunk_size: int = 1024) -> None:
    with open(filename, "wb") as fh:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": USER_AGENT})) as response:
            with tqdm(total=response.length) as pbar:
                for chunk in iter(lambda: response.read(chunk_size), ""):
                    if not chunk:
                        break
                    pbar.update(chunk_size)
                    fh.write(chunk)


class csv_dataset:
    '''
        有待完善：
            增加csv文件读取的功能
            抽取出label的功能
    '''

    def __init__(self, root, train, filename, url=None, download=False):
        self.root = root
        self.download = download
        self.url = url
        self.train = train
        self.filname = filename
        self._download()
        # 检查指定路径的文件是否存在，存储在根目录下

    def _download(self):
        self.__exists()
        url = self.url
        fpath = os.path.join(self.root, self.filname)
        # download the file
        try:
            print('Downloading ' + url + ' to ' + fpath)
            _urlretrieve(url, fpath)
        except (urllib.error.URLError, IOError) as e:  # type: ignore[attr-defined]
            if url[:5] == 'https':
                url = url.replace('https:', 'http:')
                print('Failed download. Trying https -> http instead.'
                      ' Downloading ' + url + ' to ' + fpath)
                _urlretrieve(url, fpath)
            else:
                raise e

    def __exists(self):
        if os.path.exists(self.root):
            # 存在该文件夹
            # 判断是否存在该文件
            if os.path.exists(os.path.join(self.root, self.filname)):
                raise "该文件已存在"
        # 该文件不存在，创建该文件夹
        os.makedirs(self.root, exist_ok=True)


if __name__ == '__main__':
    # csv_url = "https://storage.googleapis.com/kagglesdsdata/datasets/1879002/3069714/soildataset.csv"
    img_url = "https://image.baidu.com/search/down?tn=download&ipn=dwnl&word=download&ie=utf8&fr=result&url=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fpic3.zhimg.com%252Fv2-2552125e1dda7c60cfb15674aaa81862_b.jpg%26refer%3Dhttp%253A%252F%252Fpic3.zhimg.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Djpeg%3Fsec%3D1645266125%26t%3D9310fa7430f27b9a6acb530d41033453&thumburl=https%3A%2F%2Fimg2.baidu.com%2Fit%2Fu%3D2506974231%2C1410615315%26fm%3D253%26fmt%3Dauto%26app%3D138%26f%3DJPEG%3Fw%3D215%26h%3D205"
    dataset = csv_dataset(root="jieshen", url=img_url, download=True, train=True, filename="1.jpeg")
