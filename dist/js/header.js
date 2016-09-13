/**
 * Created by Administrator on 2016/8/26.
 * 头部
 */
/*导航条*/
var nav="";
var url = location.href;
if (url.indexOf("blog") != -1||url.indexOf("full") != -1) {
    nav='博客';
}else if(url.indexOf("photo") != -1){
    nav='照片墙';
}else if(url.indexOf("aboutme") != -1){
    nav='关于我';
}else{
    nav='首页';
}
app.controller('nav',function ($scope,$http) {
    $scope.navList=[
        {
            name:'首页',
            href:'/'
        },
        {
            name:'博客',
            href:'/blog'
        },{
            name:'照片墙',
            href:'/photo'
        }  ,
        {
            name:'关于我',
            href:'/aboutme'
        }
    ];
    console.log($scope.navList);
    $scope.Classify =nav;
    $scope.showClassify = function (data) {
        $scope.Classify = data;
    };
    $scope.classActive = function (data) {
        if(data == $scope.Classify) {
            return true;
        } else {
            return false;
        }
    }
});