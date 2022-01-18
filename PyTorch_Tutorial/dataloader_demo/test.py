# _*_coding     : UTF_8_*_
# Author        :Jie Shen
# CreatTime     :2022/1/20 16:27
import os
import urllib

from deprecated import deprecated
import warnings

from torch.utils.model_zoo import tqdm


class stu:
    def __init__(self):
        self.age = 12
        self.__name = "j"

    def __repr__(self) -> str:
        return repr(self.age) + repr(self.name)

    @deprecated
    def name(self):
        # warnings.warn("some_old_function is deprecated", DeprecationWarning)
        return self.__name


def _urlretrieve(url: str, filename: str, chunk_size: int = 1024) -> None:
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    with open(filename, "wb") as fh:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": USER_AGENT})) as response:
            with tqdm(total=response.length) as pbar:
                for chunk in iter(lambda: response.read(chunk_size), ""):
                    if not chunk:
                        break
                    pbar.update(chunk_size)
                    fh.write(chunk)


if __name__ == '__main__':
    url = "https://img2.baidu.com/it/u=2506974231,1410615315&fm=253&fmt=auto&app=138&f=JPEG?filename=1.jpg"
    # _urlretrieve(url, "for.jpg")
    basename = os.path.basename(url)
    print(basename)
