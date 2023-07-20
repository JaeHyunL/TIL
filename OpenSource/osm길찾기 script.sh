docker run -d -v /data/bahamas-latest.osm.pbf:/data/bahamas-latest.osm.pbf -p 55555:8989 --env JAVA_OPTS="-Xmx2g -Xms2g" israelhikingmap/graphhopper:7.0 --input  /data/bahamas-latest.osm.pbf


docker run -it   -e PBF_PATH=/nominatim/data/ea.osm.pbf   -p 55553:8080   -v /data/aas/ea.osm.pbf:/nominatim/data/ea.osm.pbf   --name nominatim   mediagis/nominatim:4.2

docker run \
--privileged \
-v /data/bahamas-latest.osm.pbf:/data/target.osm.pbf \
-v /hdd/volumes/miis-osm-database:/data/database/ \
overv/openstreetmap-tile-server \
import


docker run \
    -v /absolute/path/to/luxembourg.osm.pbf:/data/region.osm.pbf \
    -v osm-data:/data/database/ \
    overv/openstreetmap-tile-server \
    import

docker run \
    -p 8080:80 \
    -v osm-data:/data/database/ \
    -v osm-tiles:/data/tiles/ \
    -d overv/openstreetmap-tile-server \
    run
