'use strict';

angular.module('bell')
  .controller('BellController', ['$scope', '$modal', 'resolvedBell', 'Bell',
    function ($scope, $modal, resolvedBell, Bell) {

      $scope.bells = resolvedBell;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.bell = Bell.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        Bell.delete({id: id},
          function () {
            $scope.bells = Bell.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          Bell.update({id: id}, $scope.bell,
            function () {
              $scope.bells = Bell.query();
              $scope.clear();
            });
        } else {
          Bell.save($scope.bell,
            function () {
              $scope.bells = Bell.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.bell = {
          
          "create_time": "",
          
          "update_time": "",
          
          "request_time": "",
          
          "is_played": "",
          
          "repeat_times": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var bellSave = $modal.open({
          templateUrl: 'bell-save.html',
          controller: 'BellSaveController',
          resolve: {
            bell: function () {
              return $scope.bell;
            }
          }
        });

        bellSave.result.then(function (entity) {
          $scope.bell = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('BellSaveController', ['$scope', '$modalInstance', 'bell',
    function ($scope, $modalInstance, bell) {
      $scope.bell = bell;

      
      $scope.create_timeDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };
      $scope.update_timeDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };
      $scope.request_timeDateOptions = {
        dateFormat: 'yy-mm-dd',
        
        
      };

      $scope.ok = function () {
        $modalInstance.close($scope.bell);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
