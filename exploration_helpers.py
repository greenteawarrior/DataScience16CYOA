# TODO: clean_data function to run on both the training set and test set
def clean_data():
    return

# TODO: feature_engineering function to run on both the training set and test set
def feature_eng():
    return

def cp(featurestr, rotatelabels=True):
    # helper function for countplot with rotation=90 on the x axis labels
    # note that these are with non-normalized values
    fig = sns.countplot(x=featurestr, data=sfcrime)
    if rotatelabels:
        _ = plt.ticks(rotation=90)
    return

# TODO: helper function for countplot with relative frequencies
def relative_cp(cat_subset):

    grouped = sfcrime.groupby(['Category'], sort=False)

    weekday_counts = grouped['DayOfWeek'].value_counts(normalize=True, sort=False)

    weekday_data = [
        {'category': category, 'DayOfWeek': DayOfWeek, 'percentage': percentage*100} 
        for (category, DayOfWeek), percentage in dict(weekday_counts).items() if category in cat_subset
    ]

    df_weekday = pandas.DataFrame(weekday_data)
    weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    p = plt.figure(figsize=(10,7))
    p = sns.barplot(x='category', y='percentage', hue='DayOfWeek', data=df_weekday, hue_order=weekday_order)
    _ = plt.setp(p.get_xticklabels(), rotation=90) 
    _ = plt.legend(bbox_to_anchor=(1.05, 1), loc=2)

    return

# example
# cat_subset = ["ASSAULT", "BURGLARY", "MISSING PERSON", "ROBBERY"]v