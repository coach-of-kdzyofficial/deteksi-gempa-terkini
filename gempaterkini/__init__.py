import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 22 November 2022, 19:22:27 WIB
    Magnitudo: 2.8
    Kedalaman: 2 km
    Lokasi: LS= 6.85 BT= 107.06
    Pusat Gempa: Pusat gempa berada di darat 9 km BaratDaya Cianjur
    Dirasakan: Dirasakan (Skala MMI): III Cugenang, III Cilaku
    :return:
    """
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None
    if content.status_code == 200 :
        print(content.text)
        # soup = BeautifulSoup(content)
        # print(soup.prettify())
        hasil = dict()
        hasil['tanggal'] = '22 November 2022'
        hasil['waktu'] = '19:22:27 WIB'
        hasil['magnitudo'] = 2.8
        hasil['kedalaman'] = '2 km'
        hasil['lokasi'] = {'ls':6.85, 'bt':107.06}
        hasil['pusatgempa'] = 'Pusat gempa berada di darat 9 km BaratDaya Cianjur'
        hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Cugenang, III Cilaku'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak Bisa Menemukan Data Gempa Terkini')
        return
    print('Gempa Terakhir Bersarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusatgempa']}")
    print(f"Dirasakan {result['dirasakan']}")