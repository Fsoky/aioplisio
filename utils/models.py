from typing import Optional, Any, List
from datetime import datetime

from pydantic import BaseModel


class Balance(BaseModel):
    status: str
    psys_cid: str
    currency: str
    balance: float


class TransactionsParams(BaseModel):
    order_number: int
    order_name: str
    source_currency: Optional[str] | None = None
    amount: Optional[float] | None = None
    source_rate: float


class TransactionsData(BaseModel):
    user_id: int
    shop_id: str
    type: str
    status: str
    pending_sum: float
    psys_cid: str
    currency: str
    source_currency: str
    source_rate: float
    fee: Optional[float] | None = None
    wallet_hash: str
    sendmany: Optional[Any] | None = None
    params: TransactionsParams
    expire_at_utc: datetime
    created_at_utc: datetime
    amount: float
    sum: float
    commission: float
    tx_url: List[str]
    tx_id: List[str]
    id: str
    actual_sum: float
    actual_commission: Optional[float] | None = None
    actual_fee: Optional[float] | None = None
    actual_invoice_sum: Optional[float] | None = None
    tx: Optional[str] | None = None
    confirmations: int
    status_code: int
    child_ids: List[str]
    parent_id: Optional[List[str]] | None = None



class Transactions(BaseModel):
    status: str
    data: TransactionsData



class FeePlanBaseData(BaseModel):
    key: Optional[str] | None = None
    name: Optional[str] | None = None
    description: Optional[str] | None = None
    gas_limit: Optional[str] | None = None
    gas_price: Optional[str] | None = None
    value: Optional[str] | None = None
    fee_unit: Optional[str] = None
    conf_target: Optional[str] | None = None
    fee_rate: Optional[int] | None = None
    fee_rate_unit: Optional[str] | None = None


class FeePlanEconomy(FeePlanBaseData):
    pass


class FeePlanNormal(FeePlanBaseData):
    pass


class FeePlanPriority(FeePlanBaseData):
    pass


class FeePlan(BaseModel):
    status: Optional[str] | None = None
    economy: Optional[FeePlanEconomy]  | None = None
    normal: Optional[FeePlanNormal] | None = None
    priority: Optional[FeePlanPriority] | None = None


class Comission(BaseModel):
    status: str
    commission: float
    fee: float
    plan: str
    use_wallet: bool
    use_wallet_balance: Optional[bool]
    plans: FeePlan


class InvoiceData(BaseModel):
    txn_id: str
    invoice_url: str
    amount: Optional[float] | None = None
    pending_amount: Optional[float] | None = None
    wallet_hash: Optional[str] | None = None
    psys_cid: Optional[str] | None = None
    currency: Optional[str] | None = None
    status: Optional[str] | None = None
    source_currency: Optional[str] | None = None
    source_rate: Optional[float] | None = None
    expire_utc: Optional[datetime] | None = None
    expected_confirmations: Optional[int] | None = None
    qr_code: Optional[str] | None = None
    verify_hash: Optional[str] | None = None
    invoice_commission: Optional[float] | None = None
    invoice_sum: Optional[float] | None = None
    invoice_total_sum: Optional[float] | None = None


class Invoice(BaseModel):
    status: str
    data: InvoiceData