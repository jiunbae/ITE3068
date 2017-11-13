Software Studio @ cs.hanynag

Duplicated in [GitHub](https://github.com/MaybeS/ITE3068) for sort out my tasks.

## Sample page using [billboard.js](https://naver.github.io/billboard.js/)

Assignment requirements

- using [billboard.js](https://naver.github.io/billboard.js/)
- usign [d3.js](https://d3js.org/)
- Make [wiki](https://hconnect.hanyang.ac.kr/SW_studio2_2017/2015004584/wikis/home) on gitlab(provided by class)

## Website on [GitHub Pages](https://pages.github.com/)

See also [my page](https://blog.maydev.org/ITE3068/).

## Run on localhost

### Prepare environments 

- [Ruby](https://www.ruby-lang.org/en/downloads/) version above `2.1` (depends on jekyll)
- [RubyGems](https://rubygems.org/pages/download)
- Install [jekyll](https://jekyllrb.com/docs/installation/) using gem

```
gem install bundler
gem install jekyll
bundle update
```

See also `Gemfile.lock` to dependency.

### Run

Running site using jekyll, redefine baseurl because server setting is different with localhost.

```
jekyll serve --baseurl /
```
