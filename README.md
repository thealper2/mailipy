# mailipy

SMTP servisi üzerinden mail göndermeye yarayan bir araçtır.

## Gereksinimler

mailipy aşağıdaki kütüphaneleri kullanır.

* Colorama

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/mailipy.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

```bash
usage: mailipy.py [-h] [--target TARGET] [--server SERVER] [--count COUNT] [--subject SUBJECT]
                  [--message MESSAGE] [--list]

options:
  -h, --help         show this help message and exit
  --target TARGET
  --server SERVER
  --count COUNT
  --subject SUBJECT
  --message MESSAGE
  --list
```

## Örnekler

```python
python3 mailipy.py --target target_email --server gmail --count 1 --subject "Deneme" --message "Deneme mesajı"
python3 mailipy.py --list
```
