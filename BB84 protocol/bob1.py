import random

class Bob:
    bits=[] #0,1
    basis=[] #+(0),x(1)
    real_bits=[] #같은 basis를 사용한 bit
    exchange=[]
    
    def reset(self):#여러번 측정하기 편하게 하기위해 reset함수 생성
        self.bits=[]
        self.basis=[]
        self.real_bits=[]
        self.exchange=[]
    
    def create_basis(self,num_bits):#num_bits는 alice와 같음
        for i in range(0,num_bits,1):
            self.basis.append(random.randint(0,1))#basis 랜덤으로 선택
        #print("bob이 생성한 basis : ",self.basis)

    def measure_bits(self,received):#alice/eve 가 보낸 polarization을 매개변수(received)로 받아온다
        for i in range(0,len(self.basis),1):
            if self.basis[i]==0 and received[i]==90 :
                self.bits.append(0)
            elif self.basis[i]==0 and received[i]==0:
                self.bits.append(1)
            elif self.basis[i]==1 and received[i]==45:
                self.bits.append(0)
            elif self.basis[i]==1 and received[i]==-45:
                self.bits.append(1)
            elif self.basis[i]==0 and received[i]==45:
                self.bits.append(random.randint(0,1))
            elif self.basis[i]==0 and received[i]==-45:
                self.bits.append(random.randint(0,1))
            elif self.basis[i]==1 and received[i]==90:
                self.bits.append(random.randint(0,1))
            elif self.basis[i]==1 and received[i]==0:
                self.bits.append(random.randint(0,1))
        #print("bob이 측정한 bits : ",self.bits)

    def measure_real_bits(self,received,bits):#alice가 보낸 basis를 매개변수(received)로 받아온다.
        for i in range(0,len(self.basis),1):
            if received[i]==self.basis[i]:
                if bits[i]==self.bits[i]:
                    self.exchange.append(self.bits[i])
                self.real_bits.append(self.bits[i])
        #print("교환가능한 비트 : ",self.real_bits)
        #print("실제 교환가능한 비트 : ",self.exchange)
        #print("실제교환가능한비트/원래비트수",len(self.exchange)/len(bits))
        #return len(self.exchange)/len(bits)
        print("QBER(Quantum Bit Error Rate) : ",(len(self.real_bits)-len(self.exchange))/len(self.real_bits)*100,"%")
        return (len(self.real_bits)-len(self.exchange))/len(self.real_bits)*100

        
        
