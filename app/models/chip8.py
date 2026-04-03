from ..decorators.check_path import check_path
from ..decorators.get_data import get_data
from shared import display_msg
class chip8:
    W= 64
    H = 32
    def __init__(self):
        self.memory=[0]*4096
        self.V=[0]*16
        self.pc=0x200
        self.stack=[]
        self.i=0
        self.sound=0
        self.delay=0
        self.ecran=[]*64*32
        self.draw_flag=False
    @check_path
    @get_data
    def load_rom(self,path,rom=None):
            start=0x200
            end=start+len(rom)
            self.memory[start:end]= rom
            

    def fetch(self):
         opcode = self.memory[self.pc]<<8 | self.memory[self.pc+1]
         self.pc=self.pc+2
         return opcode
    
    def steps(self):
        opcode=self.fetch()
        nnn=opcode & 0x0FFF
        n=opcode & 0x000F
        kk= opcode&0xFF
        x=(opcode>>8)&0xF
        y=(opcode>>4)& 0xF

        if opcode== 0x0E00:
             display_msg("clear the screen")
             self.gfx=[0]*(self.W*self.H);
             self.draw_flag=True
             return
        
        if opcode==0x00EE:
             display_msg("removed last stack address becomes the pc value")
             self.pc=self.stack.pop()
             return
        if(opcode&0xF000)==0xA000:
             display_msg("change the value of I", 'info')
             self.i=nnn
             return

        if (opcode & 0xF000)==0x6000:
            display_msg(f"load in register {x} value {kk}","autre")
            self.V[x]=kk
            return

        if (opcode & 0xF000) == 0xD000:
            display_msg ("draw sprite","attention")
            self.V[0xF]=0
            for row in range(n):
                spr=self.memory[(self.i + row)&0xFFF]
            for bit in range(8):
                if spr & (0x80 >> bit):
                     xi=(self.v[x]+bit)%self.W
                     yi= (self.V[y]+row)%self.H
                     idx=xi+yi*self.W
                     self.V[0xF]|=self.gfx[idx]
                     self.ecran[idx] ^=1
            self.draw_flag=True
            return


        display_msg("opcode unknown", "danger")