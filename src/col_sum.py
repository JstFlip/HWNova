import os

import pandas as pd


def cond_sum(df: pd.DataFrame, cond: pd.Series, col_sum: str) -> int:
    """
    :param pd.DataFrame df: Dataframe which will be used
    :param pd.Series cond: Pandas condition for specified dataframe
    :param str col_sum: Column which will be summed
    :return int: sum of a column col_sum
    """
    return df[cond][col_sum].sum()


if __name__ == "__main__":
    base_path = f"{os.getcwd()}/resources/"
    files = [os.path.join(base_path, f) for f in os.listdir(base_path)]

    for file in files:
        df = pd.read_csv(file, usecols=["a", "b"])  # Load only two columns needed
        res = cond_sum(df, df["b"] == "foo", "a")
        print(f"Sum for file {file} is: {res}")
