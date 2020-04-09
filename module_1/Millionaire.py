#!/usr/bin/env python
# coding: utf-8

# In[538]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from collections import Counter
print(os.listdir())


# In[539]:


data = pd.read_csv('data.csv')
data.head(5)


# In[540]:


len(data)
data.info()


# # Предобработка датасета

# In[541]:


answer_ls = [] # создадим список с ответами. сюда будем добавлять ответы по мере прохождения теста
# сюда можем вписать создание новых колонок в датасете


# # 1. У какого фильма из списка самый большой бюджет?
# Варианты ответов:
# 1. The Dark Knight Rises (tt1345836)
# 2. Spider-Man 3 (tt0413300)
# 3. Avengers: Age of Ultron (tt2395427)
# 4. The Warrior's Way	(tt1032751)
# 5. Pirates of the Caribbean: On Stranger Tides (tt1298650)

# In[542]:


max_budget_list=('tt1345836','tt0413300','tt2395427','tt1032751','tt1298650')
max_budget=data[data.imdb_id.isin(max_budget_list)].budget.max()
data[data.budget==max_budget_movie].original_title


# In[543]:


# тут вводим ваш ответ и добавлем в его список ответов (сейчас для примера стоит "1")
answer_ls.append(4)


# # 2. Какой из фильмов самый длительный (в минутах)
# 1. The Lord of the Rings: The Return of the King	(tt0167260)
# 2. Gods and Generals	(tt0279111)
# 3. King Kong	(tt0360717)
# 4. Pearl Harbor	(tt0213149)
# 5. Alexander	(tt0346491)

# In[544]:


longest_movie_list = ('tt0167260','tt0279111','tt0360717','tt0213149','tt0346491')
longest_movie=data[data.imdb_id.isin(longest_movie_list)].runtime.max()
data[data.runtime==longest_movie]


# In[545]:


answer_ls.append(2)


# # 3. Какой из фильмов самый короткий (в минутах)
# Варианты ответов:
# 
# 1. Home on the Range	tt0299172
# 2. The Jungle Book 2	tt0283426
# 3. Winnie the Pooh	tt1449283
# 4. Corpse Bride	tt0121164
# 5. Hoodwinked!	tt0443536

# In[546]:


shortest_movie_list = ('tt0299172','tt0283426','tt1449283','tt0121164','tt0443536')
shortest_movie=data[data.imdb_id.isin(shortest_movie_list)].runtime.min()
data[data.runtime==shortest_movie]


# In[547]:


answer_ls.append(3)


# # 4. Средняя длительность фильма?
# 
# Варианты ответов:
# 1. 115
# 2. 110
# 3. 105
# 4. 120
# 5. 100
# 

# In[548]:


round(data.runtime.mean(),2)


# In[549]:


answer_ls.append(2)


# # 5. Средняя длительность фильма по медиане?
# Варианты ответов:
# 1. 106
# 2. 112
# 3. 101
# 4. 120
# 5. 115
# 
# 
# 

# In[550]:


round(data.runtime.median(),2)


# In[551]:


answer_ls.append(1)


# # 6. Какой самый прибыльный фильм?
# Варианты ответов:
# 1. The Avengers	tt0848228
# 2. Minions	tt2293640
# 3. Star Wars: The Force Awakens	tt2488496
# 4. Furious 7	tt2820852
# 5. Avatar	tt0499549

# In[552]:


data['income']=data['revenue']-data['budget']
data[data.income==data.income.max()]


# In[553]:


answer_ls.append(5)


# # 7. Какой фильм самый убыточный?
# Варианты ответов:
# 1. Supernova tt0134983
# 2. The Warrior's Way tt1032751
# 3. Flushed Away	tt0424095
# 4. The Adventures of Pluto Nash	tt0180052
# 5. The Lone Ranger	tt1210819

# In[554]:


data[data.income==data.income.min()]


# In[555]:


answer_ls.append(2)


# # 8. Сколько всего фильмов в прибыли?
# Варианты ответов:
# 1. 1478
# 2. 1520
# 3. 1241
# 4. 1135
# 5. 1398
# 

# In[556]:


data[data.income>0].imdb_id.count()


# In[557]:


answer_ls.append(1)


