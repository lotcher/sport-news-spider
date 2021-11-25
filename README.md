# sport news spider

> 爬取常见体育网站新闻列表[腾讯体育、虎扑]，解析为格式化内容：标题、内容、插图、发表时间...

## 使用方式

1. 克隆项目到本地，进入项目根目录安装依赖

```shell
pip3 install -r requirements.txt
```

2. 修改config/default.yaml为需要的配置（爬取参数、输出方式），或者自建一个yaml配置文件

![image-20211125174708759](http://lbj.wiki/static/images/a822c8c0-4dd4-11ec-9928-00163e30ead3.png)

3. 进入src目录，运行项目

```shell	
python3 main.py
```

<img src="http://lbj.wiki/static/images/e57d6b12-4dd4-11ec-9928-00163e30ead3.png" alt="image-20211125174851691" style="zoom:50%;" />

## 运行效果

![image-20211125174930337](http://lbj.wiki/static/images/fc8f8574-4dd4-11ec-9928-00163e30ead3.png)

![image-20211125175025321](http://lbj.wiki/static/images/1dee8a80-4dd5-11ec-9928-00163e30ead3.png)

## 其他

* 爬取数据仅为交流学习，切勿商用
* 默认无并发及代理
