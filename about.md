---
---
Hello, This is ITE3068: Software Studio 2 @ cs.hanyang Wiki!

First of all, check my [web site](https://blog.maydev.org/ITE3068/) demo! The website is built with [jekyll](https://jekyllrb.com/) and is operated by [GitHub-Pages](https://pages.github.com/). See README.md on front page of repository to check how to build and run.

I'm using *traffic accident statistics data* from [Korea Public Data Portal](https://www.data.go.kr/).

There are four example using [billboard.js](https://naver.github.io/billboard.js/) and [d3.js](https://d3js.org/). Each page contain some comments, charts and some interactive buttons to change chart. At the end, it shows what technology was used with link.

The code is simple, easy to understand, and has no additional description.

- [요일별 사고](https://blog.maydev.org/ITE3068/posts/accident_by_days/)
- [시간별 사고](https://blog.maydev.org/ITE3068/posts/accident_by_hours/)
- [연령별 사고](https://blog.maydev.org/ITE3068/posts/accident_by_age/)
- [지역별 사고](https://blog.maydev.org/ITE3068/posts/accident_by_states/)

## 요일별 사고

Displays incident data by day of the year in 2016. The number of occurrences, deaths, and casualties are displayed in a line-chart. It's very simple and it shows only the data. Data driven by template engine in jekyll.

## 시간별 사고

This page covers more complex fetures. First, after showing accident statistics by day of the week in a simple line-chart, on below display the accident statistics for each day of the week. The maximum minimum axis changes according to the size of the data. And dynamically fetches and displays data each time you press each button. It is a little more natural to import data by time difference(But 
billboard.js performance is not very good because there is a hurdle. This part needs to be improved in the future).

## 연령별 사고
This page uses the Donut graph. The implemented features are mostly same as above page. And custom legend applied with `padAngle`. Also dynamic load from `csv` on button event.

## 지역별 사고
It is awesome geometry-graph of Korea using D3.js!!! Also below button display different type of accidents. The darker color means more counts of accidents and red is none-data-area. Depends on svg, using `geoMercator`, `scaleQuantize`, `geoPath`, ... and many features... The detail codes is very simple and easy to recognize. Grab data from web and build dynamically on button event. (But magic variable directly used. It will fixed next time.)

# Review
Using billboard.js was a very fun experience and beneficial. Explain itself as *Re-usable, easy interface JavaScript chart library, based on D3 v4+.* and really it is! D3.js is a JavaScript library for producing dynamic, interactive data visualizations in web browsers. And It is very useful and widely used. billboard.js froked from D3.js but it is more interactive, colorful and easy to use. There was a version conflict problem using D3.js, but it was not difficult. billboard.js is noteworthy in that it takes advantage of the widely used D3.js and is easier and simpler to use.
