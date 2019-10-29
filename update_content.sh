#!/bin/bash

# Handle absence of python2 gracefully
pythonTarget=$([ -x "$(command -v python2)" ] && echo "python2" || echo "python")

$pythonTarget main.py keyfile.json temp_content.json
cp temp_content.json ../../Apps/iPad/DisruptorsTableApp/content/disruptors_content_data.json
cp temp_content.json ../../Apps/KineticTabletop/KineticTabletop/bin/data/disruptors_content_data.json
cp temp_content.json ../Readability/data/disruptors_content_data.json
rm temp_content.json