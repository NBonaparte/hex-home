#!/bin/bash
python generate.py
mkdir -p public/
cp index.html public/
cp -r fonts/ public/
cp -r icons/ public/
cp -r favicon/ public/
cp *.css public/
cp *.svg public/
