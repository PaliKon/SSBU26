from data_handling import Dataset

if __name__ == "__main__":
    dataset = Dataset()
    #uloha 1
    stats = dataset.calculate_statistics()
    print(stats)
    #uloha 3 a 4
    print("\nAll features")
    summary = dataset.summarize_features()
    print(summary.to_string())

    print("\nselected features")
    selected_features = ['mean radius', 'mean texture', 'mean area']
    summary = dataset.summarize_features(selected_features)
    print(summary.to_string())


    # plot class distribution
    dataset.plot_class_distribution()

    # plot correlation matrix
    dataset.plot_correlation_matrix()

    # plot feature importance
    dataset.feature_importance()

    # plot feature distributions
    dataset.plot_feature_distributions()

    # plot box plots
    dataset.plot_box_plots()

    # plot pair plot for the first 5 features
    selected_features = dataset.feature_names[:5]
    dataset.plot_pair_plot(selected_features)