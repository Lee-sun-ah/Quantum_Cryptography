import random

class Bob:
    bits=[] #0,1
    polarization=[]
    real_bits=[] #통과한 bit
    exchange=[]#실제 교환 가능한 bit
    passed=[]#0:통과못함, 1:통과함 
    
    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.bits=[]
        self.polarization=[]
        self.real_bits=[]
        self.exchange=[]
        self.passed=[]

    def create_bits(self, num_bits): #num_bits는 main에서 입력받는다
        for i in range(0,num_bits,1):
            x=random.randint(0,1)
            self.bits.append(x)#보낼 비트의 개수만큼 비트 랜덤으로 생성
            if x==0 :
                self.polarization.append(-45)
            elif x==1:
                self.polarization.append(90)
        #print("bob이 생성한 bits : ",self.bits)
        #print("bob의 polarization : ",self.polarization)

    def measure_bits(self,received):#alice/eve 가 보낸 polarization을 매개변수(received)로 받아온다
        for i in range(0,len(self.bits),1):
            if abs(self.polarization[i]-received[i])==90 :
                self.passed.append(0)
            elif (abs(self.polarization[i]-received[i])==45 or abs(self.polarization[i]-received[i])==135) :
                self.passed.append(random.randint(0,1))
        #print("통과한 비트표시 : ",self.passed)
    
    def measure_real_bits(self,bits):#오류율 
        for i in range(0,len(self.bits),1):
            if self.passed[i]==1:#통과했으면
                self.real_bits.append(self.bits[i])#일단 검사할비트에 집어넣는다(교환가능한 비트)
                if bits[i]==self.bits[i]:#alice의 비트와 같아야 실제 교환 가능한 비트이다.
                    self.exchange.append(self.bits[i])
        #print("교환가능한 비트 : ",self.real_bits)
        #print("실제 교환가능한 비트 : ",self.exchange)
        #print("실제교환가능한비트/원래비트수",len(self.exchange)/len(bits))
        #return len(self.exchange)/len(bits)
        print("QBER(Quantum Bit Error Rate) : ",(len(self.real_bits)-len(self.exchange))/len(self.real_bits)*100,"%")
        return (len(self.real_bits)-len(self.exchange))/len(self.real_bits)*100

        
        
