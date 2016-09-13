/**
 * Created by Administrator on 2016/8/26.
 * 头部
 */
/*导航条*/
var nav="";
var url = location.href; //获取url中"?"符后的字串
if (url.indexOf("blog") != -1) {
    nav='博客';
}else if(url.indexOf("photos") != -1){
    nav='照片墙';
}else if(url.indexOf("full") != -1){
    nav='博客';
}else{
    nav='首页';
}
app.controller('nav',function ($scope) {
    $scope.navList=[
        {
            name:'首页',
            href:'/'
        },
        {
            name:'关于我',
            href:'#aboutMe'
        },
        {
            name:'博客',
            href:'/blog'
        },{
            name:'照片墙',
            href:'/photos'
        }
    ];
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