# # 9. Самый прибыльный фильм в 2008 году?
# Варианты ответов:
# 1. Madagascar: Escape 2 Africa	tt0479952
# 2. Iron Man	tt0371746
# 3. Kung Fu Panda	tt0441773
# 4. The Dark Knight	tt0468569
# 5. Mamma Mia!	tt0795421

# In[558]:


#income2018list = ('tt0479952','tt0371746','tt0441773','tt0468569','tt0795421')
data[data.income==data[data.release_year==2008].income.max()]


# In[559]:


answer_ls.append(4)


# # 10. Самый убыточный фильм за период с 2012 по 2014 (включительно)?
# Варианты ответов:
# 1. Winter's Tale	tt1837709
# 2. Stolen	tt1656186
# 3. Broken City	tt1235522
# 4. Upside Down	tt1374992
# 5. The Lone Ranger	tt1210819
# 

# In[560]:


data[data.income==data[data.release_year.isin(['2012','2013','2014'])].income.min()]


# In[561]:


answer_ls.append(5)


# # 11. Какого жанра фильмов больше всего?
# Варианты ответов:
# 1. Action
# 2. Adventure
# 3. Drama
# 4. Comedy
# 5. Thriller

# In[562]:


genres_count={'Action':0,'Adventure':0,'Drama':0,'Comedy':0,'Thriller':0}
for genre,count in genres_count.items():
    genres_count[genre]=data[data.genres.str.contains(genre)].imdb_id.count()  
max(genres_count, key=genres_count.get)


# In[563]:


answer_ls.append(3)


# # 12. Какого жанра среди прибыльных фильмов больше всего?
# Варианты ответов:
# 1. Drama
# 2. Comedy
# 3. Action
# 4. Thriller
# 5. Adventure

# In[564]:


genres_count_income={'Drama':0,'Comedy':0,'Action':0,'Thriller':0,'Adventure':0}
for genre,count in genres_count.items():
    genres_count_income[genre]=data[(data.genres.str.contains(genre))&(data.income>0)].imdb_id.count() 
genres_count_income
max(genres_count_income, key=genres_count_income.get)


# In[565]:


answer_ls.append(1)


# # 13. Кто из режиссеров снял больше всего фильмов?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Ridley Scott 
# 3. Steven Soderbergh
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[566]:


directors_count={'Steven Spielberg':0,'Ridley Scott':0,'Steven Soderbergh':0,'Christopher Nolan':0,'Clint Eastwood':0}
for director,count in directors_count.items():
    directors_count[director]=data[data.director.str.contains(director)].imdb_id.count()
max(directors_count, key=directors_count.get)


# In[567]:


answer_ls.append(3)


# # 14. Кто из режиссеров снял больше всего Прибыльных фильмов?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Clint Eastwood
# 3. Steven Spielberg
# 4. Ridley Scott
# 5. Christopher Nolan

# In[568]:


directors_count={'Steven Spielberg':0,'Ridley Scott':0,'Steven Soderbergh':0,'Christopher Nolan':0,'Clint Eastwood':0}
for director,count in directors_count.items():
    directors_count[director]=data[(data.director.str.contains(director))&(data.income>0)].imdb_id.count()
max(directors_count, key=directors_count.get)


# In[569]:


answer_ls.append(4)


# # 15. Кто из режиссеров принес больше всего прибыли?
# Варианты ответов:
# 1. Steven Spielberg
# 2. Christopher Nolan
# 3. David Yates
# 4. James Cameron
# 5. Peter Jackson
# 

# In[570]:


directors_income={'Steven Spielberg':0,'David Yates':0,'Peter Jackson':0,'Christopher Nolan':0,'James Cameron':0}
for director,count in directors_count.items():
    directors_income[director]=data[data.director.str.contains(director)].income.sum()
max(directors_income, key=directors_income.get)
#directors_income


# In[571]:


answer_ls.append(5)


# # 16. Какой актер принес больше всего прибыли?
# Варианты ответов:
# 1. Emma Watson
# 2. Johnny Depp
# 3. Michelle Rodriguez
# 4. Orlando Bloom
# 5. Rupert Grint

# In[572]:


actor_income={'Emma Watson':0,'Johnny Depp':0,'Michelle Rodriguez':0,'Orlando Bloom':0,'Rupert Grint':0}
for actor,income in actor_income.items():
    actor_income[actor]=data[data.cast.str.contains(actor)].income.sum()
