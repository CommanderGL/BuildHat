from buildhat import Motor

speed = 32

tlm = Motor('A')
blm = Motor('B')
trm = Motor('C')
brm = Motor('D')

tlm.start(speed)
blm.start(speed)
trm.start(-speed)
brm.start(-speed)

while True:
    pass