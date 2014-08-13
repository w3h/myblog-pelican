Title: [原创]插件式木马PTrojan
Date: 2014-08-13 19:22
Tags: PTrojan

受一个同事的启发，原创插件式木马PTrojan，花费了我几个周末，调试和修改代码，终于今天如期见天日了。源代码基于gh0st V3.6修改而成。

**（一）插件式木马概念解析**

服务器端仅支持一个反向连接功能，其它的功能都由控制端以插件的方式进行远程进行加载。这样可以带来几个好处

1. 服务端程序功能单一，所以木马可以做得很小很小

2. 服务端程序由于小，所以做免杀很容易

3. 插件可以远程加载和卸载，隐蔽性会很强

4. 插件可以根据被控端的情况实时修改，适应性会很强，随时可以做免杀


**（二）功能如下**

1. 支持以插件式开发木马服务器端功能

2. 可以过win2008 UAC

3. 支持控制端随时加载和卸载服务器的插件

4. 源程序控制端和服务端都在vc++ 6.0 和 VS2010 上编译通过

5. 当前支持的插件有PluginFileManager.dll（文件管理插件） PluginScreenManager.dll（远程屏幕插件） PluginShellManager.dll（远程终端插件）


**（三）软件展示**

**1、插件加载菜单**

   ![ALT TEXT](/static/images/PTrojan-1.gif)
 
**2、插件加载对话框**

   ![ALT TEXT](/static/images/PTrojan-2.gif)

**3、插件前后对比(点击加载插件)**

   ![ALT TEXT](/static/images/PTrojan-3.gif)


   ![ALT TEXT](/static/images/PTrojan-4.gif)


   ![ALT TEXT](/static/images/PTrojan-5.gif)


