# sspanel自动签到

> 登陆、签到核心代码来自：https://github.com/zhjc1124/ssr_autocheckin
>
> yml、教程 来自：https://github.com/t00t00-crypto/cloud189-action
>
> 以上仓库已star感谢

## Github Actions 部署指南

### 一、Fork 此仓库
![image-20200727142541791](https://i.loli.net/2020/07/27/jK5H8FLvt7aBeYX.png)



### 二、设置账号密码
添加名为 **HOST**、**USER**、**PWD** 的变量，值分别为 **网址**、**登陆邮箱**、**密码 **。注意：点击 **update** 不会显示上次的值，每次修改都必须重新输入整个值。

> Settings-->Secrets-->New secret

![image-20200727142753175](https://i.loli.net/2020/07/27/xjri3p4qdchaf2G.png)

~~支持多账号，账号之间与密码之间用 ***换行*** 分隔，**网址**、**账号**与**密码**的个数要对应。

示例：**HOST:**

> https://example.com
>
> https://example-2.com



### 三、启用 Action
1. 点击 ***Actions***，再点击 **I understand my workflows, go ahead and enable them**

   ![](https://i.loli.net/2020/07/27/pyQmdMHrOIz4x2f.png)

2. 点击左侧的 ***Star***

   ![image-20200727142617807](https://i.loli.net/2020/07/27/3cXnHYIbOxfQDZh.png)

### 四、查看运行结果
> Actions --> 签到 --> build
>
> 能看到如下图所示，表示成功

![image-20200727144951950](https://i.loli.net/2020/07/27/VbrHu8UJXiIkqGx.png)

## 注意事项

1. 每天运行两次，在上午 6 点和晚上 22 点。

2. 可以通过 ***Star*** 手动启动一次。

   ![image-20200727142617807](https://i.loli.net/2020/07/27/87oQeLJOlZvU3Ep.png)
