import json

MIN_LON, MIN_LAT = 4.82, 52.385
MAX_LON, MAX_LAT = 4.87, 52.41

def in_bbox(coords):
    lon, lat = coords[0], coords[1]  # handle [lon, lat, ...]
    return (MIN_LON <= lon <= MAX_LON) and (MIN_LAT <= lat <= MAX_LAT)

def geom_intersects_bbox(geom):
    gtype = geom["type"]

    if gtype == "Point":
        return in_bbox(geom["coordinates"])

    if gtype == "MultiPoint":
        return any(in_bbox(pt) for pt in geom["coordinates"])

    if gtype == "LineString":
        return any(in_bbox(pt) for pt in geom["coordinates"])

    if gtype == "MultiLineString":
        return any(in_bbox(pt) for line in geom["coordinates"] for pt in line)

    if gtype == "Polygon":
        return any(in_bbox(pt) for ring in geom["coordinates"] for pt in ring)

    if gtype == "MultiPolygon":
        return any(
            in_bbox(pt)
            for poly in geom["coordinates"]
            for ring in poly
            for pt in ring
        )

    if gtype == "GeometryCollection":
        return any(geom_intersects_bbox(g) for g in geom.get("geometries", []))

    return False

def filter_geojson_in_bbox(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    selected = [f for f in features if geom_intersects_bbox(f["geometry"])]

    out = {"type": "FeatureCollection", "features": selected}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)

if __name__ == "__main__":
    input_file = "data-pipes-2.geojson"  # <- fix this
    output_file = "havenstad_subset.geojson"
    filter_geojson_in_bbox(input_file, output_file)
