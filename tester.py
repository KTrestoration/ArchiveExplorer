from KTarchive import KTclass

obj = KTclass()

if not obj.download_archive():
    print('pls install ruby')
    exit()
obj.user_scraper()
