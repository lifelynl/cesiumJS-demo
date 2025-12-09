# CesiumJS Triply Demo

This is a proof-of-concept demo based on the provided research. It demonstrates:
1.  Initializing a CesiumJS Viewer.
2.  Loading vector data (simulating Triply API output) from a GeoJSON file.
3.  Using a Clipping Plane to create a cross-section view (for underground visualization).

## How to Run

Because this demo loads an external data file (`stub_data.geojson`), you cannot simply open the `index.html` file in your browser due to security restrictions (CORS). You must run a local web server.

### Using npx (Node.js)
If you have Node.js installed, run:

```bash
npx serve .
```

Then open the URL shown (usually `http://localhost:3000`).

### Using Python
Alternatively, if you have Python installed:

```bash
python3 -m http.server
```

Then open `http://localhost:8000`.
