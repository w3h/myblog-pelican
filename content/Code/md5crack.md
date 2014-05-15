Title: MD5在线破解
Date: 2014-03-18 10:22
Tags: MD5,破解

#### **1、功能介绍**

MD5破解网站更新速度太快，导致很多MD5破解工具，很快就不能使用，因此自己写了一个程序，使用python开发的。参考了大量网上的开源程序和代码，收集了当前网上大部份常用的破解网站，并做了相应的优化和重写，提供了一个简单MD5破解的框架，提高了开发和维护的成本，[github链接][1]，提供的功能如下

1. 支持插件式开发，以方便后期增加和删除

2. 插件模板化，方便大家开发

3. 支持多线程和单线程破解

4. 插件模板中匹配算法并没有使用正则和BeautifulSoup, 而是字符扫描这样对网站的兼容性会更高一些，插件开发过程中也不需要关心正则匹配的问题，只需要抓即网页内容即可

5. 支持Google上搜索MD5值
    
    （注：感谢QQ：374331370兄弟的xmd5账号，不想申请此网站的账号，所以直接使用了）

#### **2、当前支持的插件**

目前支持的插件如下（支持18个插件）：

    > |---------------------------------------------------------------|

    > | [*] MD5 Online Crack by HHH QQ:2969192549                |

    > |---------------------------------------------------------------|

    > [+] site: http://cracker.blackbap.org/        password:No Find

    > [+] site: http://www.hashcracker.org/         password:No Find

    > [+] site: http://www.cmd5.com/                password:No Find

    > [+] site: http://www.md5.com.cn/              password:123

    > [+] site: http://md5.gromweb.com/             password:123

    > [+] site: http://md5decryption.com/           password:123

    > [+] site: http://md5.my-addr.com/             password:123

    > [+] site: http://www.md5-hash.com/            password:123

    > [+] site: http://md5pass.info/                password:123

    > [+] site: http://www.md5this.com/             password:123

    > [+] site: http://www.netmd5crack.com/         password:No Find

    > [+] site: http://www.2d5.net/                 password:123

    > [+] site: http://md5online.net/               password:123

    > [+] site: http://requnix.tk/                  password:123

    > [+] site: http://md5.rednoize.com/            password:No Find

    > [+] site: http://md5.noisette.ch/             password:123

    > [+] site: http://www.xmd5.com/                password:123

    > [+] site: http://www.google.com/              password:123
 

#### **3、使用方法**

    python crack.py  [MD5] [Thread]

    python crack.py  [MD5]

#### **4、插件开发方法**

1、删除插件：

直接删除plugin目录下对应的py文件即可，不需要做任何修改

2、增加插件：

【步骤1】 拷贝插件开发模板“plugin/template.py”重命名

【步骤2】 修改抓取网页部分代码即可，可以使用多种方式抓取，如下图，修改红色框即可


[1]: https://github.com/webhhh/md5crack.git
