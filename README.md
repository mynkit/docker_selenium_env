# dockerでscraping環境を構築する

* build

```sh
docker-compose build
```

* コンテナ立ち上げ

```sh
docker-compose up -d
```

* dockerサーバに入る
	* chromedriverのpathは`/usr/local/bin/chromedriver`

```sh
docker-compose exec scraping sh
# sh update_vimrc.sh
```

