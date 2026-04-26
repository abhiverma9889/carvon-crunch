def generate_summary(data_list):
    total = 0
    store_spend = {}

    for item in data_list:
        store = item["store_name"]["value"]
        value = item["total_amount"]["value"]

        try:
            amount = float(value)
            total += amount

            if store:
                store_spend[store] = store_spend.get(store, 0) + amount
        except:
            continue

    return {
        "total_spend": total,
        "transactions": len(data_list),
        "spend_per_store": store_spend
    }