import random
from alice import Alice
from bob import Bob
from eve import Eve
from matplotlib import pyplot as plt
import pandas as pd

alice=Alice()
bob=Bob()
eve=Eve()
num_bits=[500]
bits=[]
basis=[]
qc_polarization=[]#양자채널로 보내진 polarization
count=0
QBER=[]
sum_QBER=0
sum_data=0
eavesdropping_rate=0.1

for i in range(0,len(num_bits)) :

    #print("비트의 개수 : ",num_bits[i])
    
    while(eavesdropping_rate<=1):            
            
            random.seed()

            alice.reset()
            bob.reset()
            eve.reset()
    
            #int(input("몇개의 비트를 생성할까요? "))
    
            alice.create_bits(num_bits[i]) #alice가 비트와 랜덤한 basis생성
            qc_polarization=alice.send_polarization()
            eve.receive_p(qc_polarization)#도청자가없는 부분은 alice의 polarization으로 채운다.(원래 상태)
            
            eve.create_bits(num_bits[i]) #eve가 basis를 랜덤으로 선택한다.
            eve.measure_bits(qc_polarization,eavesdropping_rate) #eve의 basis로 신호 측정
            qc_polarization=eve.send_polarization() #바뀐 신호를 양자 채널로 전송
                
            bob.create_bits(num_bits[i]) #bob이 basis를 랜덤으로 선택한다.
            bob.measure_bits(qc_polarization) #basis와 polarization으로 비트 측정
    
            bits=alice.send_bits() #alice가 bit보냄
            
            QBER.append(bob.measure_real_bits(bits)) #alice랑 같은 basis인지 확인해 실제 bit 보관
            
            eavesdropping_rate+=0.1  

            
z0=pd.DataFrame({'x0' : 10,'y0' : QBER[0]},index=[0])
z1=pd.DataFrame({'x1' : 20,'y1' : QBER[1]},index=[1])
z2=pd.DataFrame({'x2' : 30,'y2' : QBER[2]},index=[2])
z3=pd.DataFrame({'x3' : 40,'y3' : QBER[3]},index=[3])
z4=pd.DataFrame({'x4' : 50,'y4' : QBER[4]},index=[4])
z5=pd.DataFrame({'x5' : 60,'y5' : QBER[5]},index=[5])
z6=pd.DataFrame({'x6' : 70,'y6' : QBER[6]},index=[6])
z7=pd.DataFrame({'x7' : 80,'y7' : QBER[7]},index=[7])
z8=pd.DataFrame({'x8' : 90,'y8' : QBER[8]},index=[8])
z9=pd.DataFrame({'x9' : 100,'y9' : QBER[9]},index=[9])

plt.scatter(z0['x0'],z0['y0'])
plt.scatter(z1['x1'],z1['y1'])
plt.scatter(z2['x2'],z2['y2'])
plt.scatter(z3['x3'],z3['y3'])
plt.scatter(z4['x4'],z4['y4'])
plt.scatter(z5['x5'],z5['y5'])
plt.scatter(z6['x6'],z6['y6'])
plt.scatter(z7['x7'],z7['y7'])
plt.scatter(z8['x8'],z8['y8'])
plt.scatter(z9['x9'],z9['y9'])

plt.xlabel('eavesdropping rate % ')
plt.ylabel('QBER')
plt.ylim([0,100])
plt.grid()
plt.show()


