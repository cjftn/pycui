import os
def user():
    inp=input('''
    0.���
    1.����� �߰�
    2.�׷� �߰�
    3.����� ����
    4.�׷� ����
    5.�׷쿡 ����� �߰�
    6.������ ���� �׷� ��ȸ
    7.��� ��ȣ ����
    �Է����ּ���>''')
    if(inp=='2'):
        name=input("�߰��� �׷��� �̸��� �Է� �ϼ���")
        os.system("sudo groupadd  "+name)
    elif(inp=='5'):
        name=input("�׷쿡 �߰��� ����ڸ� �Է� �ϼ���")
        nam=input('�׷��� �̸��� �Է� �ϼ���')
        os.system('sudo adduser '+name+" "+nam)
    elif(inp=='3'):
        name=input('������ ����� �̸��� �Է� �ϼ���')
        os.system('sudo deluser --remove-home '+name)
    elif(inp=='4'):
        name=input("������ �׷� �̸��� �Է� �ϼ���")
        os.system('sudo groupdel '+name)
    elif(inp=='0'):
        start()
    elif(inp=='1'):
        name=input("�߰��� ����ڸ� �Է��ϼ���")
        os.system('sudo adduser '+name)
    elif(inp=='6'):
        name=input('�׷��� ��ȸ�� ������� �̸��� �Է� �ϼ���')
        os.system('sudo groups '+name)
    elif(inp=='7'):
        name=input('��й�ȣ�� ������ ������� �̸��� �Է��ϼ���')
        os.system('sudo passwd '+name)
    else:
        print("�߸� �Է� �Ͽ����ϴ�.")


def start():
    inp = input('''
    0.����
    1.cpu�µ� Ȯ��
    2.gpu�µ� Ȯ��
    3.ipȮ��
    4.gpioȮ��
    5.������Ʈ
    6.�� ������
    7.����� ����
    8.���̼� ����
    9.�ʱ� ȯ�� ����
    �Է����ּ���>''')
    if (inp == '1'):
        os.system('vcgencmd measure_temp')
    elif (inp == '2'):
        os.system('/opt/vc/bin/vcgencmd measure_temp')
    elif(inp == '3'):
        os.system('ifconfig')
    elif(inp == '0'):
        exit()
    elif(inp == '4'):
        os.system('pinout')
    elif(inp=='5'):
        os.system('sudo apt upgrade -y')
        os.system('sudo apt update -y')
        os.system('sudo apt-get upgrade -y')
        os.system('sudo apt-get update -y')
    elif(inp=='6'):
        os.system('sudo apt-get install w3m -y')
        os.system('w3m google.co.kr')
    elif(inp=='7'):
        user()
    elif(inp=='8'):
        os.system('sudo raspi-config')
    elif(inp=='9'):
        #os.system('chmod +x pycui.py')#���� ���Ϸ� ����
        os.system('sudo cp pycui /usr/local/bin/')
        #os.system('sudo mv /usr/local/bin/pycui.py /usr/local/bin/pycui')
    else:
        print("�߸� �Է� �Ͽ����ϴ�.")
    start()
start()
