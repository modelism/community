var App = angular.module("App", []);

App.config([
    '$interpolateProvider', function($interpolateProvider) {
        return $interpolateProvider.startSymbol('{(').endSymbol(')}');
    }
]);

App.controller("NewsListM", function($scope, $http, $filter) {
    $scope.showData = function() {
        $scope.curPage = 0;
        $scope.pageSize = 9;
        $scope.newslist = [];
        $http.get('/json/newsmodelism.json').then(function(res){
            $scope.newslist = res.data;
        });
        $scope.numberOfPages = function() {
            return Math.ceil($scope.newslist.length / $scope.pageSize);
        };
        $scope.filterWIthSearch = function() {
            var items = $filter('filter')($scope.newslist, ($scope.search||{}).categories||"");
            items = $filter('pagination')(items, $scope.curPage*$scope.pageSize);
            $scope.numberOfPages = Math.ceil(items.length / $scope.pageSize);
            items = $filter('limitTo')(items, $scope.pageSize);
            return items;
        };
    };
});

angular.module("App").filter('pagination', function() {
    return function(input, start) {
        start = +start;
        return input.slice(start);
    };
});
