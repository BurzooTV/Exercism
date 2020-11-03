def convert(number: int) -> str:
    pattern = [[3, 'Pling'], [5, 'Plang'], [7, 'Plong']]
    result = ''.join([sound for number, sound in pattern if sound % number == 0])
    
    return str(number) if result == '' else result
