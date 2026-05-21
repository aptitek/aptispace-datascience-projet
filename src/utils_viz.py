import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def set_custom_style(theme="light"):
    if theme == "light":
        sns.set_theme(style="whitegrid")
    else:
        plt.style.use("dark_background")

def plot_generic_trends(df, x_col, y_col, group_col=None):
    fig, ax = plt.subplots(figsize=(12, 5))
    if group_col and group_col in df.columns:
        for group in df[group_col].unique()[:5]:
            subset = df[df[group_col] == group]
            ax.plot(subset[x_col] if x_col in df.columns else subset.index,
                   subset[y_col], label=str(group), alpha=0.7)
        ax.legend()
    else:
        ax.plot(df[x_col] if x_col in df.columns else df.index,
               df[y_col], alpha=0.7)
    ax.set_xlabel(str(x_col))
    ax.set_ylabel(y_col)
    plt.tight_layout()
    return fig

def plot_correlation_matrix(df, cols):
    fig, ax = plt.subplots(figsize=(10, 8))
    num_df = df[cols].select_dtypes(include=[np.number])
    corr = num_df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
                ax=ax, linewidths=0.5)
    plt.tight_layout()
    return fig

def plot_bivariate_scatter(df, x_col, y_col, color_col=None):
    fig, ax = plt.subplots(figsize=(10, 6))
    if color_col and color_col in df.columns:
        scatter = ax.scatter(df[x_col], df[y_col],
                           c=df[color_col], cmap="viridis", alpha=0.5)
        plt.colorbar(scatter, ax=ax, label=color_col)
    else:
        ax.scatter(df[x_col], df[y_col], alpha=0.5)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    plt.tight_layout()
    return fig