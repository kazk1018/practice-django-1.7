
gulp = require 'gulp'
bower = require 'gulp-bower'
filter = require 'gulp-filter'
concat = require 'gulp-concat'

config =
  bowerDest: 'bower_components'

gulp.task 'bower', ->
  bower()
    .pipe gulp.dest config.bowerDest

