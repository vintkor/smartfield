{% extends "gis/admin/openlayers.js" %}
{% block base_layer %}

    new OpenLayers.Layer.Google("Google Satellite", {
        type: google.maps.MapTypeId.SATELLITE,
        numZoomLevels: 22
    });
    var gmap_hybrid = new OpenLayers.Layer.Google("Google Hybrid", {
        type: google.maps.MapTypeId.HYBRID,
        numZoomLevels: 22
    });

    var gmap = new OpenLayers.Layer.Google("Google Streets", {
        numZoomLevels: 20
    });

	{{ module }}.map.addLayer(geodjango_polygon.layers.base);
	{{ module }}.map.addLayer(gmap_hybrid);
	{{ module }}.map.addLayer(gmap);

{% endblock %}