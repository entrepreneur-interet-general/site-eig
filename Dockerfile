FROM "jekyll/jekyll"
WORKDIR  /srv/jekyll
COPY --chown=jekyll:jekyll . .
CMD jekyll serve --config _config.yml,_config_dev.yml
