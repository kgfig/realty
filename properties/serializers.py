from rest_framework import serializers

from .models import Location, Project, RealProperty, Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'status')

class RealPropertySerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = RealProperty
        fields = ('id', 'description', 'category', 'lowest_price', 'highest_price', 'lot_area', 'units')
        depth = 1
    

class ProjectSerializer(serializers.ModelSerializer):
    real_properties = RealPropertySerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ('id', 'name', 'location', 'real_properties')
        depth = 1


class LocationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'municipality', 'province', 'projects')
        depth = 1

