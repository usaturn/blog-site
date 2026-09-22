project = "星のダンスを見においで"
author = "usaturn"
copyright = "2012–2026, usaturn"

language = "ja"
extensions = ["maatlog"]
html_theme = "maatlog-default"
html_baseurl = "https://blog.usaturn.net/"
html_static_path = ["_static"]
html_logo = "_static/usaturn_logo.png"
html_favicon = "_static/usaturn_icon.png"

maatlog_timezone = "Asia/Tokyo"

maatlog_tags = {
    "ubuntu": "Ubuntu",
    "linux": "Linux",
    "resonite": "Resonite",
    "vr": "VR",
    "gentoo": "Gentoo",
    "container": "Container",
    "kvm": "KVM",
    "libvirt": "libvirt",
    "qemu": "QEMU",
    "videogame": "Videogame",
    "cli": "CLI",
    "development": "Development",
    "pyhack": "pyhack",
    "python": "Python",
    "sphinx": "Sphinx",
    "it-study-group": "IT勉強会",
    "memo": "備忘録",
    "ai": "AI",
}

maatlog_categories = {
    "it-technology": "IT Technology",
    "linux": "Linux",
    "other": "Other",
    "virtualization": "Virtualization",
    "misc": "駄文",
}

maatlog_authors = {
    "usaturn": "usaturn",
}

maatlog_author_profiles = {
    "usaturn": {
        "role": "Gentoo 系インフラエンジニア",
        "avatar": "_static/usaturn_icon.png",
        "links": [
            {"type": "x", "url": "https://x.com/usaturn"},
            {"type": "github", "url": "https://github.com/usaturn"},
        ],
        "about_docname": "about",
    },
}

maatlog_home_docname = "index"

maatlog_archive_docname = "blog"

maatlog_page_size = 10

maatlog_generate_feeds = True

maatlog_feed_taxonomies = ("tag", "category", "author", "month")

maatlog_feed_limit = 20

# warning.rst is an include fragment, not a standalone page.
exclude_patterns = ["_build", "contents/2012/warning.rst"]
