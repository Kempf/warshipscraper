import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# load
t = pd.read_csv('titles_sorted.csv',index_col=0)
# count countries
cstat = t.country.value_counts(dropna=False)

# group smaller countries into "other"
def other_countries(country):
    if isinstance(country, str):
        perc = cstat[country] / cstat.sum()
        #print(perc)
        # change this to output more or less countries
        if perc < 0.05:
            return "other"
        else:
            return country
    else:
        return country

# apply other country func
t.country = t.country.apply(other_countries)
# recount
cstat2 = t.country.value_counts()#dropna=False)
# output
print(cstat)
pie=cstat2.plot.pie(autopct='%1.1f%%',pctdistance=1.1, labeldistance=1.2,title='Submissions by country',)
plt.ylabel('')



# scores

ts=pd.DataFrame(t.loc[:,['country','score']].dropna())
#plt.figure()
box=ts.boxplot(by='country',showfliers=False)
plt.xlabel('')
plt.title('Score by country')
plt.suptitle('')


# upvote ratio

tu=pd.DataFrame(t.loc[:,['country','upvote_ratio']].dropna())
#plt.figure()
box2=tu.boxplot(by='country',showfliers=False)
plt.xlabel('')
plt.title('Upvote ratio by country')
plt.suptitle('')

# comments

tc=pd.DataFrame(t.loc[:,['country','comms']].dropna())
#plt.figure()
box2=tc.boxplot(by='country',showfliers=False)
plt.xlabel('')
plt.title('Number of comments by country')
plt.suptitle('')

# date
plt.figure()
t.created_utc = (t.created_utc.apply(dt.datetime.utcfromtimestamp)-pd.offsets.MonthBegin(1)).dt.floor('D')
t.groupby(t.created_utc).id.count().plot(kind='line')
plt.title('Posts per month')


# country-date
tc=pd.DataFrame(t.loc[:,['country','created_utc']])
tc.groupby(t.country).created_utc.value_counts().unstack().transpose().plot(kind='line')
plt.title('Posts by country per month')
plt.show()