# -- coding: utf-8 --
# if elif else���
age = 100
message = ""
if age < 18:
	message = "you are very young"
elif age < 30:
	message = "you are not old"
else:
	message = "you are old"
print message;

if 1: # �κη��㣬�ǿյģ����б�����Ϊ�յ������Ƿ���True,���򷵻�False
	print "1��True"

if '1988' < 2000:
	print "'1988' < 2000" # ������������Ϊ�ַ������ܺ����ֱȽϣ��Ƚ���ֵ�᲻��ȷ
else:
	print "'1988' >= 2000"

num = int("19") # ����ͨ��int()�������ַ���ת��������


# whileѭ��

index = 8
while index > 0:
	print index
	index -= 1

# forѭ��
names = ["name1","name2","name3","name4"]
for name in names:
	print name

# range()������ʹ��
nums = [0,1,2,3,4] # ����һ���б�
nums = range(5) # ����һ��������һ�����б�

# ����range�Ĺ��򣬾Ϳ������forѭ�������±�ĵ�����
names = ["��־��1","��־��2","��־��3","��־��4","��־��5","��־��6"]
num = len(names); # �õ��б�ĳ���
fornum = range(num) # �����б�ĳ���������������,ֵ��:0-����-1,
for index in fornum:
	print names[index]


# enumerate()���������б��ֵ������
names = ["��־��1","��־��2","��־��3","��־��4","��־��5","��־��6"] 
for i,name in enumerate(names):
	print name + "���±���:%d" % i
