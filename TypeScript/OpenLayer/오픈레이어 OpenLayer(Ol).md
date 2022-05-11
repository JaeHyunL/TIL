# 오픈레이어 OpenLayer(Ol)

## 오픈레이어란(?)

오픈레이어란 웹 브라우저에서 지도데이터를 표시하기 위한 자바스크립트 라이브러리 도구이다.

[OpenLayers - Welcome](https://openlayers.org/)

모든 웹 페이지에 동적 지도를 쉽게 넣을 수 있다. 모든 소스에서 로드된 지도 타일, 백터 데이터 마커를 표시할 수 있음.

## 지도 생성

[Accessible Map](https://openlayers.org/en/latest/examples/accessible.html)

해당 링크 참조

```jsx
import 'ol/ol.css';
import Map from 'ol/Map';
import OSM from 'ol/source/OSM';
import TileLayer from 'ol/layer/Tile';
import View from 'ol/View';

const map = new Map({
  layers: [
    new TileLayer({
      source: new OSM(),
    }),
  ],
  target: 'map',
  view: new View({
    center: [0, 0],
    zoom: 2,
  }),
});

document.getElementById('zoom-out').onclick = function () {
  const view = map.getView();
  const zoom = view.getZoom();
  view.setZoom(zoom - 1);
};

document.getElementById('zoom-in').onclick = function () {
  const view = map.getView();
  const zoom = view.getZoom();
  view.setZoom(zoom + 1);
};
```

위 예제는 OSM (OpenStreetMap 기준으로 작성된 코드이다.

해당하는 코드로 OSM 지도를 띄울 수 있다.

```jsx
const url = `http://api.vworld.kr/req/wmts/1.0.0/${API_KEY}/${vWorldInfo[theme]['layer']}/{z}/{y}/{x}.${vWorldInfo[theme]['format']}`;

const layer = new Tile({
		opacity: 1,
		source: new XYZ({ url }),
		visible,
		zIndex: vWorldInfo[theme]['zIndex'],

	});
```

위 예제는 Tile로 지도를 생성하여 VWORD 지도를 가져오는 예제이다.

[공간정보 오픈플랫폼 포털](https://www.vworld.kr/v4po_main.do)

VWORD 같은 경우 한국어로 잘 설명되어있기에 별도로 설명은 진행하지 않는다.