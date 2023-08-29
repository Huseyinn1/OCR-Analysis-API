# Temel alınacak Docker imajı belirleniyor
FROM python:3.11

# Uygulama klasörü oluşturuluyor
WORKDIR /app

# Poetry kütüphane dosyalarının kopyalanması ve yüklenmesi
COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && poetry install --no-root

# Tesseract'ı yükle
RUN apt-get update && apt-get install -y tesseract-ocr

# Uygulama dosyalarının kopyalanması
COPY . .

