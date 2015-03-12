var App = angular.module("App", []);

App.config([
    '$interpolateProvider', function($interpolateProvider) {
        return $interpolateProvider.startSymbol('{(').endSymbol(')}');
    }
]);

App.controller("EventsListM", function($scope, $http, $filter) {
    $scope.showData = function() {
        var today_date = new Date();
        $scope.dt = $filter('date')(today_date, 'yyyyMMdd');
        $scope.curPage = 0;
        $scope.pageSize = 9;
        $scope.eventslist = [];
        $http.get('/json/events.json').then(function(res){
            $scope.eventslist = res.data;
        });
        $scope.numberOfPages = function() {
            return Math.ceil($scope.eventslist.length / $scope.pageSize);
        };
        $scope.filterWIthSearch = function() {
            var items = $filter('filter')($scope.eventslist, ($scope.search||{}).categories||"");
            $scope.numberOfPages = Math.ceil(items.length / $scope.pageSize);
            if ($scope.numberOfPages<($scope.curPage+1)){
                $scope.curPage = 0;
            };
            items = $filter('pagination')(items, $scope.curPage*$scope.pageSize);
            items = $filter('orderBy')(items, '-event_starts');
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
