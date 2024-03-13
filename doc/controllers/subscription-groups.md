# Subscription Groups

```python
subscription_groups_controller = client.subscription_groups
```

## Class Name

`SubscriptionGroupsController`

## Methods

* [Signup With Subscription Group](../../doc/controllers/subscription-groups.md#signup-with-subscription-group)
* [Create Subscription Group](../../doc/controllers/subscription-groups.md#create-subscription-group)
* [List Subscription Groups](../../doc/controllers/subscription-groups.md#list-subscription-groups)
* [Read Subscription Group](../../doc/controllers/subscription-groups.md#read-subscription-group)
* [Update Subscription Group Members](../../doc/controllers/subscription-groups.md#update-subscription-group-members)
* [Delete Subscription Group](../../doc/controllers/subscription-groups.md#delete-subscription-group)
* [Find Subscription Group](../../doc/controllers/subscription-groups.md#find-subscription-group)
* [Add Subscription to Group](../../doc/controllers/subscription-groups.md#add-subscription-to-group)
* [Remove Subscription From Group](../../doc/controllers/subscription-groups.md#remove-subscription-from-group)


# Signup With Subscription Group

Create multiple subscriptions at once under the same customer and consolidate them into a subscription group.

You must provide one and only one of the `payer_id`/`payer_reference`/`payer_attributes` for the customer attached to the group.

You must provide one and only one of the `payment_profile_id`/`credit_card_attributes`/`bank_account_attributes` for the payment profile attached to the group.

Only one of the `subscriptions` can have `"primary": true` attribute set.

When passing product to a subscription you can use either `product_id` or `product_handle` or `offer_id`. You can also use `custom_price` instead.

```python
def signup_with_subscription_group(self,
                                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubscriptionGroupSignupRequest`](../../doc/models/subscription-group-signup-request.md) | Body, Optional | - |

## Response Type

[`SubscriptionGroupSignupResponse`](../../doc/models/subscription-group-signup-response.md)

## Example Usage

```python
body = SubscriptionGroupSignupRequest(
    subscription_group=SubscriptionGroupSignup(
        subscriptions=[
            SubscriptionGroupSignupItem(
                product_id=11,
                primary=True
            ),
            SubscriptionGroupSignupItem(
                product_id=12
            ),
            SubscriptionGroupSignupItem(
                product_id=13
            )
        ],
        payment_profile_id=123,
        payer_id=123
    )
)

result = subscription_groups_controller.signup_with_subscription_group(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`SubscriptionGroupSignupErrorResponseException`](../../doc/models/subscription-group-signup-error-response-exception.md) |


# Create Subscription Group

Creates a subscription group with given members.

```python
def create_subscription_group(self,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateSubscriptionGroupRequest`](../../doc/models/create-subscription-group-request.md) | Body, Optional | - |

## Response Type

[`SubscriptionGroupResponse`](../../doc/models/subscription-group-response.md)

## Example Usage

```python
body = CreateSubscriptionGroupRequest(
    subscription_group=CreateSubscriptionGroup(
        subscription_id=1,
        member_ids=[
            2,
            3,
            4
        ]
    )
)

result = subscription_groups_controller.create_subscription_group(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "subscription_group": {
    "customer_id": 1,
    "payment_profile": {
      "id": 1,
      "first_name": "t",
      "last_name": "t",
      "masked_card_number": "XXXX-XXXX-XXXX-1"
    },
    "payment_collection_method": "automatic",
    "subscription_ids": [
      1,
      2
    ],
    "created_at": "2021-01-21T05:47:38-05:00"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`SubscriptionGroupCreateErrorResponseException`](../../doc/models/subscription-group-create-error-response-exception.md) |


# List Subscription Groups

Returns an array of subscription groups for the site. The response is paginated and will return a `meta` key with pagination information.

#### Account Balance Information

Account balance information for the subscription groups is not returned by default. If this information is desired, the `include[]=account_balances` parameter must be provided with the request.

```python
def list_subscription_groups(self,
                            options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`. |
| `include` | [`List[SubscriptionGroupsListInclude]`](../../doc/models/subscription-groups-list-include.md) | Query, Optional | A list of additional information to include in the response. The following values are supported:<br><br>- `account_balances`: Account balance information for the subscription groups. Use in query: `include[]=account_balances` |

## Response Type

[`ListSubscriptionGroupsResponse`](../../doc/models/list-subscription-groups-response.md)

## Example Usage

```python
collect = {Liquid error: Value cannot be null. (Parameter 'key')
    'page': 2,
    'per_page': 50
}
result = subscription_groups_controller.list_subscription_groups(collect)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "subscription_groups": [
    {
      "uid": "grp_952mvqcnk53wq",
      "scheme": 1,
      "customer_id": 88498000,
      "payment_profile_id": 93063018,
      "subscription_ids": [
        42768907,
        82370782
      ],
      "primary_subscription_id": 69844395,
      "next_assessment_at": "2021-05-05T16:00:21-04:00",
      "state": "active",
      "cancel_at_end_of_period": false,
      "account_balances": {
        "prepayments": {
          "balance_in_cents": 0
        },
        "service_credits": {
          "balance_in_cents": 0
        },
        "pending_discounts": {
          "balance_in_cents": 0
        }
      }
    }
  ],
  "meta": {
    "current_page": 1,
    "total_count": 1
  }
}
```


# Read Subscription Group

Use this endpoint to find subscription group details.

#### Current Billing Amount in Cents

Current billing amount for the subscription group is not returned by default. If this information is desired, the `include[]=current_billing_amount_in_cents` parameter must be provided with the request.

```python
def read_subscription_group(self,
                           uid,
                           include=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `include` | [`List[SubscriptionGroupInclude]`](../../doc/models/subscription-group-include.md) | Query, Optional | Allows including additional data in the response. Use in query: `include[]=current_billing_amount_in_cents`. |

## Response Type

[`FullSubscriptionGroupResponse`](../../doc/models/full-subscription-group-response.md)

## Example Usage

```python
uid = 'uid0'

Liquid error: Value cannot be null. (Parameter 'key')result = subscription_groups_controller.read_subscription_group(Liquid error: Value cannot be null. (Parameter 'key')uid)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "uid": "grp_939ktzq8v4477",
  "scheme": 1,
  "customer_id": 400,
  "payment_profile_id": 567,
  "subscription_ids": [
    101,
    102,
    103
  ],
  "primary_subscription_id": 101,
  "next_assessment_at": "2020-08-01T14:00:00-05:00",
  "state": "active",
  "cancel_at_end_of_period": false,
  "current_billing_amount_in_cents": 11500,
  "customer": {
    "first_name": "Mark",
    "last_name": "Wannabewahlberg",
    "organization": "The Funky Bunch",
    "email": "markymark@example.com",
    "reference": "4c92223b-bc16-4d0d-87ff-b177a89a2655"
  },
  "account_balances": {
    "prepayments": {
      "balance_in_cents": 0
    },
    "service_credits": {
      "balance_in_cents": 0
    },
    "open_invoices": {
      "balance_in_cents": 4400
    },
    "pending_discounts": {
      "balance_in_cents": 0
    }
  }
}
```


# Update Subscription Group Members

Use this endpoint to update subscription group members.
`"member_ids": []` should contain an array of both subscription IDs to set as group members and subscription IDs already present in the groups. Not including them will result in removing them from subscription group. To clean up members, just leave the array empty.

```python
def update_subscription_group_members(self,
                                     uid,
                                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `body` | [`UpdateSubscriptionGroupRequest`](../../doc/models/update-subscription-group-request.md) | Body, Optional | - |

## Response Type

[`SubscriptionGroupResponse`](../../doc/models/subscription-group-response.md)

## Example Usage

```python
uid = 'uid0'

body = UpdateSubscriptionGroupRequest(
    subscription_group=UpdateSubscriptionGroup(
        member_ids=[
            1,
            2,
            3
        ]
    )
)

result = subscription_groups_controller.update_subscription_group_members(
    uid,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "subscription_group": {
    "customer_id": 1,
    "payment_profile": {
      "id": 1,
      "first_name": "t",
      "last_name": "t",
      "masked_card_number": "XXXX-XXXX-XXXX-1"
    },
    "payment_collection_method": "automatic",
    "subscription_ids": [
      1
    ],
    "created_at": "2021-01-21T05:47:38-05:00"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`SubscriptionGroupUpdateErrorResponseException`](../../doc/models/subscription-group-update-error-response-exception.md) |


# Delete Subscription Group

Use this endpoint to delete subscription group.
Only groups without members can be deleted

```python
def delete_subscription_group(self,
                             uid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |

## Response Type

[`DeleteSubscriptionGroupResponse`](../../doc/models/delete-subscription-group-response.md)

## Example Usage

```python
uid = 'uid0'

result = subscription_groups_controller.delete_subscription_group(uid)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "uid": "grp_99w5xp9y5xycy",
  "deleted": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Find Subscription Group

Use this endpoint to find subscription group associated with subscription.

If the subscription is not in a group endpoint will return 404 code.

```python
def find_subscription_group(self,
                           subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Query, Required | The Chargify id of the subscription associated with the subscription group |

## Response Type

[`FullSubscriptionGroupResponse`](../../doc/models/full-subscription-group-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscription_groups_controller.find_subscription_group(subscription_id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "uid": "grp_939ktzq8v4477",
  "scheme": 1,
  "customer_id": 400,
  "payment_profile_id": 567,
  "subscription_ids": [
    101,
    102,
    103
  ],
  "primary_subscription_id": 101,
  "next_assessment_at": "2020-08-01T14:00:00-05:00",
  "state": "active",
  "cancel_at_end_of_period": false,
  "customer": {
    "first_name": "Mark",
    "last_name": "Wannabewahlberg",
    "organization": "The Funky Bunch",
    "email": "markymark@example.com",
    "reference": "4c92223b-bc16-4d0d-87ff-b177a89a2655"
  },
  "account_balances": {
    "prepayments": {
      "balance_in_cents": 0
    },
    "service_credits": {
      "balance_in_cents": 0
    },
    "open_invoices": {
      "balance_in_cents": 4400
    },
    "pending_discounts": {
      "balance_in_cents": 0
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Add Subscription to Group

For sites making use of the [Relationship Billing](https://chargify.zendesk.com/hc/en-us/articles/4407737494171) and [Customer Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/4407746683291) features, it is possible to add existing subscriptions to subscription groups.

Passing `group` parameters with a `target` containing a `type` and optional `id` is all that's needed. When the `target` parameter specifies a `"customer"` or `"subscription"` that is already part of a hierarchy, the subscription will become a member of the customer's subscription group.  If the target customer or subscription is not part of a subscription group, a new group will be created and the subscription will become part of the group with the specified target customer set as the responsible payer for the group's subscriptions.

**Please Note:** In order to add an existing subscription to a subscription group, it must belong to either the same customer record as the target, or be within the same customer hierarchy.

Rather than specifying a customer, the `target` parameter could instead simply have a value of

* `"self"` which indicates the subscription will be paid for not by some other customer, but by the subscribing customer,
* `"parent"` which indicates the subscription will be paid for by the subscribing customer's parent within a customer hierarchy, or
* `"eldest"` which indicates the subscription will be paid for by the root-level customer in the subscribing customer's hierarchy.

To create a new subscription into a subscription group, please reference the following:
[Create Subscription in a Subscription Group](https://developers.chargify.com/docs/api-docs/d571659cf0f24-create-subscription#subscription-in-a-subscription-group)

```python
def add_subscription_to_group(self,
                             subscription_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `body` | [`AddSubscriptionToAGroup`](../../doc/models/add-subscription-to-a-group.md) | Body, Optional | - |

## Response Type

[`SubscriptionGroupResponse`](../../doc/models/subscription-group-response.md)

## Example Usage

```python
subscription_id = 222

body = AddSubscriptionToAGroup(
    group=GroupSettings(
        target=GroupTarget(
            mtype=GroupTargetType.SUBSCRIPTION,
            id=32987
        ),
        billing=GroupBilling(
            accrue=True,
            align_date=True,
            prorate=True
        )
    )
)

result = subscription_groups_controller.add_subscription_to_group(
    subscription_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "subscription_group": {
    "customer_id": 130690,
    "payment_profile": {
      "id": 32055,
      "first_name": "Marty",
      "last_name": "McFly",
      "masked_card_number": "XXXX-XXXX-XXXX-1111"
    },
    "subscription_ids": [
      32988,
      33060,
      32986
    ],
    "created_at": "2018-08-30T17:14:30-04:00"
  }
}
```


# Remove Subscription From Group

For sites making use of the [Relationship Billing](https://chargify.zendesk.com/hc/en-us/articles/4407737494171) and [Customer Hierarchy](https://chargify.zendesk.com/hc/en-us/articles/4407746683291) features, it is possible to remove existing subscription from subscription group.

```python
def remove_subscription_from_group(self,
                                  subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |

## Response Type

`void`

## Example Usage

```python
subscription_id = 222

result = subscription_groups_controller.remove_subscription_from_group(subscription_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

