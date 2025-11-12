# Import relevant libraries
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional
from matplotlib.axes import Axes

# Set Color dictionaries
COLORS = {
    "monetary":  "#2563EB",
    "frequency": "#10B981",
    "recency":   "#EF4444",
    "uk":        "#1F77B4",
    "intl":      "#FF7F0E",
    "text":      "#222222",
    "axis":      "#444444",
    "grid":      "#999999",
}

# Set figure/axes parameters
def setup() -> None:
    plt.rcParams.update({
        "figure.dpi": 110,
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Liberation Sans", "Nimbus Sans L", "sans-serif"],
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "text.color": COLORS["text"],
        "axes.labelcolor": COLORS["text"],
        "xtick.color": COLORS["text"],
        "ytick.color": COLORS["text"],
        "axes.edgecolor": COLORS["axis"],
        "axes.grid": True,
        "grid.color": COLORS["grid"],
        "grid.linestyle": "--",
        "grid.alpha": 0.25,
        "legend.frameon": False,
    })
    sns.set_theme(context="notebook", style="whitegrid")

def style_ax(
    ax: Axes,
    *,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    legend_loc: str = "best",
) -> Axes:
    if title is not None:
        ax.set_title(title, pad=10, color=COLORS["text"])
    if xlabel is not None:
        ax.set_xlabel(xlabel, labelpad=6, color=COLORS["text"])
    if ylabel is not None:
        ax.set_ylabel(ylabel, labelpad=6, color=COLORS["text"])

    for spine in ax.spines.values():
        spine.set_color(COLORS["axis"])
        spine.set_alpha(0.6)

    _, labels = ax.get_legend_handles_labels()
    if len(labels) > 0:
        ax.legend(loc=legend_loc)

    return ax