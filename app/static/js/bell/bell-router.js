'use strict';

angular.module('bell')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/bells', {
        templateUrl: 'views/bell/bells.html',
        controller: 'BellController',
        resolve:{
          resolvedBell: ['Bell', function (Bell) {
            return Bell.query();
          }]
        }
      })
    }]);
