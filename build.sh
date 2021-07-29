#!/bin/bash
python generate.py
if [ -z "$out" ]; then out="public/"; fi
mkdir -p $out/
cp index.html $out/
cp -r fonts/ $out/
cp -r favicon/ $out/
cp *.css $out/
cp *.svg $out/
