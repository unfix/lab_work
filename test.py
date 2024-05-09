# Тесты для S-блока
def test_S_block():
    data = [0x32, 0x88, 0x31, 0xe0]
    encrypted_data = forward_S_block(data)
    decrypted_data = inverse_S_block(encrypted_data)
    assert decrypted_data == data, "Ошибка: результат обратного преобразования через S-блок неверен"

# Тесты для P-блока
def test_P_block():
    data = [0x32, 0x88, 0x31, 0xe0]
    encrypted_data = forward_P_block(data)
    decrypted_data = inverse_P_block(encrypted_data)
    assert decrypted_data == data, "Ошибка: результат обратного преобразования через P-блок неверен"

# Запуск тестов
test_S_block()
test_P_block()
print("Все тесты пройдены успешно.")