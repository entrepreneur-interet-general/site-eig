FROM "jekyll/jekyll"
WORKDIR  /app
COPY ./Gemfile* .
RUN bundle install
COPY . .
CMD jekyll serve --config _config.yml,_config_dev.yml
