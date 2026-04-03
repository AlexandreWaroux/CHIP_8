from pre.models.software import Software
from app.models.chip8 import chip8

#Software.create(path="test.ch8",data="0E 00 62 0A A2 22 D2 48")
machine=chip8()
machine.load_rom(path="test.ch8")

for i in range(4):
    machine.steps()