import pandas as pd

def load_data():
    customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
    orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
    payments = pd.read_csv("data/raw/olist_order_payments_dataset.csv")

    return customers, orders, payments


def build_master():
    customers, orders, payments = load_data()

  
    df = customers.merge(orders, on="customer_id", how="left")

    df = df.merge(payments, on="order_id", how="left")

    return df


if __name__ == "__main__":
    df = build_master()
    
    print(df.head())
    print("\nShape:", df.shape)
    
df.to_csv("data/processed/master_table.csv", index=False)
print("\nArquivo salvo em data/processed/master_table.csv")