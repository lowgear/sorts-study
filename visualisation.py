import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


def visualize(results, args):
    sns.set(style="darkgrid")

    # Load the example titanic dataset
    df = sns.load_dataset("titanic")

    # Make a custom palette with gendered colors
    pal = dict(male="#6495ED", female="#F08080")

    # Show the survival proability as a function of age and sex
    g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
                   palette=pal, y_jitter=.02, logistic=True)
    g.set(xlim=(0, 80), ylim=(-.05, 1.05))


# def get_data_home(data_home=None):
#     """Return the path of the seaborn data directory.
#
#     This is used by the ``load_dataset`` function.
#
#     If the ``data_home`` argument is not specified, the default location
#     is ``~/seaborn-data``.
#
#     Alternatively, a different default location can be specified using the
#     environment variable ``SEABORN_DATA``.
#     """
#     if data_home is None:
#         data_home = os.environ.get('SEABORN_DATA',
#                                    os.path.join('~', 'seaborn-data'))
#     data_home = os.path.expanduser(data_home)
#     if not os.path.exists(data_home):
#         os.makedirs(data_home)
#     return data_home
#
#
# def load_dataset(name, cache=True, data_home=None, **kws):
#     """Load a dataset from the online repository (requires internet).
#
#     Parameters
#     ----------
#     name : str
#         Name of the dataset (`name`.csv on
#         https://github.com/mwaskom/seaborn-data).  You can obtain list of
#         available datasets using :func:`get_dataset_names`
#     cache : boolean, optional
#         If True, then cache data locally and use the cache on subsequent calls
#     data_home : string, optional
#         The directory in which to cache data. By default, uses ~/seaborn-data/
#     kws : dict, optional
#         Passed to pandas.read_csv
#
#     """
#     path = ("https://raw.githubusercontent.com/"
#             "mwaskom/seaborn-data/master/{}.csv")
#     full_path = path.format(name)
#
#     if cache:
#         cache_path = os.path.join(get_data_home(data_home),
#                                   os.path.basename(full_path))
#         if not os.path.exists(cache_path):
#             urlretrieve(full_path, cache_path)
#         full_path = cache_path
#
#     df = pd.read_csv(full_path, **kws)
#     if df.iloc[-1].isnull().all():
#         df = df.iloc[:-1]
#
#     # Set some columns as a categorical type with ordered levels
#
#     if name == "tips":
#         df["day"] = pd.Categorical(df["day"], ["Thur", "Fri", "Sat", "Sun"])
#         df["sex"] = pd.Categorical(df["sex"], ["Male", "Female"])
#         df["time"] = pd.Categorical(df["time"], ["Lunch", "Dinner"])
#         df["smoker"] = pd.Categorical(df["smoker"], ["Yes", "No"])
#
#     if name == "flights":
#         df["month"] = pd.Categorical(df["month"], df.month.unique())
#
#     if name == "exercise":
#         df["time"] = pd.Categorical(df["time"], ["1 min", "15 min", "30 min"])
#         df["kind"] = pd.Categorical(df["kind"], ["rest", "walking", "running"])
#         df["diet"] = pd.Categorical(df["diet"], ["no fat", "low fat"])
#
#     if name == "titanic":
#         df["class"] = pd.Categorical(df["class"], ["First", "Second", "Third"])
#         df["deck"] = pd.Categorical(df["deck"], list("ABCDEFG"))
#
#     return df


if __name__ == "__main__":
    sns.set(style="darkgrid")

    # Load the example titanic dataset
    df = sns.load_dataset("titanic")

    # Make a custom palette with gendered colors
    pal = dict(male="#6495ED", female="#F08080")

    # Show the survival proability as a function of age and sex
    g = sns.lmplot(x="age", y="survived", col="sex", hue="sex", data=df,
                   palette=pal, y_jitter=.02, logistic=True)
    g.set(xlim=(0, 80), ylim=(-.05, 1.05))

    plt.show(g)
