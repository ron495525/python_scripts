import matplotlib as mpl
import matplotlib.pyplot as plt
from cycler import cycler

DARK_BLUE = "#2b2d42"
MEDIUM_GREY = "#8d99ae"
LIGHT_GREY = "#edf2f4"
LIGHT_RED = "#ef233c"
DARK_RED = "#d90429"

MPL_RCPARAMS = {
    "axes.axisbelow": True,
    "axes.titlesize": "medium",
    "axes.edgecolor": "white",
    "axes.labelcolor": MEDIUM_GREY,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "grid.linestyle": "--",
    "grid.linewidth": 1.0,
    "grid.color": LIGHT_GREY,
    "xtick.major.size": 0,
    "xtick.minor.size": 0,
    "xtick.color": MEDIUM_GREY,
    "ytick.major.size": 0,
    "ytick.minor.size": 0,
    "ytick.color": MEDIUM_GREY,
    "lines.color": DARK_BLUE,
    "lines.markerfacecolor": DARK_BLUE,
    "patch.facecolor": DARK_BLUE,
    "axes.prop_cycle": cycler("color", [DARK_BLUE + "ee", DARK_RED + "ee"]),
    "legend.edgecolor": LIGHT_GREY,
    "figure.max_open_warning": 150,
    "figure.dpi": 300,
}

ind = [0, 1, 2]
with mpl.rc_context(MPL_RCPARAMS):
    fig = plt.figure(figsize=(6, 3))
    plt.bar(ind, [5, 10, 7])
    plt.grid(axis='y')
    plt.ylabel('Scores')
    plt.title('Scores by group and gender', color=MEDIUM_GREY)
    plt.xticks(ind, ('Children', 'Adults', 'Elderly'))
    fig.savefig('plot_1.png')

    fig = plt.figure(figsize=(6, 3))
    plt.bar([i - 0.2 for i in ind], [5, 10, 7], .4, label='Men')
    plt.bar([i + 0.2 for i in ind], [3, 7, 7.5], .4, label='Women')
    plt.grid(axis='y')
    plt.ylabel('Scores')
    plt.title('Scores by group and gender', color=MEDIUM_GREY)
    plt.xticks(ind, ('Children', 'Adults', 'Elderly'))
    plt.legend(loc="upper right", frameon=True)
    fig.savefig('plot_2.png')

    plt.show()