max(actor_income, key=actor_income.get)
#actor_income


# In[573]:


answer_ls.append(1)


# # 17. Какой актер принес меньше всего прибыли в 2012 году?
# Варианты ответов:
# 1. Nicolas Cage
# 2. Danny Huston
# 3. Kirsten Dunst
# 4. Jim Sturgess
# 5. Sami Gayle

# In[574]:


actor_income={'Nicolas Cage':0,'Danny Huston':0,'Kirsten Dunst':0,'Jim Sturgess':0,'Sami Gayle':0}
for actor,income in actor_income.items():
    actor_income[actor]=data[(data.cast.str.contains(actor))&(data.release_year==2012)].income.sum()
min(actor_income, key=actor_income.get)
#actor_income


# In[575]:


answer_ls.append(3)


# # 18. Какой актер снялся в большем количестве высокобюджетных фильмов? (в фильмах где бюджет выше среднего по данной выборке)
# Варианты ответов:
# 1. Tom Cruise
# 2. Mark Wahlberg 
# 3. Matt Damon
# 4. Angelina Jolie
# 5. Adam Sandler

# In[576]:


actor_income={'Tom Cruise':0,'Mark Wahlberg':0,'Matt Damon':0,'Angelina Jolie':0,'Adam Sandler':0}
for actor,income in actor_income.items():
    actor_income[actor]=data[(data.cast.str.contains(actor))&(data.budget>data.budget.mean())].imdb_id.count()
print(actor_income)
print(max(actor_income, key=actor_income.get))


# In[577]:


answer_ls.append(3)


# # 19. В фильмах какого жанра больше всего снимался Nicolas Cage?  
# Варианты ответа:
# 1. Drama
# 2. Action
# 3. Thriller
# 4. Adventure
# 5. Crime

# In[578]:


genres_cage={'Drama':0,'Action':0,'Thriller':0,'Adventure':0,'Crime':0}
for genre,count in genres_cage.items():
    genres_cage[genre]=data[(data.cast.str.contains('Nicolas Cage'))&(data.genres.str.contains(genre))].imdb_id.count()
print(genres_cage)
print(max(genres_cage, key=genres_cage.get))


# In[579]:


answer_ls.append(2)


# # 20. Какая студия сняла больше всего фильмов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[580]:


studios={'Universal':0,'Paramount Pictures':0,'Columbia Pictures':0,'Warner Bros':0,'Twentieth Century Fox Film Corporation':0}
for studio,count in studios.items():
    studios[studio]=data[data.production_companies.str.contains(studio)].imdb_id.count()
print(studios)
print(max(studios, key=studios.get))


# In[581]:


answer_ls.append(1)


# # 21. Какая студия сняла больше всего фильмов в 2015 году?
# Варианты ответа:
# 1. Universal Pictures
# 2. Paramount Pictures
# 3. Columbia Pictures
# 4. Warner Bros
# 5. Twentieth Century Fox Film Corporation

# In[582]:


studios={'Universal Pictures':0,'Paramount':0,'Columbia':0,'Warner Bros':0,'Century Fox':0}
for studio,count in studios.items():
    studios[studio]=data[(data.production_companies.str.contains(studio))&(data.release_year==2015)].imdb_id.count()
print(studios)
print(max(studios, key=studios.get))


# In[583]:


answer_ls.append(4)


# # 22. Какая студия заработала больше всего денег в жанре комедий за все время?
# Варианты ответа:
# 1. Warner Bros
# 2. Universal Pictures (Universal)
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Walt Disney

# In[584]:


studios={'Universal':0,'Paramount':0,'Columbia':0,'Warner':0,'Walt Disney':0}
for studio,count in studios.items():
    studios[studio]=data[(data.production_companies.str.contains(studio))&(data.genres.str.contains('Comedy'))].income.sum()
print(studios)
print(max(studios, key=studios.get))


# In[585]:


answer_ls.append(2)


# # 23. Какая студия заработала больше всего денег в 2012 году?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Columbia Pictures
# 4. Paramount Pictures
# 5. Lucasfilm

# In[586]:


