import random

class Eve:
    basis=[] #+(0),x(1)
    polarization=[] #0,90,45,-45
    a_polarization=[]
    
    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.basis=[]
        self.polarization=[]
        self.a_polarization=[]
        
    def create_basis(self,num_bits): #num_bits는 main에서 입력받는다
        for i in range(0,num_bits):
            self.basis.append(random.randint(0,1))#basis 랜덤으로 선택
        #print("eve가 생성한 basis : ",self.basis)
    
    def measure_bits(self,received,eavesdropping):#alice가 보낸 polarization을 매개변수(received)로 받아온다
        for i in range(0,int(len(self.basis)*eavesdropping),1):#도청자가 존재하는 부분 
            if self.basis[i]==0 and received[i]==90 :
                self.polarization.append(90)
            elif self.basis[i]==0 and received[i]==0:
                self.polarization.append(0)
            elif self.basis[i]==1 and received[i]==45:
                self.polarization.append(45)
            elif self.basis[i]==1 and received[i]==-45:
                self.polarization.append(-45)
            elif self.basis[i]==0 and received[i]==45:
                if random.randint(0,1)==0:
                    self.polarization.append(0)
                else :
                    self.polarization.append(90)
            elif self.basis[i]==0 and received[i]==-45:
                if random.randint(0,1)==0:
                    self.polarization.append(0)
                else :
                    self.polarization.append(90)
            elif self.basis[i]==1 and received[i]==90:
                if random.randint(0,1)==0:
                    self.polarization.append(45)
                else :
                    self.polarization.append(-45)                
            elif self.basis[i]==1 and received[i]==0:
                if random.randint(0,1)==0:
                    self.polarization.append(45)
                else :
                    self.polarization.append(-45)
        #print("eve가 측정한 polariztion : ",self.polarization)
                    
        for i in range(int(len(self.basis)*eavesdropping),len(self.basis),1):#도청자가 없는 부분
            self.polarization.append(self.a_polarization[i])

    def send_polarization(self): #채널로 보냄
        return self.polarization

    def receive_p(self,alice):#alice의 polarization받아오기 
        self.a_polarization=alice
        
