# py-msf-tool
* 需在Linux运行此py代码，Linux需要安装nmap和msfconsole不是特殊版本是自带python3,也可在kali直接运行

## 作用
* 这是一个通过python使用nmap和msfconsole自动渗透windows7或者windows server 2008操作系统取C://flagvalues.txt可以替换直接想要执行的指令-c是windows指令-C是linux指令下面（只能渗透未打补丁的系统）
* 目前仅支持Linux系统
* 扫描的时候严格按照提示输入网段
* 渗透进去后可以使用sessions进行批量运行命令
* 将来应该不会再更新了因为发现了更好用的msfrpc

* 本程序电影于学习交流，请勇于坚守《网络安全法》，勿使中华人民共和国工具非授权的测试，开发者不负任何连带法律责任。
* 好好学习,天天向上！

# 运行方法

## 方法一

* ```shell
  ./automsf.py
  ```

## 方法二

* ```shell
  python3 automsf.py
  ```

## 替换为windows指令

```
从
config.write("sessions -C 'cat C://flagvalue.txt'"+"\n")
替换成：
config.write("sessions -c 'cmd.exe /c type C://flagvalue.txt'" + "\n")
```

