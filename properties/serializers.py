from rest_framework import serializers

from .models import Location, Project, RealProperty, Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'status')

class RealPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = RealProperty
        fields = ('id', 'name', 'description', 'category', 'lowest_price', 'highest_price', 'lot_area', 'floor_area')
        depth = 1
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'location')
        depth = 1


class LocationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'municipality', 'province', 'projects')
        depth = 1

