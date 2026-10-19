# SİHA telemetri ve radar izleme arayüzü

Bu 'Demo' proje, Düzce Üniversitesi Akınay SİHA takımı mülakatı için hazırlanmıştır.

## Çalışma mantığı

- telemetry.py dosyası arayüz için gereken sahte verileri oluşturur.
- main.py ise bu verileri kullanarak arayüzü günceller.

## Gereksinimler

- Python 3.10+
- `uv` paket yöneticisi

## Kullanılan kütüphaneler

- pydantic
- pyqt5
- pyqtdarktheme
- pyqtgraph

## Geliştirme

1. Repo'yu klonlayıp klasöre girin.
   ```bash
   git clone <repo-url>
   cd demo_project
   ```
2. Bağımlılıkları senkronize edin.
   ```bash
   uv sync
   ```
3. Uygulamayı çalıştırın.
   ```bash
   uv run main.py
   ```

## Derleme

```bash
uv run pyinstaller --noconsole --onefile \
  --add-data "style.css:." \
  --add-data "logo.png:." \
  main.py
```
