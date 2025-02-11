from mitmproxy import http

def response(packet):
    content_type = packet.response.headers.get("content-type", "")

    try:
        if "image" in content_type:
            url = packet.request.url
            extension = content_type.split("/")[-1]

            if extension == "jpeg":
                extension = "jpg"

            filename = f"images/{url.replace('/', '_')}.{extension}"
            image_data = packet.response.content

            with open(filename, "wb") as f:
                f.write(image_data)

            print(f"[+] Image saved: {filename}")
    except:
        pass