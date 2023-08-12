from cryptography import x509
from cryptography.hazmat.backends import default_backend
import ssl

# Укажите путь к файлу x.509
file_path = "kzmboz1019.cer"

# Считываем файл x.509
with open(file_path, "rb") as file:
    cert_data = file.read()

# Парсим данные сертификата
cert = x509.load_der_x509_certificate(cert_data, default_backend())

# Выводим информацию о сертификате
print("Информация о сертификате:")
print(f"Субъект: {cert.subject}")
print(f"Издатель: {cert.issuer}")
print(f"Срок действия: с {cert.not_valid_before} по {cert.not_valid_after}")
print(f"Version {cert.version}")
print(cert.signature_algorithm_oid)

# Получаем публичный ключ из сертификата
public_key = cert.public_key()

print(public_key)


