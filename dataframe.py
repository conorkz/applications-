from pyspark.sql import functions as F

def get_product_category_pairs(products_df, categories_df, product_cat_df):
    joined_df = products_df.alias('p') \
        .join(product_cat_df.alias('pc'), 'product_id', how='left') \
        .join(categories_df.alias('c'), 'category_id', how='left') \
        .select('p.product_name', 'c.category_name')
    products_without_categories = products_df \
        .join(product_cat_df, 'product_id', how='leftanti') \
        .select('product_name')
    result_df = joined_df.union(products_without_categories.withColumn('category_name', F.lit(None)))
    return result_df
