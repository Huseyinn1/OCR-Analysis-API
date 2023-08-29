import requests



def is_valid_plate_number(plate_number) -> tuple:
    """
    Checks whether the given license plate number (plate_number) is associated with a province in Turkey.

    Args:
    plate_number (str): The license plate number to be checked.

    Returns:
    tuple: If the license plate number belongs to a province in Turkey (between 1-81), it returns a tuple (True, province name).
    Otherwise, it returns a tuple (False,).
    """
    try:
        first_two_digits = int(plate_number[:2])
        if 1 <= first_two_digits <= 81:
            name = get_il_for_plaka(first_two_digits)
            return True, name
        else:
            return False
    except ValueError:
        return False

# Fonksiyon tanımı
def get_il_for_plaka(plaka) -> str:
    """
    Verilen plaka numarasına (plaka) karşılık gelen Türkiye ilini döndürür.

    Args:
    plaka (int): Plaka numarası (1-81 arası).

    Returns:
    str: Plaka numarasına karşılık gelen Türkiye ilinin adı.
    """
    try:
    # API adresini oluştur
        api_url = f"https://api.ubilisim.com/postakodu/il/{plaka}"

        # API'ye GET isteği gönder
        response = requests.get(api_url)

        # Yanıtı JSON formatında al
        data = response.json()

        # İl bilgisini çıkar
        il = data['postakodu'][0]['il']

        return il
    except Exception as e:
        return False 