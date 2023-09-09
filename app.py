from flask import Flask, Response, request
import yt_dlp
from pathlib import Path


vid_paths = {}


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        vid_paths[info["original_url"]] = info["filename"]
        return [], info


app = Flask(__name__)


@app.route("/")
def get_video():
    url = request.args.get("url")

    with yt_dlp.YoutubeDL({
        "cookiefile": "newcookiefile.txt",
        "format": "mp4"
        # "cookies-from-browser": "firefox"

    }) as ydl:
        ydl.add_post_processor(MyCustomPP())
        ydl.download(url)

    return Response(
        Path(vid_paths[url]).read_bytes(),
        mimetype='video/mp4',
        content_type='video/mp4',
        direct_passthrough=True
    )
