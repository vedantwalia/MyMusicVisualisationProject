# MyMusicVisualisationProject


A small project I decided to bulid for getting better hands on experience with Pandas.

You can run `pip install -r requirements.txt` after cloning the repo to ensure that you have all the libraries required to replicate the project.


I shall also try to emulate this project on PowerBI, for which I intend to covert the XML file to JSON since I prefer working with the same in the Power Query Editor. Since Apple uses the nortious to parse 'plist' format for the XML, I have used two python scripts, one to swap the `<date>` tags in the XML with `<string>` tag since JSON doesn't have a `date` datatype, which causes type errors.

You can use the `XmlToJson.py` script to convert the plist XML to JSON. The script essentially replaces the tags in the XML and then converts the XML to JSON.

If you are on MacOS, you can also use the `plutil` command to convert the XML to JSON. (Please note that the `<date>` elements have to be converted to `<string>` first)

`plutil -convert json -o output.json input.plist`
