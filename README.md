# MyMusicVisualisationProject


A small project I decided to bulid for getting better hands on experience with Pandas.

You can run ```pip install -r requirements.txt``` after cloning the repo to ensure that you have all the libraries required to replicate the project.


I shall also try to emulate this project on PowerBI, for which I intend to covert the XML file to JSON since I prefer worknig with the same in the Power Query Editor. Since Apple uses the nortious to parse 'plist' format for the XML, I have used two python scripts, one to swap the `<date>` tags in the XML with `<string>` tag since JSON doesn't have a `date` datatype, which causes type errors.

First run the `UpdateTags.py` script to convert the headers of the xml followed by `XmlToJson.py` to get the required JSON file.

If you are on MacOS, you can also use the `plutil` command to convert the XML to JSON. (Please note that the `<date>` elements hav e to be converted to `<string>` first)

`plutil -convert json  output.xml`