import metadata_parser
import json

from Metadata.models import Metadata

def retrive_metadata(url):

    try:
        page = metadata_parser.MetadataParser(url)
    except:
        res = Metadata(web_page=url)
        return res
        
    data = page.metadata
    # print(data)

    res = Metadata(web_page=url)

    if 'og' in data and ('title' in data["og"] or 'Title' in data["og"]):
        if 'title' in data["og"]:
            res.title = data["og"]["title"]
        elif 'Title' in data["og"]:
            res.title = data["og"]["Title"]
    elif 'meta' in data and ('title' in data["meta"] or 'Title' in data["meta"]):
        if 'title' in data["meta"]:
            res.title = data["meta"]["title"]
        elif 'Title' in data["meta"]:
            res.title = data["meta"]["Title"]
    elif 'page' in data and ('title' in data["page"] or 'Title' in data["page"]):
        if 'title' in data["page"]:
            res.title = data["page"]["title"]
        elif 'Title' in data["page"]:
            res.title = data["page"]["Title"]


    if 'og' in data and ('description' in data["og"] or 'Description' in data["og"]):
        if 'description' in data["og"]:
            res.description = data["og"]["description"]
        elif 'Description' in data["og"]:
            res.description = data["og"]["Description"]
    elif 'meta' in data and ('description' in data["meta"] or 'Description' in data["meta"]):
        if 'description' in data["meta"]:
            res.description = data["meta"]["description"]
        elif 'Description' in data["meta"]:
            res.description = data["meta"]["Description"]
    elif 'page' in data and ('description' in data["page"] or 'Description' in data["page"]):
        if 'description' in data["page"]:
            res.description = data["page"]["description"]
        elif 'Description' in data["page"]:
            res.description = data["page"]["Description"]

    if 'og' in data and 'image' in data["og"]:
        res.thumbnail = data["og"]["image"]
    elif 'meta' in data and 'image' in data["meta"]:
        res.thumbnail = data["meta"]["image"]
    elif 'page' in data and 'image' in data["page"]:
        res.thumbnail = data["page"]["image"]

    print(res)
    return res