# Rubén Villalpando Bremont A01376331
# Alex Fernando Leyva Martínez A01747078

def encodeMessage(parities, digits):
    digits.insert(0, parities[0])
    for x in range(len(parities)-1):
        digits.insert(2**x, parities[x+1])
    return digits



def binAHex(MR):
    hexString = ""
    zeros = 0
    if len(MR)%4 != 0:
        zeros = 4 - len(MR)%4
    zeroes = []
    for _ in range(zeros):
        zeroes.append(0)
    for x in MR:
        zeroes.append(x)
    MR = zeroes
    for x in range(0, len(MR), 4):
        hexInBinary = MR[x:x+4]
        hexNumber = 0
        power = 0
        for n in range(3, -1, -1):
            if hexInBinary[n] == 1:
                hexNumber += 2**power
            power += 1
        if hexNumber>=10:
            if hexNumber == 10:
                hexNumber = "A"
            elif hexNumber == 11:
                hexNumber = "B"
            elif hexNumber == 12:
                hexNumber = "C"
            elif hexNumber == 13:
                hexNumber = "D"
            elif hexNumber == 14:
                hexNumber = "E"
            elif hexNumber == 15:
                hexNumber = "F"
        hexString += str(hexNumber)
    return hexString


def calcularSindrome(paridades, paridadesPrimas):
    syndrome = ""
    for n in range(len(paridades)-1, -1, -1):
        if paridades[n] == paridadesPrimas[n]:
            syndrome += "0"
        else:
            syndrome += "1"
    return syndrome


def corregirError(sindrome, localMR):
    lugarDeError = 0
    potencia = 0
    for n in range(-1, -len(sindrome), -1):
        if sindrome[n] == "1":
            lugarDeError += 2**potencia
        potencia += 1
    if localMR[lugarDeError] == 0:
        localMR[lugarDeError] = 1
        return localMR
    localMR[lugarDeError] = 0

    return localMR


def HEXaBIN(MR):
    stringBinario = ""
    for char in MR:
        if char == "0":
            stringBinario += "0000"
        elif char == "1":
            stringBinario += "0001"
        elif char == "2":
            stringBinario += "0010"
        elif char == "3":
            stringBinario += "0011"
        elif char == "4":
            stringBinario += "0100"
        elif char == "5":
            stringBinario += "0101"
        elif char == "6":
            stringBinario += "0110"
        elif char == "7":
            stringBinario += "0111"
        elif char == "8":
            stringBinario += "1000"
        elif char == "9":
            stringBinario += "1001"
        elif char == "A":
            stringBinario += "1010"
        elif char == "B":
            stringBinario += "1011"
        elif char == "C":
            stringBinario += "1100"
        elif char == "D":
            stringBinario += "1101"
        elif char == "E":
            stringBinario += "1110"
        elif char == "F":
            stringBinario += "1111"
    return stringBinario


def calculateParities(digits):
    paritiesDigits = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
    change = [2, 5, 12, 27]
    conts = [0, 1]
    for digitNum in range(1, len(digits)+1):

        if digitNum in change:
            conts.append(0)
            conts[0] -= 1
            for x in range(1, len(conts)):
                conts[x] += 1

        if conts[0] == 0:
            paritiesDigits[1].append(digitNum)
            conts[0] += 1
        else:
            conts[0] = 0

        for n in range(1, len(conts)):
            conts[n] += 1
            if conts[n] <= 2**n:
                paritiesDigits[n+1].append(digitNum)
            elif conts[n] >= 2*(2**n):
                conts[n] = 0

    parities = []
    for x in range(1, len(paritiesDigits)+1):
        suma = 0
        if paritiesDigits[x]:
            for n in paritiesDigits[x]:
                suma += digits[n-1]
        parities.append(suma)
    for x in range(len(parities)):
        parities[x] %= 2
    gp = (sum(parities) + sum(digits))%2

    allParities = [gp]

    for x in parities:
        allParities.append(x)
    return allParities


def calculatePrimeParities(MR):
    parities = {}
    for n in range(5, -1, -1):
        if len(MR) > 2 **n:
            maxPower = n
            break
    x = len(MR)
    if x <= 39:
        for n in range(maxPower, -1, -1):
            if x > 2**n:
                parities[n+1] = MR.pop(2**n)
    parities[0] = MR.pop(0)
    parities1 = []
    for x in range(maxPower+1, -1, -1):
        parities1.append(parities[x])
    primeParities = calculateParities(MR)
    return primeParities, parities1


def correctZeros(MR):
    x = len(MR)
    if x == 40 or x == 36:
        MR.pop(0)
    elif x == 32 or x == 28 or x == 24 or x == 20:
        MR.pop(0)
        MR.pop(0)
    elif x == 16:
        MR.pop(0)
        MR.pop(0)
        MR.pop(0)



if __name__ == '__main__':
    message = str(input("Mensaje recibido: "))
    MRHEX = message[:]
    message = HEXaBIN(message)

    MR = [int(i) for i in message]

    correctZeros(MR)
    # Mensaje volteado para que coincidan indices con digitos más fácil
    MR.reverse()

    constantMR = MR[:]

    digits = MR[:]


    # Se calculan las paridades en caso de que lo que se mando fuera digitos
    if len(digits) <= 32:
        paritiesDigits = calculateParities(digits)
        stringParities = "GP = " + str(paritiesDigits[0])
        for x in range(1, len(paritiesDigits)):
            stringParities += ", P" + str(x) + " = " + str(paritiesDigits[x])
        print("If what you entered were digits, the parities are: " + stringParities)
        messageToTransmit = encodeMessage(paritiesDigits, digits)
        messageToTransmit.reverse()
        encodedMessage = binAHex(messageToTransmit)
        print("And the encoded message for that would be: ", encodedMessage)

    if len(MR) <= 39:
        primeParities, parities = calculatePrimeParities(MR)

        gp, gpp = parities.pop(0), primeParities.pop(0)

        sindrome = calcularSindrome(parities, primeParities)

        print("If what you entered was a message then the error encountered was: ")

        stringSindrome = ""

        for x in sindrome:
            stringSindrome += "0"

        if sindrome != stringSindrome:
            if gp == gpp:
                print("DED")
                print("Errors can't be identified.")
            else:
                print("SEC")
                print("Mensaje recibido: ", MRHEX)
                MRCORREGIDO = corregirError(sindrome, constantMR)
                MRCORREGIDO.reverse()
                print("Mensaje transmitido: ", binAHex(MRCORREGIDO))
        else:
            print("No hay error")
            print("Mensaje recibido: ", MRHEX)
            print("Mensaje transmitido: ", MRHEX)
    else:
        print("The message you are trying to enter uses more than 32 digits, please try again")
