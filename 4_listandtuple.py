# -- coding: utf-8 --
# list �б�
strList = ['Name1','Name2','Name3']
intList = [1,2,3]
arrayList = ['Name',1,'Age'] # ���ݿ��Բ�ͬ
arrayList1 = ['Name',1,'Age',arrayList,["123",123]] # ���ݿ�������һ���б�
arrayList1[4][1] # Ҫȡ�����123����ͨ����ά�������ʽȡ����
item = arrayList[0]; #�õ�ĳ��λ�õ�Ԫ��,��0��ʼ
item = arrayList[len(arrayList)-1]; # ���һ��Ԫ��
item = arrayList[-1]; # -1Ҳ���Եõ����һ��Ԫ��
item = arrayList[-2]; # �����Դ����ƣ��õ������ڶ���Ԫ��-2
itemcount = len(arrayList) # ���Ԫ�صĸ���
arrayList.append("newValue") #����β��׷��һ���µ�ֵ 
arrayList.insert(1,"newValue") #��������λ��׷��һ���µ�ֵ 
arrayList.pop() #ɾ��ĩβ��Ԫ��
arrayList.pop(1) # ɾ��ָ��λ�õ�Ԫ��
arrayList[0] = "new" # �滻ĳ��λ�õ�ֵ

# tuple Ԫ��
# Ԫ��һ�������˾Ͳ��ܸı���
tuples = ("sdf","123",123) # �����ʱ���Ҫȷ������
tuples = () # ����һ���յ�Ԫ����û������
tuples = (1) # �����൱����tuples = 1,��Ϊ()�ᵱ�������������()
tuples = (1,) # ���������Ƕ�����ֻ��һ��Ԫ�ص�Ԫ��
tuples = (1,2,["12",1]) # ͨ��������б�Ԫ�ؿ��Ա���ĸı�tuples��ֵ
# tuples[0] = 9 # �����
tuples[2][0] = "new" # �ı�list��ֵ

