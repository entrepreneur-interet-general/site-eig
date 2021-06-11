FROM "jekyll/jekyll"
WORKDIR  /srv/jekyll
# Define jekyll user id and group id as current user id and group id.
# will be then used to chown every jekyll folder https://github.com/envygeeks/jekyll-docker/blob/master/repos/jekyll/copy/all/usr/jekyll/bin/entrypoint
ARG JEKYLL_UID
ARG JEKYLL_GID
# At build time (before entrypoint) jekyll is still 1000:1000 so we force it to be able to run bundle install.
RUN usermod  -o -u "$JEKYLL_UID" jekyll
RUN groupmod -o -g "$JEKYLL_GID" jekyll
# Copy must be chown with jekyll:jekyll to avoid permission conflict when bundle install (with jekyll user) try to update Gemfile.lock
# https://github.com/envygeeks/jekyll-docker/blob/575057ab5f14055e161b871e75f8295afd571aa9/repos/jekyll/copy/all/usr/jekyll/bin/bundle#L16
COPY --chown=jekyll:jekyll Gemfile* ./
RUN bundle install
# No need to chown src files as this is carried by entrypoint
COPY . .
# Avoid permission conflict running jekyll serve at runtime
RUN chown -R jekyll:jekyll /srv/jekyll
CMD jekyll serve --config _config.yml,_config_dev.yml