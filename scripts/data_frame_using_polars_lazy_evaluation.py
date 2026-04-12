import polars as pl
import os

def get_raw_data():
    return {
        "id":[1,2,3,4,5],
        "name":["ab","ac","ad","ae","af"],
        "salary":[14000,14000,15000,14000,16000],
        "dept":["sales","market","sales","sales","market"]
    }

if __name__=="__main__":
    file_path = os.path.join("..","data_files","employees.csv")
    lazy_df = pl.scan_csv(file_path)

    avg_sal_df = (
        lazy_df.group_by(pl.col("dept")).agg(
        pl.col("salary").mean().alias("Avg_salary"),
        pl.col("salary").max().alias("Max_salary"),
        pl.col("salary").min().alias("Min_salary"),
        )
    )
    print(avg_sal_df.explain())

    result = avg_sal_df.collect() # lazy dataframe will return a dataframe after collect()
    result.show()
    print(f"Final Dataframe type is {type(result)} where as original is {type(avg_sal_df)}")

