"""
Order data payloads for Locust testing.
Contains sample Shopify order data for testing the sync-shopify-orders endpoint.
"""

ORDER_DATA = {
    "request_data": {
        "order": {
            "id": 6525950329008,
            "admin_graphql_api_id": "gid://shopify/Order/6525950329008",
            "app_id": 1354745,
            "browser_ip": "197.39.114.25",
            "buyer_accepts_marketing": False,
            "cancel_reason": None,
            "cancelled_at": None,
            "cart_token": None,
            "checkout_id": 30124895207600,
            "checkout_token": "78303283499efe82ff1112bc1292329d",
            "client_details": {
                "accept_language": None,
                "browser_height": None,
                "browser_ip": "197.39.114.25",
                "browser_width": None,
                "session_hash": None,
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
            },
            "closed_at": None,
            "confirmation_number": "AGLJZCAZW",
            "confirmed": True,
            "contact_email": None,
            "created_at": "2025-07-01T12:33:23+03:00",
            "currency": "EGP",
            "current_shipping_price_set": {
                "shop_money": {
                    "amount": "50.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "50.00",
                    "currency_code": "EGP"
                }
            },
            "current_subtotal_price": "150.00",
            "current_subtotal_price_set": {
                "shop_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                }
            },
            "current_total_additional_fees_set": None,
            "current_total_discounts": "150.00",
            "current_total_discounts_set": {
                "shop_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                }
            },
            "current_total_duties_set": None,
            "current_total_price": "200.00",
            "current_total_price_set": {
                "shop_money": {
                    "amount": "200.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "200.00",
                    "currency_code": "EGP"
                }
            },
            "current_total_tax": "0.00",
            "current_total_tax_set": {
                "shop_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                }
            },
            "customer_locale": "en",
            "device_id": None,
            "discount_codes": [
                {
                    "code": "C4",
                    "amount": "150.00",
                    "type": "percentage"
                }
            ],
            "duties_included": False,
            "email": "",
            "estimated_taxes": False,
            "financial_status": "pending",
            "fulfillment_status": None,
            "landing_site": None,
            "landing_site_ref": None,
            "location_id": None,
            "merchant_business_entity_id": "MTY3MjM2MzY0NDY0",
            "merchant_of_record_app_id": None,
            "name": "#15814",
            "note": None,
            "note_attributes": [],
            "number": 14814,
            "order_number": 15814,
            "order_status_url": "https://store.mypremierpharma.com/67236364464/orders/8fefc3155079eff272c1a600cdcfcea3/authenticate?key=009b4b3e6b279129a2c3105c8503417f",
            "original_total_additional_fees_set": None,
            "original_total_duties_set": None,
            "payment_gateway_names": [],
            "phone": None,
            "po_number": None,
            "presentment_currency": "EGP",
            "processed_at": "2025-07-01T12:33:23+03:00",
            "reference": None,
            "referring_site": None,
            "source_identifier": None,
            "source_name": "shopify_draft_order",
            "source_url": None,
            "subtotal_price": "150.00",
            "subtotal_price_set": {
                "shop_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                }
            },
            "tags": "Website whatsapp",
            "tax_exempt": False,
            "tax_lines": [],
            "taxes_included": False,
            "test": False,
            "token": "8fefc3155079eff272c1a600cdcfcea3",
            "total_cash_rounding_payment_adjustment_set": {
                "shop_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                }
            },
            "total_cash_rounding_refund_adjustment_set": {
                "shop_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                }
            },
            "total_discounts": "150.00",
            "total_discounts_set": {
                "shop_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "150.00",
                    "currency_code": "EGP"
                }
            },
            "total_line_items_price": "300.00",
            "total_line_items_price_set": {
                "shop_money": {
                    "amount": "300.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "300.00",
                    "currency_code": "EGP"
                }
            },
            "total_outstanding": "200.00",
            "total_price": "200.00",
            "total_price_set": {
                "shop_money": {
                    "amount": "200.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "200.00",
                    "currency_code": "EGP"
                }
            },
            "total_shipping_price_set": {
                "shop_money": {
                    "amount": "50.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "50.00",
                    "currency_code": "EGP"
                }
            },
            "total_tax": "0.00",
            "total_tax_set": {
                "shop_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                },
                "presentment_money": {
                    "amount": "0.00",
                    "currency_code": "EGP"
                }
            },
            "total_tip_received": "0.00",
            "total_weight": 1000,
            "updated_at": "2025-07-01T12:35:06+03:00",
            "user_id": 90191036592,
            "billing_address": {
                "first_name": "ضحي",
                "address1": "01210199309 اسديمه مركز كفر الزيات الغربيه عند جامع البسطامي",
                "phone": "+201207845738",
                "city": "كفر الزيات",
                "zip": None,
                "province": "Gharbia",
                "country": "Egypt",
                "last_name": "عادل",
                "address2": None,
                "company": None,
                "latitude": 30.8815112,
                "longitude": 30.8321716,
                "name": "ضحي عادل",
                "country_code": "EG",
                "province_code": "GH"
            },
            "customer": {
                "id": 8547379904688,
                "email": None,
                "created_at": "2025-07-01T12:32:20+03:00",
                "updated_at": "2025-07-01T12:33:24+03:00",
                "first_name": "ضحي",
                "last_name": "عادل",
                "state": "disabled",
                "note": None,
                "verified_email": True,
                "multipass_identifier": None,
                "tax_exempt": False,
                "phone": None,
                "currency": "EGP",
                "tax_exemptions": [],
                "admin_graphql_api_id": "gid://shopify/Customer/8547379904688",
                "default_address": {
                    "id": 9907384942768,
                    "customer_id": 8547379904688,
                    "first_name": "ضحي",
                    "last_name": "عادل",
                    "company": "",
                    "address1": "01210199309 اسديمه مركز كفر الزيات الغربيه عند جامع البسطامي ",
                    "address2": "",
                    "city": "كفر الزيات",
                    "province": "Gharbia",
                    "country": "Egypt",
                    "zip": "",
                    "phone": "+201207845738",
                    "name": "ضحي عادل",
                    "province_code": "GH",
                    "country_code": "EG",
                    "country_name": "Egypt",
                    "default": True
                }
            },
            "discount_applications": [
                {
                    "target_type": "line_item",
                    "type": "discount_code",
                    "value": "50.0",
                    "value_type": "percentage",
                    "allocation_method": "each",
                    "target_selection": "entitled",
                    "code": "C4"
                }
            ],
            "fulfillments": [],
            "line_items": [
                {
                    "id": 15885687455920,
                    "admin_graphql_api_id": "gid://shopify/LineItem/15885687455920",
                    "attributed_staffs": [],
                    "current_quantity": 1,
                    "fulfillable_quantity": 1,
                    "fulfillment_service": "manual",
                    "fulfillment_status": None,
                    "gift_card": False,
                    "grams": 1000,
                    "name": "facial cleanser with brush",
                    "price": "300.00",
                    "price_set": {
                        "shop_money": {
                            "amount": "300.00",
                            "currency_code": "EGP"
                        },
                        "presentment_money": {
                            "amount": "300.00",
                            "currency_code": "EGP"
                        }
                    },
                    "product_exists": True,
                    "product_id": 7782703169712,
                    "properties": [],
                    "quantity": 1,
                    "requires_shipping": True,
                    "sales_line_item_group_id": None,
                    "sku": "PS01",
                    "taxable": False,
                    "title": "facial cleanser with brush",
                    "total_discount": "0.00",
                    "total_discount_set": {
                        "shop_money": {
                            "amount": "0.00",
                            "currency_code": "EGP"
                        },
                        "presentment_money": {
                            "amount": "0.00",
                            "currency_code": "EGP"
                        }
                    },
                    "variant_id": 44189234069680,
                    "variant_inventory_management": None,
                    "variant_title": None,
                    "vendor": "Premier",
                    "tax_lines": [],
                    "duties": [],
                    "discount_allocations": [
                        {
                            "amount": "150.00",
                            "amount_set": {
                                "shop_money": {
                                    "amount": "150.00",
                                    "currency_code": "EGP"
                                },
                                "presentment_money": {
                                    "amount": "150.00",
                                    "currency_code": "EGP"
                                }
                            },
                            "discount_application_index": 0
                        }
                    ]
                }
            ],
            "payment_terms": {
                "id": 25855885488,
                "created_at": "2025-07-01T12:33:23+03:00",
                "due_in_days": None,
                "payment_schedules": [],
                "payment_terms_name": "Due on receipt",
                "payment_terms_type": "receipt",
                "updated_at": "2025-07-01T12:33:23+03:00"
            },
            "refunds": [],
            "shipping_address": {
                "first_name": "ضحي",
                "address1": "01210199309 اسديمه مركز كفر الزيات الغربيه عند جامع البسطامي",
                "phone": "+201207845738",
                "city": "كفر الزيات",
                "zip": None,
                "province": "Gharbia",
                "country": "Egypt",
                "last_name": "عادل",
                "address2": None,
                "company": None,
                "latitude": 30.8815112,
                "longitude": 30.8321716,
                "name": "ضحي عادل",
                "country_code": "EG",
                "province_code": "GH"
            },
            "shipping_lines": [
                {
                    "id": 5494848487600,
                    "carrier_identifier": None,
                    "code": "Standard",
                    "current_discounted_price_set": {
                        "shop_money": {
                            "amount": "50.00",
                            "currency_code": "EGP"
                        }
                    }
                }
            ]
        }
    }
}