studios={'Universal Pi':0,'Paramount Pi':0,'Columbia Pi':0,'Warner Br':0,'Lucasfilm':0}
for studio,count in studios.items():
    studios[studio]=data[(data.production_companies.str.contains(studio))&(data.release_year==2012)].income.sum()
print(studios)
print(max(studios, key=studios.get))


# In[587]:


answer_ls.append(1)


# # 24. Самый убыточный фильм от Paramount Pictures
# Варианты ответа:
# 
# 1. K-19: The Widowmaker tt0267626
# 2. Next tt0435705
# 3. Twisted tt0315297
# 4. The Love Guru tt0811138
# 5. The Fighter tt0964517

# In[588]:


movies_count={'tt0267626':0,'tt0435705':0,'tt0315297':0,'tt0811138':0,'tt0964517':0}
for movie,count in movies_count.items():
    movies_count[movie]=data[(data.imdb_id==movie)].income.sum()
print(movies_count)
print(min(movies_count, key=movies_count.get))


# In[589]:


answer_ls.append(1)


# # 25. Какой Самый прибыльный год (заработали больше всего)?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2002
# 5. 2015

# In[590]:


incomeyears=data.groupby(['release_year']).income.sum()
incomeyears.idxmax(axis=1)


# In[591]:


answer_ls.append(5)


# # 26. Какой Самый прибыльный год для студии Warner Bros?
# Варианты ответа:
# 1. 2014
# 2. 2008
# 3. 2012
# 4. 2010
# 5. 2015

# In[592]:


incomeyears=data[data.production_companies.str.contains('Warner Bros')].groupby(['release_year']).income.sum()
incomeyears.idxmax(axis=1)


# In[593]:


answer_ls.append(1)


# # 27. В каком месяце за все годы суммарно вышло больше всего фильмов?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[594]:


data['release_date']=pd.to_datetime(data.release_date)
data['release_month']=data.release_date.dt.month
months_count=data.groupby(['release_month']).imdb_id.count()
months_count.idxmax(axis=1)


# In[595]:


answer_ls.append(4)


# # 28. Сколько суммарно вышло фильмов летом? (за июнь, июль, август)
# Варианты ответа:
# 1. 345
# 2. 450
# 3. 478
# 4. 523
# 5. 381

# In[596]:


months_count[5:8].sum()


# In[597]:


answer_ls.append(2)


# # 29. Какой режисер выпускает (суммарно по годам) больше всего фильмов зимой?
# Варианты ответов:
# 1. Steven Soderbergh
# 2. Christopher Nolan
# 3. Clint Eastwood
# 4. Ridley Scott
# 5. Peter Jackson

# In[598]:


directors_count={'Peter Jackson':0,'Ridley Scott':0,'Steven Soderbergh':0,'Christopher Nolan':0,'Clint Eastwood':0}
for director,count in directors_count.items():
    directors_count[director]=data[(data.director.str.contains(director))&(data.release_month.isin([12,1,2]))].imdb_id.count()
max(directors_count, key=directors_count.get)


# In[599]:


answer_ls.append(5)


# # 30. Какой месяц чаще всего по годам самый прибыльный?
# Варианты ответа:
# 1. Январь
# 2. Июнь
# 3. Декабрь
# 4. Сентябрь
# 5. Май

# In[600]:


