# Target Detect

Detects images with a specified 'target' image in a folder and returns matching filenames

Usage:
```
docker run --rm -v ./files:/home/files -v ./target:/home/target target_detect
```
where /files is the folder with your files and /target has your target.png file.
