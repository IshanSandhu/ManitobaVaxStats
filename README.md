# Vaccine Statistic Visualizer

A program that generates charts displaying the progression of administered vaccines during the pandemic.

## Functions

```get_vaccine_num(bulletin_url)``` - uses urllib gather data on administered vaccines from daily news update on governement webpage (https://www.gov.mb.ca/covid19/vaccine/media.html)

```get_current_dict()``` - creates a dictionary of daily updates using get_vaccine_num(bulletin_url) by iterating through all posts

```get_bar_graph(dict)``` - generates bar graphs showing the number of immunizations by date

## note

This programs fetches URLs to gather data and the URLs may be outdated, last time fetched: January 2021
