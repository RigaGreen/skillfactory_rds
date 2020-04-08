
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import re
from datetime import datetime


# In[4]:


wd = pd.read_csv('/Users/reginakhabirova/Downloads/data.csv')


# In[10]:


display(wd.info())


# #### 1. У какого фильма из списка самый большой бюджет?

# In[362]:


wd[wd['budget'] == wd['budget'].max()]['original_title']


# #### 2.Какой из фильмов самый длительный (в минутах)?

# In[363]:


wd[wd['runtime'] == wd['runtime'].max()]['original_title']


# #### 3. Какой из фильмов самый короткий (в минутах)?

# In[19]:


wd[wd['runtime'] == wd['runtime'].min()]


# #### 4. Какое число ближе к средней длительности фильма в датасете?

# In[214]:


wd['runtime'].mean()


# #### 5. Какое число ближе к медианной длительности фильма в датасете?

# In[23]:


wd['runtime'].median()


# #### 6. Какой самый прибыльный фильм?

# In[7]:


wd['profit'] = wd['revenue'] - wd['budget']
wd[wd['profit'] == wd['profit'].max()]


# #### 7. Какой фильм самый убыточный?

# In[97]:


wd['profit'] = wd['revenue'] - wd['budget']
wd[wd['profit'] == wd['profit'].min()]


# #### 8. У скольких фильмов из датасета объем сборов оказался выше бюджета?

# In[216]:


a = wd[wd['revenue']>wd['budget']]
len(a)


# #### 9. Какой фильм оказался самым кассовым в 2008 году?

# In[22]:


wd_2008 = wd[wd['release_year'] == 2008]
wd_2008[wd_2008['revenue'] == wd_2008['revenue'].max()]


# #### 10. Самый убыточный фильм за период с 2012 по 2014 гг. (включительно)?

# In[221]:


wd_2014 = wd[(wd['release_year'] >= 2012) & (wd['release_year'] <= 2014)]
wd_2014[wd_2014['profit'] == wd_2014['profit'].min()]


# #### 11. Какого жанра фильмов больше всего?

# In[191]:


genres_all = wd['genres'].str.split('|')

a = []
for i in range(len(genres_all)):
    for j in range(len(genres_all[i])):
        a.append(genres_all[i][j])
        
res = Counter(a).most_common(1)
res        


# #### 12. Какого жанра среди прибыльных фильмов больше всего?

# In[225]:


gg = wd[wd['profit']>0]['genres'].str.split('|')

a = []
for i in range(len(gg)):
    for j in range(len(gg.iloc[i])):
        a.append(gg.iloc[i][j])
        
res = Counter(a).most_common(1)
res        


# #### 13. Кто из режиссеров снял больше всего фильмов?

# In[8]:


from collections import Counter

director = wd['director'].str.split('|')
a = []
for i in range(len(director)):
    for j in range(len(director[i])):
        a.append(director[i][j])
        
res = Counter(a).most_common(1)
res 


# #### 14. Кто из режиссеров снял больше всего прибыльных фильмов?

# In[9]:


pd = wd[wd['profit']>0]['director'].str.split('|')

x = []
for i in range(len(pd)):
    for j in range(len(pd.iloc[i])):
        x.append(pd.iloc[i][j]) 
        
x_res = Counter(x).most_common(1)
x_res        


# #### 15. Кто из режиссеров принес больше всего прибыли?

# In[10]:


grouped_wd = wd.groupby(['director'])['profit'].sum().sort_values(ascending=False)
grouped_wd.head(1)


# #### 16. Какой актер принес больше всего прибыли?

# In[11]:


from collections import Counter

actors = Counter()

for i, x in enumerate(wd['cast'].str.split('|')):
    for actor in x:
        actors[actor] += wd.loc[i]['revenue']


# In[17]:


actors.most_common(1)


# #### 17. Какой актер принес меньше всего прибыли в 2012 году?

# In[49]:


wd_2012 = wd[wd['release_year'] == 2012]

actors_2012 = Counter()

for i, x in enumerate(wd_2012['cast'].str.split('|')):
    for actor in x:
        actors_2012[actor] += wd_2012.iloc[i]['revenue']

list(reversed(actors_2012.most_common()))         


# In[54]:


actors_2012 = Counter()


# #### 18. Какой актер снялся в большем количестве высокобюджетных фильмов? Примечание: в фильмах, где бюджет выше среднего по данной выборке.

# In[58]:


wd_high_budget = wd[wd['budget'] > wd['budget'].mean()]


# In[78]:


actors_high_budget = Counter()

for i, x in enumerate(wd_high_budget['cast'].str.split('|')):
    for actor in x:
        actors_high_budget[actor] += 1
        
actors_high_budget.most_common(1)      


# #### 19. В фильмах какого жанра больше всего снимался Nicolas Cage?

# In[79]:


gg = wd[wd['cast'].str.contains('Nicolas Cage')]['genres'].str.split('|')

a = []
for i in range(len(gg)):
    for j in range(len(gg.iloc[i])):
        a.append(gg.iloc[i][j])
        
