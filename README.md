# ComfyUI Spectral

`ComfyUI Spectral` is a ComfyUI custom nodes library based on the [spectral](https://github.com/spectralpython/spectral), 
mainly used for visual processing of spectral files

## Install

You can choose to use [ComfyUI Manager's](https://github.com/ltdrdata/ComfyUI-Manager) `install via Git URL` 

Or manual installation:

1. clone to your `custom_nodes` folder
2. `cd ComfyUI_Spectral`
3. install dependencies `pip install -r reqirements.txt`
4. restart ComfyUI


## Notice

**_This repository is in the early stages of development, the functionality is not complete and may change in the future_**


## Workflow

![example_01](./images/preview.png)

download workflow: [example_01](./workflows/example_01.json)

## Nodes

- `Spectral Loader`: load spectral file, output `Spectral` object and preview image
- `ENVI Loader`: load imagery with associated ENVI header files and reading & writing spectral libraries with ENVI headers. 


## WIP

- plot nodes
- k-means node
- pca node
- calculate nodes
- save node
- preprocess nodes
