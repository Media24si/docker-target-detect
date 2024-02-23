# Target Detect

Detects images with a specified 'target' image in a folder and returns matching filenames

Usage:
```
docker run --rm -v ./files:/home/files -v ./target:/home/target media24si/target_detect:latest [-t template_name] [-th threshold]
```
where:
- `/files` is the folder with your files
- `/target` has your template file
- `-t` or `--template` is an optional argument to specify the template name (default: `target.png`)
- `-th` or `--threshold` is an optional argument to specify the threshold (default: 0.7)
