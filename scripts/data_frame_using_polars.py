import polars as pl


def get_raw_data():
    return {
        "id":[1,2,3,4,5],
        "name":["ab","ac","ad","ae","af"],
        "salary":[14000,14000,15000,14000,16000],
        "dept":["sales","market","sales","sales","market"]
    }

if __name__=="__main__":
    df = pl.DataFrame(get_raw_data())
    df.show()
    avg_sal_df = df.group_by(pl.col("dept")).agg(
        pl.col("salary").mean().alias("Avg_salary"),
        pl.col("salary").max().alias("Max_salary"),
        pl.col("salary").min().alias("Min_salary"),
    )
    avg_sal_df.show()

