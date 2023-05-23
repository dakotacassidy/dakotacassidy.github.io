# loading packages

library(ggpubr)
library(tidyverse)
library(here)
library(skimr)
library(janitor)
library(lubridate)
library(ggrepel)
library(ggplot2)
library(dplyr)

# importing datasets

activity <- read.csv('C:\\Users\\cococ\\Downloads\\archive\\Fitabase Data 4.12.16-5.12.16\\dailyActivity_merged.csv')
weight <- read.csv('C:\\Users\\cococ\\Downloads\\archive\\Fitabase Data 4.12.16-5.12.16\\weightLogInfo_merged.csv')
sleep <- read.csv('C:\\Users\\cococ\\Downloads\\archive\\Fitabase Data 4.12.16-5.12.16\\sleepDay_merged.csv')
intensities <- read.csv('C:\\Users\\cococ\\Downloads\\archive\\Fitabase Data 4.12.16-5.12.16\\hourlyIntensities_merged.csv')

# preview datasets

head(activity)
view(activity)

head(weight)
view(weight)

head(sleep)
view(sleep)

head(intensities)
view(intensities)

## cleaning and formatting

# verifying number of users

n_distinct(activity$Id)
n_distinct(intensities$Id)
n_distinct(sleep$Id)
n_distinct(weight$Id)

# checking for duplicates

sum(duplicated(activity))
sum(duplicated(intensities))
sum(duplicated(sleep))

# remove duplicates and NA

activity <- activity %>%
  distinct() %>%
  drop_na()

intensities <- intensities %>%
  distinct() %>%
  drop_na()

sleep <- sleep %>%
  distinct() %>%
  drop_na()

# verify removal of duplicates

sum(duplicated(sleep))

# clean and rename columns

clean_names(activity)
activity <- rename_with(activity, tolower)

clean_names(intensities)
intensities <- rename_with(intensities, tolower)

clean_names(sleep)
sleep <- rename_with(sleep, tolower)

# consistent date format

sleep <- sleep %>%
  rename(date = sleepday) %>%
  mutate(date = as_date(date, format ="%m/%d/%Y"))

activity <- activity %>%
  rename(date = activitydate) %>%
  mutate(date = as_date(date, format = "%m/%d/%Y"))

view(activity)
view(sleep)

intensities <- intensities %>% 
  rename(date_time = activityhour) %>% 
  mutate(date_time = as.POSIXct(date_time,format ="%m/%d/%Y %I:%M:%S %p" , tz=Sys.timezone()))

head(intensities)

## merging datasets

activity_sleep <- merge(activity, sleep, by=c ("id", "date"))
view(activity_sleep)

##correlations

ggplot(data=activity_sleep, aes(x=totalminutesasleep, y=sedentaryminutes)) + 
  geom_point() + geom_smooth() + labs(title="Sedentary Minutes vs. Total Minutes Asleep")

## intensities data

int_new <- intensities %>%
  group_by(time) %>%
  summarise(mean_total_int = mean(TotalIntensity))

ggplot(data=int_new, aes(x=time, y=mean_total_int)) + geom_histogram(stat = "identity", fill='darkgreen') +
  theme(axis.text.x = element_text(angle = 90)) +
  labs(title="Average Total Intensity vs. Time")