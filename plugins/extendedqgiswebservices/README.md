# QGIS Extended WMS plugin

```
SERVICE=EWMS
REQUEST=GetLayerCustomProperties
```

Request:

```
curl http://localhost:8015/ogc/nepal_hazard?service=EWMS&request=GetLayerCustomProperties
```

Returns:

```json
{
    "carto-dark": {
        "identify/format": "Undefined",
        "layer_id": "d340eaa9-1d15-45cf-8983-a3e3b5343b92"
    },
    "carto-light": {
        "identify/format": "Undefined",
        "layer_id": "c3c2115d-8676-4136-8a9e-3e67183e4e04"
    },
    "esri-imagery": {
        "identify/format": "Undefined",
        "layer_id": "360de9fb-e3fb-49eb-af9d-70405e614d73"
    },
    "esri-physical": {
        "identify/format": "Undefined",
        "layer_id": "b00a6075-168d-40d7-9fd5-077d592e7b89"
    },
    "hazard-curves": {
        "calc_id": "5",
        "embeddedWidgets/count": "0",
        "engine_version": "3.4.0",
        "investigation_time": "50.0",
        "irmt_version": "3.4.0",
        "layer_id": "hcurves_50_0y_462f9fc6_cd92_4ac4_9b6f_97e573890f22",
        "output_type": "hcurves",
        "variableNames": [],
        "variableValues": []
    },
    "hazard-map-max": {
        "calc_id": "5",
        "embeddedWidgets/count": "0",
        "engine_version": "3.4.0",
        "investigation_time": "50.0",
        "irmt_version": "3.4.0",
        "layer_id": "hazard_map_max_50_0y_66e6b397_cae1_446a_ab3e_5967035dcd80",
        "output_type": "hmaps",
        "variableNames": [],
        "variableValues": []
    },
    "hazard-map-mean": {
        "calc_id": "5",
        "embeddedWidgets/count": "0",
        "engine_version": "3.4.0",
        "investigation_time": "50.0",
        "irmt_version": "3.4.0",
        "layer_id": "hazard_map_mean_50_0y_b2404d67_c9a5_454f_81f4_15acb2068cbf",
        "output_type": "hmaps",
        "variableNames": [],
        "variableValues": []
    },
    "mapbox": {
        "identify/format": "Undefined",
        "layer_id": "6633245d-7e0c-47e5-967e-480a3ac4eccc"
    },
    "natural-earth": {
        "identify/format": "Undefined",
        "layer_id": "60e65efa-3318-4def-897e-b3ccc001bbb1"
    },
    "natural-earth-dark": {
        "identify/format": "Undefined",
        "layer_id": "c7f2ea2e-29ce-4677-94e1-4526062dcb8d"
    },
    "natural-earth-gray": {
        "identify/format": "Undefined",
        "layer_id": "4ce84cb2-889f-4914-a08f-39dd5556d10b"
    },
    "openstreetmap": {
        "identify/format": "Undefined",
        "layer_id": "17192e54-54d4-49ea-8ce7-d8f4c65b7528"
    },
    "stamen-terrain": {
        "identify/format": "Undefined",
        "layer_id": "3661fa9b-7a59-42e6-a48c-69f07d76cc2f"
    },
    "thunderforest": {
        "identify/format": "Undefined",
        "layer_id": "4c57c9a5-c4fb-4cce-a336-ce982ee7c364"
    },
    "uhs-poe-001": {
        "calc_id": "5",
        "embeddedWidgets/count": "0",
        "engine_version": "3.4.0",
        "investigation_time": "50.0",
        "irmt_version": "3.4.0",
        "layer_id": "uhs_poe_0_1_50_0y_f67d4497_fb8b_4f8b_a6ad_f25442293c9c",
        "output_type": "uhs",
        "poe": "0.1",
        "variableNames": [],
        "variableValues": []
    },
    "uhs-poe-002": {
        "calc_id": "5",
        "embeddedWidgets/count": "0",
        "engine_version": "3.4.0",
        "investigation_time": "50.0",
        "irmt_version": "3.4.0",
        "layer_id": "uhs_poe_0_02_50_0y_fbc7a486_7918_4bd5_9518_ec6cece506ee",
        "output_type": "uhs",
        "poe": "0.02",
        "variableNames": [],
        "variableValues": []
    }
}
```
