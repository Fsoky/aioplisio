# aioplisio - Asynchronous wrapper for Plisio API

> **_Модуль в разработке, сейчас недоступны методы withdraw_**

## Установка 💾
- Установка, используя пакетный менеджер pip
```
$ pip install aioplisio
```
- Установка с GitHub *(требуется [git](https://git-scm.com/downloads))*
```
$ git clone https://github.com/Fsoky/aioplisio
$ cd aioplisio
$ python setup.py install
```
- Или
```
$ pip install git+https://github.com/Fsoky/aioplisio
```

### Дополнительно:
Зарегистрируйтесь на сайте **[Plisio](https://plisio.net/)** и получите API-ключ. \
Официальная документация по API: **[PLISIO API DOCS](https://plisio.net/documentation/getting-started/introduction)**

## Примеры использования:
- Шаблон
```py
import asyncio
from aioplisio import AIOPlisioClient


async def main() -> None:
    async with AIOPlisioClient("API-KEY") as plisio:
        ...


if __name__ == "__main__":
  asyncio.run(main())
```
- Получение транзакций
```py

async with AIOPlisioClient("YOUR API-KEY") as plisio:
    transactions = await plisio.get.transactions() # You can pass txnID for search by it
    print(transactions.data)
```
- Инвойсы (чеки)
```py
async with AIOPlisioClient("YOUR API-KEY") as plisio:
    invoice = await plisio.invoice.create(
        "ORDER-NAME",
        12345001, # Order number
        amount=10 # 10 USDT
        currency="USDT" # Crypto
        source_currency="USD" # Fiat
        expire_min=15
    )
    print(f"Your invoice: {transaction.data.invoice_url}")

    transaction = await plisio.get.transactions(invoice.data.txn_id)
    print(transaction.data.status)
```

> _...И также другие методы_
