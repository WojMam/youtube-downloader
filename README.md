# qr_generator

YouTube Downloader is a small side project that enables quick download of youtube videos.

## Pre-requisities

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all
required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

User can use application GUI to input youtube links. To run the GUI below command must be executed from the project root directory:

```bash
python main.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to check pylint results in the Actions tab after commiting.

Last commit Pylink status:

[![Pylint](https://github.com/WojMam/youtube-downloader/actions/workflows/pylint.yml/badge.svg)](https://github.com/WojMam/youtube-downloader/actions/workflows/pylint.yml)

## Plans for the future:

- [x] Create PoC
- [x] Create the plans foe the future
- [x] Create new GUI template using custom tkinter
- [ ] Create special cases for videos that needs the user to be logged in
- [x] Create preview image with the data about the clip
- [x] Create dummy image for the "before vide load" state
- [x] Disable the download button at start of the App
- [x] Create a dropdown with the different resolutions to download video
- [ ] Add the icon in the main frame of the app window, above all elements
- [ ] Add icons to the buttons
- [x] Add app icon
- [x] Add URl verification mechanism
- [x] Add the function to open results directory
- [x] Add deletion of miniature when the app is closed
- [ ] Add possibility to download higher resolutions (not only progressive streams)
- [ ] Add a progress bar for downloading
- [ ] Add a progress animation (?) for loading a preview
- [x] Fix issue with wrong default value for scaling
- [ ] Add a possibility to download preview image

## License

[MIT](https://choosealicense.com/licenses/mit/)
