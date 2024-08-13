<a href="https://signpath.org"> <img src="docs/assets/signpath-logo.svg" width="500px"> </a>

# SignPath Foundation Website

This repository contains the SignPath Foundation website data. It runs on Github pages, which is built upon [Jekyll](https://jekyllrb.com).

## Running it locally
There are two ways of running the application locally: Either directly using a local Ruby installation or by using Docker. In both setups the website will be reachable on [http://localhost:4000](http://localhost:4000)

### Running it on local Ruby installation
You need to have Ruby and RubyGems installed. See the [official documentation of Jekyll](https://jekyllrb.com/docs/installation/).
Then, run the following command to install all dependencies:

	gem install jekyll bundler
	bundle install

To run the installation locally, you need to execute

	bundle exec jekyll serve

### Running it using Docker
You need to have Docker installed.
Then, run the following command (in PowerShell):

	docker run --rm -e JEKYLL_ENV=docker --label=jekyll --volume=${PWD}/docs:/srv/jekyll -it -p 127.0.0.1:4000:4000 jekyll/jekyll jekyll serve --force_polling
