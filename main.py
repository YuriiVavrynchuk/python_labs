from protector import Protector

protector1 = Protector()
protector2 = Protector(20)
protector3 = Protector(200,10,"green",500,"Bosch", 2015)

print(protector1)
print(protector2)
print(protector3)

print(protector1.advertisement())
