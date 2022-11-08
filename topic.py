from passageiro import Passageiro


class Topic:
    def __init__(self, capacidade: int, qtdPrioritarios: int):
        self.numPassageiros = capacidade - qtdPrioritarios
        self.numPrioritaria = qtdPrioritarios
        self.passageiros = []
        self.prioritaria = []
        self.ctPassageiros = self.numPassageiros
        self.ctPrioritaria = self.numPrioritaria
        self.vagasDisp = capacidade

    def getAssentosPrioritarios(self):
        return self.ctPrioritaria

    def getAssentosNormais(self):
        return self.ctPassageiros

    def getPassageiroAssentoNormal(self, lugar):
        if len(self.passageiros) > 0:
            return self.passageiros[lugar]
        else:
            return None

    def getPassageiroAssentoPrioritario(self, lugar):
        if len(self.prioritaria) > 0:
            return self.prioritaria[lugar]
        else:
            return None

    def getVagas(self):
        return self.vagasDisp

    def subir(self, passageiro: Passageiro):
        if self.vagasDisp > 0:
            if passageiro.ePrioridade():
                if self.ctPrioritaria > 0:
                    self.prioritaria.append(passageiro)
                    self.vagasDisp -= 1
                    self.ctPrioritaria -= 1
                    return True
                else:
                    self.passageiros.append(passageiro)
                    self.vagasDisp -= 1
                    self.ctPassageiros -= 1
                    return True
            else:
                if self.ctPassageiros > 0:
                    self.passageiros.append(passageiro)
                    self.vagasDisp -= 1
                    self.ctPassageiros -= 1
                    return True
                else:
                    self.prioritaria.append(passageiro)
                    self.vagasDisp -= 1
                    self.ctPrioritaria -= 1
                    return True
        else:
            print("Topic Cheia! Não é possivel adionar mais pessoas!")
            return False

    def descer(self, nome):
        for num in range(len(self.prioritaria)):
            passageiro = self.prioritaria[num]
            if passageiro.nome == nome:
                self.prioritaria.pop(num)
                self.vagasDisp += 1
                return True

        for num in range(len(self.passageiros)):
            passageiro = self.passageiros[num]
            if passageiro.nome == nome:
                self.passageiros.pop(num)
                self.vagasDisp += 1
                return True
        return False

    def toString(self):
        pasa = ['='] * self.numPassageiros
        prio = ['@'] * self.numPrioritaria
        for num in range(len(self.passageiros)):
            passageiro = self.passageiros[num]
            pasa[num] = '=' + passageiro.getNome()
        for num in range(len(self.prioritaria)):
            passageiro = self.prioritaria[num]
            prio[num] = '@' + passageiro.getNome()
        listaPassageiros = prio + pasa
        return listaPassageiros


