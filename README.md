![generated](generated.gif)


## Documents

1. Описание проекта https://docs.google.com/document/d/1hk-XnfFkub-kfwe0UYecx62N2mpee7OyIuURyGEO_lU/edit?usp=sharing 

1. Карточка проекта https://www.notion.so/TattooGAN-4cbb30d49f9444b992707d0ae71f3181


## Yandex.Disk

- подключаемся к яндекс диску через либу [yadisk](https://github.com/ivknv/yadisk)
- для асинхронной работы можно использовать [yadisk-async](https://github.com/ivknv/yadisk-async)
- по токену есть доступ только к папке приложения
- путь к корню папки приложения задается так: `app:/`


```bash
$ pip install yadisk
```

```python
import yadisk

y = yadisk.YaDisk(token="...")
y.listdir("app:/")
y.mkdir("app:/test")
```

## Pinterest scrapper

Для запуска [скрепера](pinterest_scraper/scraper.py) нужно заполнить данные пользователя в [конфиге](pinterest_scraper/config.py).

Для запуска:

```bash
$ python scraper.py <pinterest_url or search_title>
```

Примеры:

```bash
$ python scraper.py https://www.pinterest.ru/pin/19984792086693342/

$ python scraper.py "татуировки эскизы"
```

## StyleGAN2

Для обучения использовался StyleGAN2 из https://github.com/lucidrains/stylegan2-pytorch

