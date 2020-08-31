import random

class Eve:
    polarization=[] #0,90,45,-45
    passed=[]#0:통과못함, 1:통과함
    a_polarization=[]
    num_b=0
    
    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.polarization=[]
        self.passed=[]
        self.a_polarization=[]
        
    def create_bits(self, num_bits): #num_bits는 main에서 입력받는다
        self.num_b=num_bits
        for i in range(0,num_bits,1):
            x=random.randint(0,1)
            if x==0 :
                self.polarization.append(-45)
            elif x==1:
                self.polarization.append(90)
        #print("eve의 polarization : ",self.polarization)

    def measure_bits(self,received,eavesdropping):#alice가 보낸 polarization을 매개변수(received)로 받아온다
        for i in range(0,int(self.num_b*eavesdropping),1):#도청자가 존재하는 부분 
            if abs(self.polarization[i]-received[i])==90 :
                self.passed.append(0)
            elif (abs(self.polarization[i]-received[i])==45 or abs(self.polarization[i]-received[i])==135) :
                self.passed.append(random.randint(0,1))

        for i in range(0,int(self.num_b*eavesdropping),1):
            if self.passed[i]==1:
                self.polarization[i]=45
            elif self.passed[i]==0:
                x=random.randint(0,1)
                if x==0:
                    self.polarization[i]=0
                elif x==1:
                    self.polarization[i]=45

        for i in range(int(self.num_b*eavesdropping),self.num_b,1):#도청자가 없는 부분
            self.polarization[i]=self.a_polarization[i]          
            self.passed.append(1)
            
        #print("eve가 다시보낸 polariztion : ",self.polarization)
        #print("통과한 비트표시 : ",self.passed)
    
            
    def send_polarization(self): #채널로 보냄
        return self.polarization
    
    def receive_p(self,alice):#alice의 polarization받아오기 
        self.a_polarization=alice
