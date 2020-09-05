from google_images_download import google_images_download

res = google_images_download.googleimagesdownload()

args = {"keywords":"polar bears, baloons, Beaches", "limit":20, "print_urls":True}

paths = res.download(args)

print(paths)