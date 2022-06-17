# requests-cache
是 requests 库的一个扩展包，利用它我们可以非常方便地实现请求的缓存，直接得到对应的爬取结果。

    GitHub：https://github.com/reclosedev/requests-cache
    PyPi：https://pypi.org/project/requests-cache/
    官方文档：https://requests-cache.readthedocs.io/en/stable/index.html

# Patch 写法
>./requests_test/request_demo.py
我们在写的时候把 requests 的 session 对象直接替换了。有没有别的写法呢？比如我不影响当前代码，只在代码前面加几行初始化代码就完成 requests-cache 的配置呢？

requests_cache.install_cache('demo_cache')
这次我们直接调用了 requests-cache 库的 install_cache 方法就好了，其他的 requests 的 Session 照常使用即可。

# 后端配置
刚才我们知道了，requests-cache 默认使用了 SQLite 作为缓存对象，那这个能不能换啊？比如用文件，或者其他的数据库呢？
    requests_cache.install_cache('demo_cache', backend='filesystem')
这里我们添加了一个 backend 参数，然后指定为 filesystem，这样运行之后本地就会生成一个 demo_cache 的文件夹用作缓存，如果不想用缓存的话把这个文件夹删了就好了。

    requests_cache.install_cache('demo_cache', backend='filesystem', use_temp=True)
这里添加一个 use_temp 参数，缓存文件夹便会使用系统的临时目录，而不会在代码区创建缓存文件夹。

    requests_cache.install_cache('demo_cache', backend='filesystem', use_cache_dir=True)
这里添加一个 use_cache_dir 参数，缓存文件夹便会使用系统的专用缓存文件夹，而不会在代码区创建缓存文件夹。

# Filter
    requests_cache.install_cache('demo_cache2', allowable_methods=['POST'])
这里我们添加了一个 allowable_methods 指定了一个过滤器，只有 POST 请求会被缓存，GET 请求就不会。



url(more link)[https://mp.weixin.qq.com/s/yGnMq9gKsDvn2jqbWPbmzw]