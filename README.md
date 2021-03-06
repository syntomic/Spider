## Python爬虫
- [理论基础](spider.md): 大规模,自动化复制粘帖
    - 爬取
        - 网页
            - 服务端渲染
            - 客户端渲染: Ajax Selenium
        - APP: 接口
    - 解析
        - re/Xpath/CSS Selector
        - 智能解析
    - 反爬
        - 非浏览器检测
        - 封IP
            - 手机站点
            - [代理池](https://github.com/syntomic/Spider/tree/master/ProxyPool/)
        - 验证码: 打码平台
        - 封帐号
            - [Cookies池](https://github.com/syntomic/Spider/tree/master/CookiesPool/)
    - 存储
        - 文件
        - 数据库
        - 搜索引擎
    - 加速
        - 优化: DNS缓存
        - 多线程/进程
        - 异步
        - 分布式: Scrapy-Redis-BloomFliter
        - 部署
            - Docker
- 实战项目
    - [猫眼电影Top100](https://github.com/syntomic/Spider/tree/master/MaoYan/)
        - 利用requests和正则表达式抓取
    - [今日头条街拍](https://github.com/syntomic/Spider/tree/master/JiePai/)
        - 存储图片: 多进程
    - [水木社区](https://github.com/syntomic/Spider/tree/master/Newsmth/)
        - 全站抓取: 深度优先 vs 宽度优先
    - [GitHub登录](https://github.com/syntomic/Spider/tree/master/GitHubLogin/)
        - 保持会话：`requests.Session()`
        - 验证Token
    - [淘宝商品](https://github.com/syntomic/Spider/tree/master/TaobaoProduct/)
        - Selenium: 设置开发者选项
        - 绑定账号登录
    - 利用Scrapy框架
        - [Scrapy入门](https://github.com/syntomic/Spider/tree/master/ScrapyTutorial/): 各个模块独立,结合任务调度, 就形成了框架
        - [python职位](https://github.com/syntomic/Spider/tree/master/PythonJob/)
            - 51job
            - 拉钩网
            - 智联招聘
            - Boss直聘
        - [360美图](https://github.com/syntomic/Spider/tree/master/Images360/)
            - Image Pipeline：支持异步和多线程
        - [新浪微博](https://github.com/syntomic/Spider/tree/master/Weibo): 对接Cookies池和代理池
            - [分布式](https://github.com/syntomic/Spider/tree/master/Weibo-distributed/)
                - 利用Scrapy-Redis实现分布式队列、调度器、去重
                - 利用Scrapyd分布式部署