res = Counter(a).most_common(1)
res  


# #### 20. Какая студия сняла больше всего фильмов?

# In[67]:


pc = wd['production_companies'].str.split('|')

a = []
for i in range(len(pc)):
    for j in range(len(pc[i])):
        a.append(pc[i][j])
        
res = Counter(a).most_common(1)
res  


# In[68]:


pc.head()


# #### 21. Какая студия сняла больше всего фильмов в 2015 году?

# In[263]:


pc_2015 = wd[wd['release_year'] >= 2015]['production_companies'].str.split('|')


# In[264]:


a = []
for i in range(len(pc_2015)):
    for j in range(len(pc_2015.iloc[i])):
        a.append(pc_2015.iloc[i][j])
        
res = Counter(a).most_common(1)
res  


# #### 22. Какая студия заработала больше всего денег в жанре комедий за все время?

# In[81]:


pc_com = wd[wd['genres'].str.contains('Comedy')]


# In[101]:


production_companies = Counter()

for i, c in enumerate(pc_com['production_companies'].str.split('|')):
    for company in c:
        production_companies[company] += pc_com.iloc[i]['revenue']

production_companies.most_common(1)        


# #### 23. Какая студия заработала больше всего денег в 2012 году?

# In[83]:


wd_2012 = wd[wd['release_year'] == 2012]


# In[103]:


production_companies_2012 = Counter()

for i, c in enumerate(wd_2012['production_companies'].str.split('|')):
    for company in c:
        production_companies_2012[company] += wd_2012.iloc[i]['revenue']

production_companies_2012.most_common(1)   


# #### 24. Самый убыточный фильм от Paramount Pictures?

# In[429]:


grouped_wd = wd[wd['production_companies'].str.contains('Paramount Pictures')].groupby(['original_title'])['profit'].sum().sort_values(ascending=True)
grouped_wd.head(1)


# #### 25. Какой самый прибыльный год (в какой год студии заработали больше всего)?

# In[433]:


grouped_wd = wd.groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
grouped_wd.head(5)


# #### 26. Какой самый прибыльный год для студии Warner Bros?

# In[434]:


grouped_wd = wd[wd['production_companies'].str.contains('Warner Bros')].groupby(['release_year'])['profit'].sum().sort_values(ascending=False)
grouped_wd.head(5)


# #### 27. В каком месяце за все годы суммарно вышло больше всего фильмов?

# In[167]:


release_date = wd['release_date'].iloc[0:]

months = []
for i in release_date:
    months.append(datetime.strptime(i, '%m/%d/%Y').month)


# In[165]:


res = Counter(months).most_common(1)
res


# #### 28. Сколько суммарно вышло фильмов летом (за июнь, июль, август)?

# In[283]:


months_summer = []
for i in release_date:
    month = datetime.strptime(i, '%m/%d/%Y').month
    if month in (6,7,8):
        months_summer.append(month)


# In[178]:


len(months_summer)


# #### 29. Какой режиссер выпускает (суммарно по годам) больше всего фильмов зимой?

# In[9]:


wd['month'] = [datetime.strptime(i, '%m/%d/%Y').month for i in wd['release_date']]


# In[200]:


wd_winter = wd[(wd['month'] == 1 )|(wd['month'] == 2)|(wd['month'] == 12)]


# In[202]:


res = Counter(wd_winter['director']).most_common(1)
res


# #### 30. Какой месяц чаще всего самый прибыльный в году?

# In[136]:


wd['ym_revenue'] = wd.groupby(['month', 'release_year'])['revenue'].transform(np.sum) 
wd['ym_revenue_rnk'] = wd.groupby(['release_year'])['ym_revenue'].rank(method='dense', ascending=False)

wd[['month', 'release_year','ym_revenue_rnk']].drop_duplicates().loc[wd['ym_revenue_rnk'] == 1]     .groupby(['month']).size().sort_values(ascending=False)


# #### 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?

# In[78]:


wd['length_title'] = [len(x) for x in wd['original_title']]
from collections import Counter
tl = Counter()
for i, x in enumerate(wd['production_companies'].str.split('|')):
    for a in x:
        tl[a] += wd.loc[i]['length_title']  
        
length_title = pd.DataFrame.from_dict(tl, orient = 'index').reset_index()
length_title = length_title.rename(columns={'index':'company', 0:'length_title'})
length_title.head()        


# In[71]:


n = Counter()
for i, x in enumerate(wd['production_companies'].str.split('|')):
    for a in x:
        n[a] += 1
        
numb = pd.DataFrame.from_dict(n, orient = 'index').reset_index()
numb = numb.rename(columns={'index':'company', 0:'numb'})
numb.head()        


# In[174]:


joined = length_title.merge(numb, on='company', how='left')
joined['avg_lenght']  = joined['length_title'] / joined['numb']
joined.sort_values(by = 'avg_lenght', ascending = False).head(1)


# #### 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?

# In[ ]:


