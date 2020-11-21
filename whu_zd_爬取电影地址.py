import urllib.request
import re


def get_movie_links():
    """获取列表影片信息"""
    # 1.定义列表的地址
    # https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html
    film_list_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
    # 2.打开url地址，获取数据
    response_list = urllib.request.urlopen(film_list_url)
    # 通过read()读取网络资源数据
    response_list_data = response_list.read()
    # 3.解码获取得到的数据
    response_list_text = response_list_data.decode("GBK")
    # 4.使用正则得到所有影片内容地址
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>", response_list_text)
    print(url_list)
    # 定义字典
    films_dict = {}
    i = 1
    # 循环遍历列表得到
    for content_url, film_name in url_list:
        # 拼接内容页面地址
        content_url = "https://www.ygdy8.net/" + content_url
        # print("影片名称：%s,内容地址： %s" % (film_name, content_url))
        # 打开内容页面
        response_content = urllib.request.urlopen(content_url)
        # 接受数据
        response_content_data = response_content.read()
        # 解码得到数据
        response_content_text = response_content_data.decode("GBK")
        result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*?)\">", response_content_text)
        films_dict[film_name] = result.group(1)
        print("已经获取第%d条信息" % i)
        i += 1
    return films_dict


def main():
    films_dict = get_movie_links()
    for film_name, film_link in films_dict.items():
        print("%s | %s" % (film_name, film_link))


if __name__ == '__name__':
    main()
