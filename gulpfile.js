/**
 * Created by Administrator on 2016/9/6.
 */
var gulp = require('gulp'), //本地安装gulp所用到的地方
    cleanCSS = require('gulp-clean-css'),
    ngAnnotate = require('gulp-ng-annotate'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'), //合并js文件
    notify = require('gulp-notify'),
    ngmin = require('gulp-ngmin'),
    stripDebug = require('gulp-strip-debug'),
    concat = require('gulp-concat');
var watcher = gulp.watch('js/**/*.js', ['uglify','reload']);
watcher.on('change', function(event) {
    console.log('File ' + event.path + ' was ' + event.type + ', running tasks...');
});

/*压缩*/
gulp.task('cssminIndex', function () {
    return gulp.src(['dist/css/header.css','dist/css/index.css'])
        .pipe(concat('index.css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(cleanCSS({
            advanced: false,//类型：Boolean 默认：true [是否开启高级优化（合并选择器等）]
            //compatibility: 'ie7',//保留ie7及以下兼容写法 类型：String 默认：''or'*' [启用兼容模式； 'ie7'：IE7兼容模式，'ie8'：IE8兼容模式，'*'：IE9+兼容模式]
            keepBreaks: false,//类型：Boolean 默认：false [是否保留换行]
            keepSpecialComments: '1'
            //保留所有特殊前缀 当你用autoprefixer生成的浏览器前缀，如果不加这个参数，有可能将会删除你的部分前缀
        }))
        .pipe(gulp.dest('public/css'));
});
gulp.task('cssminblog', function () {
    return gulp.src(['dist/css/header.css','dist/css/blog.css'])
        .pipe(concat('blog.css'))
        .pipe(rename({suffix: '.min'}))
        .pipe(cleanCSS({
            advanced: false,//类型：Boolean 默认：true [是否开启高级优化（合并选择器等）]
            //compatibility: 'ie7',//保留ie7及以下兼容写法 类型：String 默认：''or'*' [启用兼容模式； 'ie7'：IE7兼容模式，'ie8'：IE8兼容模式，'*'：IE9+兼容模式]
            keepBreaks: false,//类型：Boolean 默认：false [是否保留换行]
            keepSpecialComments: '1'
            //保留所有特殊前缀 当你用autoprefixer生成的浏览器前缀，如果不加这个参数，有可能将会删除你的部分前缀
        }))
        .pipe(gulp.dest('public/css'));
});

gulp.task('scripts', function() {
    return gulp.src(['dist/js/myApp.js','dist/js/header.js','dist/js/index.js'])
        .pipe(ngAnnotate())
        .pipe(ngmin({dynamic: false}))
        .pipe(stripDebug())
        .pipe(uglify({outSourceMap: false}))
        .pipe(concat('index.min.js'))
        .pipe(gulp.dest('public/js/'))
});
gulp.task('default', function () {
    gulp.watch(['dist/css/header.css','dist/css/index.css'],[ 'cssminIndex']);
    gulp.watch(['dist/css/header.css','dist/css/blog.css'],[ 'cssminblog']);
    gulp.watch('dist/js/*.js', ['scripts']);
});
