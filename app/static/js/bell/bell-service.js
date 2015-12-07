'use strict';

angular.module('bell')
  .factory('Bell', ['$resource', function ($resource) {
    return $resource('bell/bells/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
