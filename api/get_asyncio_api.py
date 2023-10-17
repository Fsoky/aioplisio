from typing import Optional, Any, List

from utils.base import _BaseAIOPlisioClient
from utils.enums import CryptoCurrency, FiatCurrency, TransactionStatus, TransactionType, PlanName
from utils.models import (
    Balance,
    Transactions,
    TransactionsData,
    TransactionsParams,
    FeePlan,
    FeePlanEconomy,
    FeePlanNormal,
    FeePlanPriority,
    Comission,
    Invoice,
    InvoiceData
)


class _PlisioMethods(_BaseAIOPlisioClient):

    async def balance(self, psys_cid: CryptoCurrency) -> Balance:
        payload = {
            "psys_cid": psys_cid,
            "api_key": self._api_key
        }

        response = await self._make_request("balances", params=payload)
        return Balance(status=response["status"], **response["data"])
    
    async def transactions(
        self,
        id: Optional[str] | None=None,
        *,
        page: Optional[int] | None=None,
        limit: Optional[int] | None=None,
        shop_id: Optional[str] | None=None,
        type: str | Optional[TransactionStatus] | None=None,
        status: str | Optional[TransactionStatus] | None=None,
        currency: str | Optional[CryptoCurrency] | None=None
    ) -> Transactions:
        payload = {
            "page": page,
            "limit": limit,
            "shop_id": shop_id,
            "type": type.name if not isinstance(type, str) and type is not None else type,
            "status": status.name if not isinstance(status, str) and type is not None else status,
            "currency": currency.name if not isinstance(currency, str) and type is not None else currency,
            "api_key": self._api_key
        }
        payload = {k: v for k, v in payload.items() if v is not None}
        
        endpoint = "operations" if id is None else f"operations/{id}"
        if endpoint.startswith("operations/"):
            payload = {"api_key": self._api_key}

        response = await self._make_request(endpoint, params=payload)
        response_data = response["data"].copy()
        response_data.pop("params", {})

        return Transactions(
            status=response["status"],
            data=TransactionsData(**response_data, params=TransactionsParams(**response["data"]["params"]))
        )
    
    async def fee_plan(self, psys_cid: str | CryptoCurrency) -> FeePlan:
        payload = {
            "api_key": self._api_key
        }

        response = await self._make_request(f"operations/fee-plan/{psys_cid}", params=payload)
        return FeePlan(
            status=response["status"],
            economy=FeePlanEconomy(**response["data"]["economy"]),
            normal=FeePlanNormal(**response["data"]["normal"]),
            priority=FeePlanPriority(**response["data"]["priority"])
        )
    
    async def fee(self, psys_cid: str | CryptoCurrency, addresses: str, amounts: float) -> Any:
        payload = {
            "addresses": addresses,
            "amounts": amounts,
            "api_key": self._api_key
        }

        response = await self._make_request(f"operations/fee/{psys_cid}", params=payload)
        return response
    
    async def commission(
        self,
        psys_cid: str | CryptoCurrency,
        addresses: str,
        amounts: float,
        fee_plan: PlanName,
        type: str | TransactionType
    ) -> Comission:
        payload = {
            "addresses": addresses,
            "amounts": amounts,
            "fee_plan": fee_plan,
            "type": type.name if not isinstance(type, str) else type,
            "api_key": self._api_key
        }

        response = await self._make_request(f"operations/commission/{psys_cid}", params=payload)
        return Comission(
            status=response["status"],
            commission=response["data"]["commission"],
            fee=response["data"]["fee"],
            plan=response["data"]["plan"],
            use_wallet=response["data"]["useWallet"],
            use_wallet_balance=response["data"]["useWalletBalance"],
            plans=FeePlan(
                normal=FeePlanNormal(**response["data"]["plans"]["normal"]),
                priority=FeePlanPriority(**response["data"]["plans"]["priority"])
            )
        )
    

class _PlisioInvoice(_BaseAIOPlisioClient):

    async def create(
        self,
        order_name: str,
        order_number: int,
        *,
        language: str="en_US",
        currency: Optional[str] | Optional[CryptoCurrency] | None=None,
        source_currency: Optional[str] | Optional[FiatCurrency] | None=None,
        source_amount: Optional[float] | None=None,
        amount: Optional[float] | None=None,
        allowed_psys_cids: Optional[List[str]] | Optional[List[CryptoCurrency]] | None=None,
        description: Optional[str] | None=None,
        callback_url: Optional[str] | None=None,
        success_callback_url: Optional[str] | None=None,
        fail_callback_url: Optional[str] | None=None,
        email: Optional[str] | None=None,
        plugin: Optional[Any] | None=None,
        version: Optional[Any] | None=None,
        redirect_to_invoice: Optional[str] | None=None,
        expire_min: Optional[int] | None=None
    ) -> Invoice:
        payload = {
            "order_name": order_name,
            "order_number": order_number,
            "language": language,
            "currency": currency.name if not isinstance(currency, str) else str(currency),
            "source_currency": source_currency.name if not isinstance(currency, str) else str(source_currency),
            "source_amount": source_amount,
            "amount": amount,
            "allowed_psys_cids": ",".join(
                    apc.name if not isinstance(apc, str) else apc
                    for apc in allowed_psys_cids
                ) if allowed_psys_cids is not None else None,
            "description": description,
            "callback_url": callback_url,
            "success_callback_url": success_callback_url,
            "fail_callback_url": fail_callback_url,
            "email": email,
            "plugin": plugin,
            "version": version,
            "redirect_to_invoice": redirect_to_invoice,
            "expire_min": expire_min,
            "api_key": self._api_key
        }
        payload = {k: v for k, v in payload.items() if v is not None}

        response = await self._make_request("invoices/new", params=payload)
        return Invoice(status=response["status"], data=InvoiceData(**response["data"]))