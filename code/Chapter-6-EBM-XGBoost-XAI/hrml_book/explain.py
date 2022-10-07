import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Callable


def plot_partial_dep_ice(feature: str,
                         X: pd.DataFrame,
                         y: pd.Series,
                         predict: Callable):
    """
    Generate side-by-side PD/ICE plots with histogram of feature values.
    :param feature: The feature to explain.
    :param X: A dataset to generate predictions on.
    :param y: The true label.
    :param predict: A callable that generates model predictions as a numpy ndarray or Pandas Series. For example:
            predict = lambda x: my_xgb_model.predict(xgb.DMatrix(x[features], label=x[label]))
    """

    X[y.name] = y
    
    pd_ice_data = pd_ice_new(feature, X, predict)
    preds = predict(X)
        
    # create a copy of frame and sort it by yhat
    sort_df = X.copy(deep=True)
    sort_df['prediction'] = preds
    sort_df.sort_values('prediction', inplace=True)
    
    # sort_df.reset_index(inplace=True)
    # Use the native pandas index rather than the id column
    
    # find top and bottom percentiles
    percentiles_dict = {0: sort_df.index[0], 99: sort_df.index[-1]}

    # find 10th-90th percentiles
    inc = sort_df.shape[0] // 10
    for i in range(1, 10):
        percentiles_dict[i * 10] = sort_df.index[i * inc]
        
    # collect bins used in partial dependence
    bins = list(pd_ice_data[feature])
    
    # calculate ICE at percentiles using partial dependence bins for each feature
    for pctile in sorted(percentiles_dict.keys()):
        col_name = 'Percentile_' + str(pctile)
        pd_ice_data[col_name] = pd_ice_new(feature,
                                           X.loc[[int(percentiles_dict[pctile])]], 
                                           predict,
                                           bins=bins)['partial_dependence']
        
    return hist_mean_pd_ice_plot(feature, str(y.name), X, {feature: pd_ice_data})


def pd_ice_new(feature: str,
               data: pd.DataFrame,
               predict: Callable,
               resolution=20,
               bins=None):

    # turn off pesky Pandas copy warning
    pd.options.mode.chained_assignment = None

    if bins is None:
        # TODO: do this automatically with some external package
        min_ = data[feature].min()
        max_ = data[feature].max()
        by = (max_ - min_) / resolution
        # modify max and by
        # to preserve resolution and actually search up to max
        bins = np.arange(min_, (max_ + by), (by + np.round((1. / resolution) * by, 3)))

    # cache original column values
    col_cache = data.loc[:, feature].copy(deep=True)

    # calculate partial dependence by setting column of interest to constant
    # and scoring the altered data and taking the mean of the predictions
    temp_df = data.copy(deep=True)
    temp_df.loc[:, feature] = bins[0]
    for j, _ in enumerate(bins):
        data.loc[:, feature] = bins[j]
        temp_df = temp_df.append(data, ignore_index=True)

    # return input frame to original cached state
    data.loc[:, feature] = col_cache
    temp_df['partial_dependence'] = predict(temp_df)

    return pd.DataFrame(temp_df[[feature, 'partial_dependence']].groupby([feature]).mean()).reset_index()


def hist_mean_pd_ice_plot(feature: str,
                          target: str,
                          data: pd.DataFrame, pd_ice_dict):

    """ Plots diagnostic plot of histogram with mean line overlay
        side-by-side with partial dependence and ICE.
    :param feature: Name of variable for which to plot ICE and partial dependence.
    :param target: Name of target variable.
    :param data: Dataset used to calculate PD/ICE values.
    :param pd_ice_dict: Dict of Pandas DataFrames containing partial dependence
                        and ICE values.
    """

    # initialize figure and axis
    fig, (ax, ax2) = plt.subplots(ncols=2)  # , sharey=False)
    plt.tight_layout()
    plt.subplots_adjust(left=0, right=1.8, wspace=0.18)

    # if variable is *not* high cardinality
    # create histogram directly
    if data[feature].nunique() <= 20:
        mean_df = data[[feature, target]].groupby(by=feature).mean()
        freq, bins, _ = ax.hist(data[feature], color='k')

    # if variable is high cardinality
    # bin, then create hist
    else:
        temp_df = pd.concat([pd.cut(data[feature], pd_ice_dict[feature][feature] - 1, duplicates='drop'),
                             data[target]], axis=1)
        mean_df = temp_df.groupby(by=feature).mean()
        del temp_df
        freq, bins, _ = ax.hist(data[feature], bins=pd_ice_dict[feature][feature] - 1, color='k')
        bins = bins[:-1]

    # annotate hist
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram with Mean ' + target + ' Overlay')

    # create a new twin axis
    # on which to plot a line showing mean value
    # across hist bins
    ax1 = ax.twinx()
    _ = ax1.set_ylim((0, 1))
    _ = ax1.plot(bins, mean_df.reindex(labels=bins)[target], color='r')
    _ = ax1.set_ylabel('Mean ' + target)
    _ = ax1.legend(['Mean ' + target], loc=1)

    # plot PD and ICE
    plot_pd_ice(feature,
                pd_ice_dict[feature],
                ax2)
    _ = ax2.legend(bbox_to_anchor=(1.05, 0),
                   loc=3,
                   borderaxespad=0.)
    return fig


def plot_pd_ice(feature: str,
                par_dep_frame: pd.DataFrame,
                ax=None):

    """ Plots ICE overlayed onto partial dependence for a single variable.
    Conditionally uses user-defined axes, ticks, and labels for grouped subplots.
    :param feature: Name of variable for which to plot ICE and partial dependence.
    :param par_dep_frame: Name of Pandas frame containing ICE and partial
                          dependence values (tightly coupled to frame schema).
    :param ax: Matplotlib axis object to use.
    """

    if ax is None:
        fig, ax = plt.subplots() 

    # plot ICE
    par_dep_frame.drop('partial_dependence', axis=1).plot(x=feature,
                                                          colormap='gnuplot',
                                                          ax=ax)
    # overlay partial dependence, annotate plot
    par_dep_frame.plot(title='Partial Dependence with ICE: ' + feature,
                       x=feature,
                       y='partial_dependence',
                       color='red',
                       linewidth=3,
                       ax=ax)

    return
