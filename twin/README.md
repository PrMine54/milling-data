# DigitalTwin Cloud Architecture Run Steps
 Burada bulutta DT pipeline'ı simüle edilmiştir:

* Mantık: makineler verilerini bulut makinesine yollar, burada eğitim ve test olur. Veriler merkezde toplanır.
## Services:
* **FastAPI**: Buluttaki makineye verilerin prediction sonuçlarını API üzerinden alırız.
* **Prometheus**: API gelen isteklere ait metrikleri çıkarır.
* **Grafana**: Prometheus'dan gelen metrikleri görselleştirebilmek için.
* **Druid**: Kafka topiğini stream olarak dinler ve data source oluşturur.
* **Stream Data**: Test verisinin edge'den buluttaki API'a istek yollamasını simüle eder.
* **Superset**: Druid datasource'dan gelen verilerin görsel dashboardlarını oluşturabilmek için.
* **Consumer**: Belirtilen kafka topiğini dinler.(test için)
* **Kafka**: Model tahmin sonuçlarını basabilmek için.

## Servisleri Ayağa Kaldırabilmek için:
* $ docker-compose up -d
* $ docker run -d -p 8090:8088 --name superset apache/superset
* $ docker exec -it superset superset fab create-admin  --username admin  --firstname Superset  --lastname Admin  --email admin@superset.com --password admin
* $ docker exec -it superset superset db upgrade
* $ docker exec -it superset superset init

## Stream Olarak Test Verisini Bastırabilmek için; 
* $ cd stream_data/
* $ docker build . -t stream_data
* $ docker run 

## Notlar:
* **Grafana**:
  * kullanıcı adi: admin
  * sifre: pass@123
* **Superset**:
  * kullanıcı adi: admin
  * sifre: admin
* Supersete druid datasource eklemek için broker ip,port vermeliyiz.(druid://<makine_ip>:8082/druid/v2/sql)
* FASTAPI istek atan servisler için ip adresi makinenin api olmalı.
* druid datasource stream data eklerken broker:<makine_ip>:9092 olmalı, veriyi parse ederken json seçelim

## Ekranlar:
* **FastAPI** :http://<makine_ip>:8000/docs#
* **Druid** :http://<makine_ip>:8888/
* **Grafana** :http://<makine_ip>:3000/
* **Prometheus** :http://<makine_ip>:9090/
* **Superset** :http://<makine_ip>:8090/