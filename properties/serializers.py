from rest_framework import serializers

from .models import Location, Project, RealProperty, Unit

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('status', 'last_update')

class RealPropertySerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)
    class Meta:
        model = RealProperty
        fields = ('description', 'category', 'lowest_price', 'highest_price', 'lot_area')
        depth = 1
    

class ProjectSerializer(serializers.ModelSerializer):
    real_properties = RealPropertySerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ('name', 'location')
        depth = 1


class LocationSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('municipality', 'province')
        depth = 1

