import random

class Alice:
    bits=[] #0,1
    polarization=[] #0,90,45,-45

    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.bits=[]
        self.polarization=[]

    def create_bits(self, num_bits): #num_bits는 main에서 입력받는다
        for i in range(0,num_bits,1):
            x=random.randint(0,1)
            self.bits.append(x)#보낼 비트의 개수만큼 비트 랜덤으로 생성
            if x==0 :
                self.polarization.append(0)
            elif x==1:
                self.polarization.append(45)
        #print("alice가 생성한 bits : ",self.bits)
        #print("alice의 polarization : ",self.polarization)
    def send_bits(self):#bob과 같은 bit인지 확인해야함
        return self.bits
    
    def send_polarization(self):
        return self.polarization
    
