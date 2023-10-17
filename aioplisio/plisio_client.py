from utils.base import _BaseAIOPlisioClient
from api.get_asyncio_api import _PlisioMethods, _PlisioInvoice

# TODO: Распределить код по файлам
# TODO: Написать датаклассы


class AIOPlisioClient(_BaseAIOPlisioClient):
    
    @property
    def get(self) -> _PlisioMethods:
        return _PlisioMethods(self._api_key)
    
    @property
    def invoice(self) -> _PlisioInvoice:
        return _PlisioInvoice(self._api_key)