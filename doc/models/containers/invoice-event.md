
# Invoice-Event

## Data Type

`ApplyCreditNoteEvent | ApplyDebitNoteEvent | ApplyPaymentEvent | BackportInvoiceEvent | ChangeChargebackStatusEvent | ChangeInvoiceCollectionMethodEvent | ChangeInvoiceStatusEvent | CreateCreditNoteEvent | CreateDebitNoteEvent | FailedPaymentEvent | IssueInvoiceEvent | RefundInvoiceEvent | RemovePaymentEvent | VoidInvoiceEvent | VoidRemainderEvent`

## Cases

| Type |
|  --- |
| [`ApplyCreditNoteEvent`](../../../doc/models/apply-credit-note-event.md) |
| [`ApplyDebitNoteEvent`](../../../doc/models/apply-debit-note-event.md) |
| [`ApplyPaymentEvent`](../../../doc/models/apply-payment-event.md) |
| [`BackportInvoiceEvent`](../../../doc/models/backport-invoice-event.md) |
| [`ChangeChargebackStatusEvent`](../../../doc/models/change-chargeback-status-event.md) |
| [`ChangeInvoiceCollectionMethodEvent`](../../../doc/models/change-invoice-collection-method-event.md) |
| [`ChangeInvoiceStatusEvent`](../../../doc/models/change-invoice-status-event.md) |
| [`CreateCreditNoteEvent`](../../../doc/models/create-credit-note-event.md) |
| [`CreateDebitNoteEvent`](../../../doc/models/create-debit-note-event.md) |
| [`FailedPaymentEvent`](../../../doc/models/failed-payment-event.md) |
| [`IssueInvoiceEvent`](../../../doc/models/issue-invoice-event.md) |
| [`RefundInvoiceEvent`](../../../doc/models/refund-invoice-event.md) |
| [`RemovePaymentEvent`](../../../doc/models/remove-payment-event.md) |
| [`VoidInvoiceEvent`](../../../doc/models/void-invoice-event.md) |
| [`VoidRemainderEvent`](../../../doc/models/void-remainder-event.md) |

## ApplyCreditNoteEvent

### Initialization Code

#### Example

```python
value = ApplyCreditNoteEvent(
    id=214,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.APPLY_CREDIT_NOTE,
    event_data=ApplyCreditNoteEventData(
        uid='uid6',
        credit_note_number='credit_note_number0',
        credit_note_uid='credit_note_uid0',
        original_amount='original_amount0',
        applied_amount='applied_amount2'
    )
)
```

## ApplyDebitNoteEvent

### Initialization Code

#### Example

```python
value = ApplyDebitNoteEvent(
    id=164,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.APPLY_DEBIT_NOTE,
    event_data=ApplyDebitNoteEventData(
        debit_note_number='debit_note_number6',
        debit_note_uid='debit_note_uid2',
        original_amount='original_amount0',
        applied_amount='applied_amount2'
    )
)
```

## ApplyPaymentEvent

### Initialization Code

#### Example

```python
value = ApplyPaymentEvent(
    id=234,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.APPLY_PAYMENT,
    event_data=ApplyPaymentEventData(
        consolidation_level=InvoiceConsolidationLevel.CHILD,
        memo='memo0',
        original_amount='original_amount0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        payment_method=PaymentMethodApplePay(
            mtype=InvoiceEventPaymentMethod.APPLE_PAY
        )
    )
)
```

## BackportInvoiceEvent

### Initialization Code

#### Example

```python
value = BackportInvoiceEvent(
    id=78,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.BACKPORT_INVOICE,
    event_data=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    )
)
```

## ChangeChargebackStatusEvent

### Initialization Code

#### Example

```python
value = ChangeChargebackStatusEvent(
    id=214,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.CHANGE_CHARGEBACK_STATUS,
    event_data=ChangeChargebackStatusEventData(
        chargeback_status=ChargebackStatus.WON
    )
)
```

## ChangeInvoiceCollectionMethodEvent

### Initialization Code

#### Example

```python
value = ChangeInvoiceCollectionMethodEvent(
    id=246,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.CHANGE_INVOICE_COLLECTION_METHOD,
    event_data=ChangeInvoiceCollectionMethodEventData(
        from_collection_method='from_collection_method4',
        to_collection_method='to_collection_method8'
    )
)
```

## ChangeInvoiceStatusEvent

### Initialization Code

#### Example

```python
value = ChangeInvoiceStatusEvent(
    id=92,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.CHANGE_INVOICE_STATUS,
    event_data=ChangeInvoiceStatusEventData(
        from_status=InvoiceStatus.OPEN,
        to_status=InvoiceStatus.PENDING
    )
)
```

## CreateCreditNoteEvent

### Initialization Code

#### Example

```python
value = CreateCreditNoteEvent(
    id=28,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.CREATE_CREDIT_NOTE,
    event_data=CreditNote()
)
```

## CreateDebitNoteEvent

### Initialization Code

#### Example

```python
value = CreateDebitNoteEvent(
    id=98,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.CREATE_DEBIT_NOTE,
    event_data=DebitNote()
)
```

## FailedPaymentEvent

### Initialization Code

#### Example

```python
value = FailedPaymentEvent(
    id=120,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.FAILED_PAYMENT,
    event_data=FailedPaymentEventData(
        amount_in_cents=220,
        applied_amount=194,
        payment_method=InvoicePaymentMethodType.CASH,
        transaction_id=78
    )
)
```

## IssueInvoiceEvent

### Initialization Code

#### Example

```python
value = IssueInvoiceEvent(
    id=130,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.ISSUE_INVOICE,
    event_data=IssueInvoiceEventData(
        consolidation_level=InvoiceConsolidationLevel.CHILD,
        from_status=InvoiceStatus.OPEN,
        to_status=InvoiceStatus.PENDING,
        due_amount='due_amount8',
        total_amount='total_amount2'
    )
)
```

## RefundInvoiceEvent

### Initialization Code

#### Example

```python
value = RefundInvoiceEvent(
    id=54,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.REFUND_INVOICE,
    event_data=RefundInvoiceEventData(
        apply_credit=False,
        credit_note_attributes=CreditNote(),
        payment_id=204,
        refund_amount='refund_amount8',
        refund_id=248,
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

## RemovePaymentEvent

### Initialization Code

#### Example

```python
value = RemovePaymentEvent(
    id=236,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.REMOVE_PAYMENT,
    event_data=RemovePaymentEventData(
        transaction_id=78,
        memo='memo0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        payment_method=PaymentMethodApplePay(
            mtype=InvoiceEventPaymentMethod.APPLE_PAY
        ),
        prepayment=False
    )
)
```

## VoidInvoiceEvent

### Initialization Code

#### Example

```python
value = VoidInvoiceEvent(
    id=16,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.VOID_INVOICE,
    event_data=VoidInvoiceEventData(
        credit_note_attributes=CreditNote(),
        memo='memo0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        is_advance_invoice=False,
        reason='reason2'
    )
)
```

## VoidRemainderEvent

### Initialization Code

#### Example

```python
value = VoidRemainderEvent(
    id=128,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.VOID_REMAINDER,
    event_data=VoidRemainderEventData(
        credit_note_attributes=CreditNote(),
        memo='memo0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