months_income=data.groupby(['release_year','release_month']).income.sum()
months={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
months_income[year].idxmax(axis=1)
for year in range (2000,2016):
    months[months_income[year].idxmax(axis=1)]+=1
max(months, key=months.get)


# In[601]:


answer_ls.append(2)


# # 31. Названия фильмов какой студии в среднем самые длинные по количеству символов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[602]:


def q31(row):
    if 'Universal' in row['production_companies']:
        return 'Universal'
    if 'Paramount' in row['production_companies']:
        return 'Paramount'
    if 'Four By Two' in row['production_companies']:
        return 'Four By Two'
    if 'Warner' in row['production_companies']:
        return 'Warner'
    if 'Jim Henson' in row['production_companies']:
        return 'Jim Henson'
data['q31']=data.apply(q31,axis=1)
data['title_len']=data.original_title.str.len()
directors_len=data.groupby(['q31']).title_len.mean()
directors_len


# In[603]:


answer_ls.append(5)


# # 32. Названия фильмов какой студии в среднем самые длинные по количеству слов?
# Варианты ответа:
# 1. Universal Pictures (Universal)
# 2. Warner Bros
# 3. Jim Henson Company, The
# 4. Paramount Pictures
# 5. Four By Two Productions

# In[604]:


data['title_words']=data.original_title.str.count(' ')+1
directors_len=data.groupby(['q31']).title_words.mean()
directors_len


# In[605]:


answer_ls.append(5)


# # 33. Сколько разных слов используется в названиях фильмов?(без учета регистра)
# Варианты ответа:
# 1. 6540
# 2. 1002
# 3. 2461
# 4. 28304
# 5. 3432

# In[606]:


different_words=[]
for row in data.original_title:
    words=row.split()
    for word in words:
        if word.lower() in different_words: 
            continue
        else: 
            different_words.append(word.lower())
len(different_words)


# In[607]:


answer_ls.append(3)


# # 34. Какие фильмы входят в 1 процент лучших по рейтингу?
# Варианты ответа:
# 1. Inside Out, Gone Girl, 12 Years a Slave
# 2. BloodRayne, The Adventures of Rocky & Bullwinkle
# 3. The Lord of the Rings: The Return of the King
# 4. 300, Lucky Number Slevin

# In[608]:


movies_1=['Inside Out', 'Gone Girl', '12 Years a Slave']
movies_2=['The Adventures of Rocky & Bullwinkle', 'BloodRayne Girl']
movies_3=['The Lord of the Rings: The Return of the King']
movies_4=['300','Lucky Number Slevin']
count=data.imdb_id.count()
count1=int(round(0.01*count)-1)
data1=data.sort_values(by=['vote_average'], ascending=False).iloc[0:count1]
for movie in movies_1:
    display(data1[data1['original_title'].str.contains(movie)])
for movie in movies_2:
    display(data1[data1['original_title'].str.contains(movie)])
for movie in movies_3:
    display(data1[data1['original_title'].str.contains(movie)])


# In[609]:


answer_ls.append(1)


# # 35. Какие актеры чаще всего снимаются в одном фильме вместе
# Варианты ответа:
# 1. Johnny Depp & Helena Bonham Carter
# 2. Hugh Jackman & Ian McKellen
# 3. Vin Diesel & Paul Walker
# 4. Adam Sandler & Kevin James
# 5. Daniel Radcliffe & Rupert Grint

# In[610]:


actors1=['Johnny Depp','Helena Bonham Carter']
actors2=['Johnny Depp','Ian McKellen']
actors3=['Vin Diesel','Paul Walker']
actors4=['Adam Sandler','Kevin James']
actors5=['Daniel Radcliffe','Rupert Grint']
print('1:',data[(data.cast.str.contains(actors1[0]))&(data.cast.str.contains(actors1[1]))].imdb_id.count())
print('2:',data[(data.cast.str.contains(actors2[0]))&(data.cast.str.contains(actors2[1]))].imdb_id.count())
print('3:',data[(data.cast.str.contains(actors3[0]))&(data.cast.str.contains(actors3[1]))].imdb_id.count())
print('4:',data[(data.cast.str.contains(actors4[0]))&(data.cast.str.contains(actors4[1]))].imdb_id.count())
print('5:',data[(data.cast.str.contains(actors5[0]))&(data.cast.str.contains(actors5[1]))].imdb_id.count())


# In[611]:


answer_ls.append(5)


# # 36. У какого из режиссеров выше вероятность выпустить фильм в прибыли? (5 баллов)101
# Варианты ответа:
# 1. Quentin Tarantino
# 2. Steven Soderbergh
# 3. Robert Rodriguez
# 4. Christopher Nolan
# 5. Clint Eastwood

# In[612]:


directors=['Quentin Tarantino','Steven Soderbergh','Robert Rodriguez','Christopher Nolan','Clint Eastwood']
for director in directors:
    income_movies=data[(data.director.str.contains(director))&(data.income>0)].imdb_id.count()
    movies=data[data.director.str.contains(director)].imdb_id.count()
    print(income_movies/movies)


# In[613]:


answer_ls.append(4)


# # Submission

# In[620]:


len(answer_ls)


# ### pd.DataFrame({'Id':range(1,len(answer_ls)+1), 'Answer':answer_ls}, columns=['Id', 'Answer'])

# In[ ]:




