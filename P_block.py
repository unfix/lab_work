# Функция прямого преобразования через P-блок
def forward_P_block(data, shift=1):
    return data[shift:] + data[:shift]

# Функция обратного преобразования через P-блок
def inverse_P_block(data, shift=1):
    return data[-shift:] + data[:-shift]