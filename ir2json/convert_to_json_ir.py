from json import dump
from brukeropusreader import read_file


def convert(filenames):
    """convert files from dotZero to json

    Args:
        filenames (List[str]): list of filenames with path. each path must be a string
    """
    for filename in filenames:
        sample_dict = {}
        sample_dict["Sample Name"] = filename.split("/")[-1].replace(".0", "")

        opus_data = read_file(filename)
        x = [round(i) for i in opus_data.get_range("AB")[:-1]]
        y = [round(i, 4) for i in opus_data["AB"][0 : len(x)]]

        sample_dict["x"] = x
        sample_dict["y"] = y
        # write to a json file
        with open(filename.replace(".0", ".json"), "w") as outfile:
            dump(sample_dict, outfile)
