# Target Detect

Detects images with a specified 'target' image in a folder and returns matching filenames

Usage:
```
docker run --rm -v ./files:/home/files -v ./target:/home/target media24si/target_detect:latest [template_name]
```
where `/files` is the folder with your files and `/target` has your template file (default name: `target.png`)