wd['count_words_title'] = wd['original_title'].str.split().str.len()


# In[182]:


from collections import Counter
cw = Counter()
for i, x in enumerate(wd['production_companies'].str.split('|')):
    for a in x:
        cw[a] += wd.loc[i]['count_words_title']  
        
count_words_title = pd.DataFrame.from_dict(cw, orient = 'index').reset_index()
count_words_title = count_words_title.rename(columns={'index':'company', 0:'count_words_title'})


# In[183]:


# numb from question 31
joined = count_words_title.merge(numb, on='company', how='left')
joined['avg_count_words']  = joined['count_words_title'] / joined['numb']
joined.sort_values(by = 'avg_count_words', ascending = False).head(1)


# #### 33. Сколько разных слов используется в названиях фильмов (без учета регистра)?

# In[253]:


wd['original_title_clean'] = wd['original_title'].str.replace('[#:!?-]', '') 
words_all = wd['original_title_clean'].str.split(' ')


# In[254]:


a = []
for i in range(len(words_all)):
    for j in range(len(words_all[i])):
        a.append(words_all[i][j])
        
unique_list = [] 

for i in a:
    if i not in unique_list:
        unique_list.append(i)
        
len(unique_list)         


# #### 34. Какие фильмы входят в 1 % лучших по рейтингу?       

# In[265]:


best_movies = wd['original_title'][wd['vote_average'] >= wd['vote_average'].quantile(.99)]


# In[277]:


q1 = 0
q2 = 0
q3 = 0
q4 = 0
q5 = 0

for i in best_movies:
    if i in ('Inside Out', 'Gone Girl', '12 Years a Slave'):
       q1+=1

for i in best_movies:
    if i in ('BloodRayne', 'The Adventures of Rocky and Bullwinkle'):
       q2+=1

for i in best_movies:
    if i in ('The Lord of the Rings: The Return of the King', 'Upside Down'):
       q3+=1   
    
for i in best_movies:
    if i in ('300', 'Lucky Number Slevin'):
       q4+=1  

for i in best_movies:
    if i in ('Upside Down', '300', 'Inside Out', 'The Lord of the Rings: The Return of the King'):
       q5+=1 


# In[278]:


print(q1, q2, q3, q4, q5)


# #### 35. Какие актеры чаще всего снимаются в одном фильме вместе?

# In[279]:


from collections import defaultdict

actors_couple = defaultdict(list)

for i, row in data.iterrows():
    imdb_id = row['imdb_id']
    for actor in row['cast'].split('|'):
        actorsDict['imdb_id'].append(imdb_id)
        actorsDict['actor'].append(actor)
        
actorsDF = pd.DataFrame(actorsDict)
am = actorsDF.merge(data,how='inner',on = 'imdb_id')


# In[316]:


from collections import defaultdict
actors = defaultdict(list)

for i, row in wd.iterrows():
    imdb_id = row['imdb_id']
    for actor in row['cast'].split('|'):
        actors['imdb_id'].append(imdb_id)
        actors['actor'].append(actor)


# In[317]:


actors = pd.DataFrame(actorsDict)
actors_couple = actorsDF.merge(actorsDF,how='inner',on = 'imdb_id')
actors_couple = actors_couple[actors_couple['actor_x'] != actors_couple['actor_y']]


# In[318]:


actors_couple.groupby(['actor_x', 'actor_y'])['imdb_id'].count().sort_values(ascending=False).head(10)


# #### 36. У какого из режиссеров самый высокий процент фильмов со сборами выше бюджета?

# In[329]:


directors = Counter()

for i, x in enumerate(wd['director'].str.split('|')):
    for director in x:
        directors[director] += 1


# In[334]:


wd_exp = wd[wd['revenue'] > wd['budget']] 

directors_exp = Counter()

for i, x in enumerate(wd_exp['director'].str.split('|')):
    for director in x:
        directors_exp[director] += 1



# In[335]:


directors_df = pd.DataFrame.from_dict(directors, orient = 'index').reset_index()
directors_df = directors_df.rename(columns={'index':'director', 0:'movies_cnt'})
directors_df.head() 


# In[337]:


directors_exp_df = pd.DataFrame.from_dict(directors_exp, orient = 'index').reset_index()
directors_exp_df = directors_exp_df.rename(columns={'index':'director', 0:'movies_exp_cnt'})
directors_exp_df.head() 


# In[341]:


joined = directors_df.merge(directors_exp_df, on='director', how='left')
joined['share']  = joined['movies_exp_cnt'] / joined['movies_cnt']
#joined.sort_values(by = 'share', ascending = False).head(1)


# In[344]:


z = joined[joined['share'] >= 1]


# In[346]:


z[z['movies_cnt'] == z['movies_cnt'].max()]


# In[359]:


z[(z['director'] == 'Quentin Tarantino' ) | (z['director'] == 'Steven Soderbergh') |   (z['director'] == 'Robert Rodriguez' )  | (z['director'] == 'Christopher Nolan' ) |   (z['director'] == 'Clint Eastwood' ) ]

