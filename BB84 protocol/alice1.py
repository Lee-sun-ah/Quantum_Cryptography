import random

class Alice:
    bits=[] #0,1
    basis=[] #+(0),x(1)
    polarization=[] #0,90,45,-45

    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.bits=[]
        self.basis=[]
        self.polarization=[]

    def create_bits(self, num_bits): #num_bits는 main에서 입력받는다
        for i in range(0,num_bits,1):
            self.bits.append(random.randint(0,1))#보낼 비트의 개수만큼 비트 랜덤으로 생성
            self.basis.append(random.randint(0,1))#basis도 랜덤으로 선택
        #print("alice가 생성한 bits : ",self.bits)
        #print("alice가 생성한 basis : ",self.basis)

    def measure_polarization(self):#신호 측정 
        for i in range(0,len(self.bits),1):
            if self.bits[i]==0 and self.basis[i]==0 :
                self.polarization.append(90)
            elif self.bits[i]==0 and self.basis[i]==1:
                self.polarization.append(45)
            elif self.bits[i]==1 and self.basis[i]==0:
                self.polarization.append(0)
            elif self.bits[i]==1 and self.basis[i]==1:
                self.polarization.append(-45)
        #print("alice가 측정한 polarization : ",self.polarization)
        return self.polarization

    def send_bits(self):#bob과 같은 bit인지 확인해야함
        return self.bits
    
    def send_basis(self):#bob과 같은 basis인지 확인해야함
        return self.basis
        
    
