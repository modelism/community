var App = angular.module("App", []);

App.config([
    '$interpolateProvider', function($interpolateProvider) {
        return $interpolateProvider.startSymbol('{(').endSymbol(')}');
    }
]);

App.controller("NewsListM", function($scope, $http) {
    $scope.showData = function() {
        $scope.curPage = 0;
        $scope.pageSize = 9;
        $http.get('/json/newsmodelism.json').then(function(res){
            $scope.newslist = res.data;
        });
        $scope.numberOfPages = function() {
            return Math.ceil($scope.newslist.length / $scope.pageSize);
        };
    };
});

angular.module("App").filter('pagination', function() {
    return function(input, start) {
        start = +start;
        return input.slice(start);
    };
});
