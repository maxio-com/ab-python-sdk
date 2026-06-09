
# Invoice-Event-Payment

A nested data structure detailing the method of payment

## Data Type

`PaymentMethodApplePay | PaymentMethodBankAccount | PaymentMethodCreditCard | PaymentMethodExternal | PaymentMethodPaypal`

## Cases

| Type |
|  --- |
| [`PaymentMethodApplePay`](../../../doc/models/payment-method-apple-pay.md) |
| [`PaymentMethodBankAccount`](../../../doc/models/payment-method-bank-account.md) |
| [`PaymentMethodCreditCard`](../../../doc/models/payment-method-credit-card.md) |
| [`PaymentMethodExternal`](../../../doc/models/payment-method-external.md) |
| [`PaymentMethodPaypal`](../../../doc/models/payment-method-paypal.md) |

## PaymentMethodApplePay

### Initialization Code

#### Example

```python
value = PaymentMethodApplePay(
    mtype=InvoiceEventPaymentMethod.APPLE_PAY
)
```

## PaymentMethodBankAccount

### Initialization Code

#### Example

```python
value = PaymentMethodBankAccount(
    masked_account_number='masked_account_number2',
    masked_routing_number='masked_routing_number2',
    mtype=InvoiceEventPaymentMethod.BANK_ACCOUNT
)
```

## PaymentMethodCreditCard

### Initialization Code

#### Example

```python
value = PaymentMethodCreditCard(
    card_brand='card_brand4',
    masked_card_number='masked_card_number0',
    mtype=InvoiceEventPaymentMethod.CREDIT_CARD
)
```

## PaymentMethodExternal

### Initialization Code

#### Example

```python
value = PaymentMethodExternal(
    details='details4',
    kind='kind2',
    memo='memo8',
    mtype=InvoiceEventPaymentMethod.EXTERNAL
)
```

## PaymentMethodPaypal

### Initialization Code

#### Example

```python
value = PaymentMethodPaypal(
    email='email2',
    mtype=InvoiceEventPaymentMethod.PAYPAL_ACCOUNT
)
```

